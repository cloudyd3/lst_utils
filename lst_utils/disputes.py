# -*- coding: utf-8 -*-
import argparse

import gspread
from gspread.utils import ValueInputOption

from . import structs


def main():
    parser = argparse.ArgumentParser(description="Filtering and formatting LST disputes")
    parser.add_argument("-s", "--source", help="Source Google spreadsheet key", required=True)
    parser.add_argument("-st", "--source_tab", help="Source Google spreadsheet tab name", required=True)
    parser.add_argument("-d", "--destination", help="Destination Google spreadsheet key", required=True)
    parser.add_argument("-dt", "--destination_tab", help="Destination Google spreadsheet tab name", required=True)
    parser.add_argument("-c", "--credentials", help="Google credentials file", required=False)
    parser.add_argument("-i", "--index", help="Starting index", required=False)
    args = parser.parse_args()
    gc = gspread.oauth()
    source_sheet = gc.open_by_key(args.source)
    source_tab = source_sheet.worksheet(args.source_tab)
    destination_sheet = gc.open_by_key(args.destination)
    destination_tab = destination_sheet.worksheet(args.destination_tab)
    source_data = source_tab.get_all_records()
    for i, row in enumerate(source_data):
        if args.index is not None:
            if i < int(args.index) - 2:
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
        destination_tab.update('A{}'.format(len(destination_tab.col_values(1)) + 1),
                               [[dispute.date, dispute.playerName, dispute.order, dispute.playerStatus, dispute.game,
                                 dispute.violation,
                                 dispute.punishment, dispute.comment]],
                               value_input_option=ValueInputOption.user_entered)


if __name__ == "__main__":
    main()
