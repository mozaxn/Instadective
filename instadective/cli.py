#!/usr/bin/env python3

import argparse
from .core import find_nonfollowers

def main():

    # Create a parser
    parser = argparse.ArgumentParser()

    # Add arguments to the parser
    parser.add_argument("-s", "--sessionid", required=True, help="Instagram Session ID")

    # Parse the arguments
    args = parser.parse_args()

    # Execute the main command
    find_nonfollowers(args.sessionid)

if __name__ == "__main__":
    main()