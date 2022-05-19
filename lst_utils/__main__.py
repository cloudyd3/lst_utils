# -*- coding: utf-8 -*-
import argparse
import sys

from . import parse_disputes
from . settings import __version__


def get_args():
    description = "Filtering and formatting LST disputes"
    arg = argparse.ArgumentParser(description=description)
    arg.add_argument("-s", "--source_key",
                     help="Source Google spreadsheet key")
    arg.add_argument("-st", "--source_tab",
                     help="Source Google spreadsheet tab name")
    arg.add_argument("-d", "--destination_key",
                     help="Destination Google spreadsheet key")
    arg.add_argument("-dt", "--destination_tab",
                     help="Destination Google spreadsheet tab name")
    arg.add_argument("-c", "--credentials",
                     help="Google credentials file")
    arg.add_argument("-i", "--index",
                     help="Starting index")
    arg.add_argument("-v", action="store_true",
                     help="Print \"lst_utils\" version.")
    return arg


def parse_args_exit(parser):
    """Process args that exit."""
    args = parser.parse_args()

    if args.v:
        parser.exit(0, "lst_utils %s\n" % __version__)

    if not args.source_key or \
            not args.source_tab or \
            not args.destination_key or \
            not args.destination_tab:
        parser.error("No input specified.\n"
                     "--source_key, --source_tab, --destination_key and --destination_tab are required.")

    if args.source_key and args.source_tab and args.destination_key and args.destination_tab:
        parse_disputes.parse_disputes(args.source_key, args.source_tab, args.destination_key, args.destination_tab,
                                      credentials=args.credentials, index=args.index)
        sys.exit(0)


def main():
    parser = get_args()
    parse_args_exit(parser)


if __name__ == "__main__":
    main()
