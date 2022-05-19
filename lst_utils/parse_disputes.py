# -*- coding: utf-8 -*-
import os
import shutil
from dataclasses import asdict

import gspread
from gspread.utils import ValueInputOption
from prettytable import PrettyTable

from . import structs
from .settings import CONF_DIR


def parse_disputes(source_key, source_tab, destination_key, destination_tab, **kwargs):
    """Parses LST disputes from a Google spreadsheet."""
    credentials = kwargs.get("credentials", None)
    index = kwargs.get("index", None)
    print("Parsing disputes from {}:{} to {}:{}".format(source_key, source_tab, destination_key, destination_tab))

    if not credentials:
        gc = gspread.oauth(credentials_filename=os.path.join(CONF_DIR, "credentials.json"),
                           authorized_user_filename=os.path.join(CONF_DIR, "authorized_user.json"))
    else:
        gc = gspread.oauth(credentials_filename=credentials,
                           authorized_user_filename=os.path.join(CONF_DIR, "authorized_user.json"))
        shutil.copy(credentials, os.path.join(CONF_DIR, "credentials.json"))

    source_sheet = gc.open_by_key(source_key).worksheet(source_tab)
    destination_sheet = gc.open_by_key(destination_key).worksheet(destination_tab)
    source_data = source_sheet.get_all_records()
    dispute_list = []
    x = PrettyTable()
    x.field_names = ["Date", "Player Name", "Order", "Player Status", "Game"]
    for i, row in enumerate(source_data):
        if index is not None:
            if i < int(index) - 2:
                continue
        if row["вина про"] != "ЕСТЬ":
            continue
        dispute = structs.Dispute()
        dispute.date = row['']
        dispute.playerName = row["Имя игрока"]
        dispute.order = row["Номер заказа"]
        dispute.playerStatus = row["current status"]
        dispute.game = row["game"]
        dispute.violation = row["violation"]
        dispute.punishment = row["punishment"]
        dispute.comment = row["комментарий"]
        dispute_list.append(list(asdict(dispute).values()))
        x.add_row(list(asdict(dispute).values())[:5])
    destination_sheet.update('A{}'.format(len(destination_sheet.col_values(1)) + 1),
                             dispute_list, value_input_option=ValueInputOption.user_entered)
    print(x)
