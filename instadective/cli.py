#!/usr/bin/env python3

import argparse
from .core import *

def main():

    # Create a parser
    parser = argparse.ArgumentParser()

    # Add arguments to the parser
    parser.add_argument("-s", "--sessionid", required=False, help="Your Instagram SESSION_ID")
    parser.add_argument("--scan", required=False, action="store_true", help="Perform core scan. This displays your followers and following. Use with flag -o to save the results to a file.")
    parser.add_argument("-o", "--out", required=False, help="Save the output of a scan to a directory. Mention the directory without the '/' at the end.")
    parser.add_argument("-n", "--non-follow", required=False, action="store_true", help="Identify accounts you follow but don't follow you back.")
    parser.add_argument("-c", "--compare", required=False, nargs=2, metavar=("SCAN1", "SCAN2"), help="Compare two core scans to identify changes in followers & following.")
    
    # Parse the arguments
    args = parser.parse_args()

    # Execute the main command
    session_id = args.sessionid
    _core_scan = args.scan
    _out = args.out
    _non_follow_scan = args.non_follow
    
    if args.compare:
        scan1, scan2 = args.compare

    if _core_scan:
        if _out:
            core_scan(session_id, output=_out)
        else:
            core_scan(session_id)

    elif _non_follow_scan:
        find_nonfollowers(session_id)

    elif args.compare:
        comparison(scan1, scan2)

if __name__ == "__main__":
    main()