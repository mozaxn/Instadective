# Imports
from instagrapi import Client
from pyfiglet import Figlet
import shutil
from yaspin import yaspin
import time
import json
from datetime import datetime
from colorama import Style, init
import sys
import os
import contextlib

# Used to suppress inherent errors in Instagrapi
@contextlib.contextmanager
def suppress_output():
    with open(os.devnull, 'w') as devnull:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = sys.stderr = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr


# Declare terminal width and version
TERMINAL_WIDTH = shutil.get_terminal_size().columns
VERSION = "1.0.0"

# Columns width standards
col_width = 32
names_per_row = TERMINAL_WIDTH // col_width

# Initialise colorama
init(autoreset=True)

# Printing the title
f = Figlet(font='epic')
title = f.renderText("insta dective")

for line in title.splitlines():
    print(Style.BRIGHT + line.center(TERMINAL_WIDTH) + Style.RESET_ALL)

print(("VERSION " + Style.BRIGHT + f"{VERSION}" + Style.RESET_ALL ).center(TERMINAL_WIDTH+8))
print(("DEVELOPED BY " + Style.BRIGHT + "ZAXN" + Style.RESET_ALL).center(TERMINAL_WIDTH+8))
print((Style.DIM + "mozaxn@protonmail.com" + Style.RESET_ALL).center(TERMINAL_WIDTH+8))
print("\n\n")

# Function for finding non-followers
def find_nonfollowers(session_id: str) -> None:
    """Finds accounts on Instagram you follow but don't follow you back."""
    
    # Create an instagrapi Client
    with yaspin(text="Performing non-follower scan..."):

        with suppress_output():
            cl = Client()

            # Login via SESSION ID
            cl.login_by_sessionid(session_id)

            # Retrieve the username (later to be used to get USER ID)
            username = dict(cl.account_info())['username']

            # Retrieve the USER ID
            user_id = cl.user_id_from_username(username)

            # Retrieve the list of followers and the list of people the client follows
            followers_dict = cl.user_followers(user_id)
            following_dict = cl.user_following(user_id)

    time.sleep(0.5)

    followers = list(followers_dict.keys())
    following = list(following_dict.keys())

    # Identify people you follow but they don't follow back
    non_followers = [user for user in following if user not in followers]

    # Print the name and username of non-followers
    print("People you follow but don't follow you back:")
    for nf in non_followers:
        full_name = dict(following_dict[nf])['full_name']
        username = dict(following_dict[nf])['username']

        print(f"\t- {full_name} ({username})")

# Core scan function
def core_scan(session_id:str, output:str='') -> None:
    """Performs a core scan and returns user's followers and following. If output=True, then saves the results to a file."""

    # Create an instagrapi Client
    with yaspin(text="Performing core scan..."):

        with suppress_output():
            cl = Client()

            # Login via SESSION ID
            cl.login_by_sessionid(session_id)

            # Retrieve the username (later to be used to get USER ID)
            client_username = dict(cl.account_info())['username']

            # Retrieve the USER ID
            user_id = cl.user_id_from_username(client_username)

            # Retrieve the list of followers and the list of people the client follows
            followers_dict = cl.user_followers(user_id)
            following_dict = cl.user_following(user_id)

    time.sleep(0.5)

    # Only keep the UIDs
    followers = list(followers_dict.keys())
    following = list(following_dict.keys())


    print(f"{'='*TERMINAL_WIDTH}\n"+f"CORE SCAN RESULTS for @{client_username}".center(TERMINAL_WIDTH)+f"\n{'='*TERMINAL_WIDTH}\n")
    print("/=========\\".center(TERMINAL_WIDTH) + "\n" + "|FOLLOWERS|".center(TERMINAL_WIDTH) + "\n" + "\\=========/".center(TERMINAL_WIDTH))

    # Store the usernames of followers
    fo_usernames = list()
    for fo in followers:
        username = dict(followers_dict[fo])['username']
        fo_usernames.append("@" + username)


    for i in range(0, len(fo_usernames), names_per_row):
        print("".join(f"{x:<{col_width}}" for x in fo_usernames[i:i+names_per_row]))

    print("/=========\\".center(TERMINAL_WIDTH) + "\n" + "|FOLLOWING|".center(TERMINAL_WIDTH) + "\n" + "\\=========/".center(TERMINAL_WIDTH))

    # Store the usernames of 'following' accounts
    fi_usernames = list()
    for fi in following:
        username = dict(following_dict[fi])['username']
        fi_usernames.append("@" + username)

    for i in range(0, len(fi_usernames), names_per_row):
        print("".join(f"{x:<{col_width}}" for x in fi_usernames[i:i+names_per_row]))

    print(f"{'='*TERMINAL_WIDTH}\n"+"END OF SCAN RESULTS".center(TERMINAL_WIDTH)+f"\n{'='*TERMINAL_WIDTH}\n")

    # If output=True, then output the results to a file
    if output:

        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        json_dict = {
            "timestamp": timestamp,
            "follower_count": len(fo_usernames),
            "following_count": len(fi_usernames),
            "followers": fo_usernames,
            "following": fi_usernames
        }

        # Check if the output directory exists. If not, create it.
        if not os.path.isdir(output):
            os.mkdir(output)
        
        # Write the scan results
        with open(f"{output}/Instadective-CS-{timestamp}.json", 'w') as f:
            json.dump(json_dict, f, indent=4)
            f.close()
        
        print(f"Scan results saved to '{output}/Instadective-CS-{timestamp}.json'.")

# Comparing scans
def comparison(scan1:str, scan2:str) -> None:
    """Compare two core scans to identify changes in followers and following."""

    if not (os.path.isfile(scan1) and os.path.isfile(scan2)):
        raise FileNotFoundError("One or more of the scan files don't exist!")
    
    scan1_results = json.load(open(scan1, 'r'))
    scan2_results = json.load(open(scan2, 'r'))

    scan1_time = scan1_results["timestamp"]
    scan2_time = scan2_results["timestamp"]

    fmt = "%Y-%m-%d-%H-%M-%S"

    s1_date = datetime.strptime(scan1_time, fmt)
    s2_date = datetime.strptime(scan2_time, fmt)

    diff = max(s1_date, s2_date) - min(s1_date, s2_date)
    days = diff.days
    seconds = diff.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    diff_string = f"{days} days, {hours} hours, {minutes} minutes, {secs} seconds"

    s1_followers = scan1_results["followers"]
    s2_followers = scan2_results["followers"]
    s1_following = scan1_results["following"]
    s2_following = scan2_results["following"]

    if min(s1_date, s2_date) == s1_date:
        followers_lost = [f for f in s1_followers if f not in s2_followers]
        followers_gained = [f for f in s2_followers if f not in s1_followers]
        unfollowed = [f for f in s1_following if f not in s2_following]
        followed = [f for f in s2_following if f not in s1_following]

    else:
        followers_lost = [f for f in s2_followers if f not in s1_followers]
        followers_gained = [f for f in s1_followers if f not in s2_followers]
        unfollowed = [f for f in s2_following if f not in s1_following]
        followed = [f for f in s1_following if f not in s2_following]

    print(f"{'='*TERMINAL_WIDTH}\n"+f"COMPARSION RESULTS".center(TERMINAL_WIDTH)+f"\n{'='*TERMINAL_WIDTH}\n")

    print("SUMMARY:\n")
    print(f"In {diff_string},")
    print(f"- You gained {len(followers_gained)} new followers")
    print(f"- You lost {len(followers_lost)} followers")
    print(f"- You followed {len(followed)} new accounts")
    print(f"- You unfollowed {len(unfollowed)} accounts")

    print("="*TERMINAL_WIDTH)
    print(("/"+ "="*16 + "\\").center(TERMINAL_WIDTH) + "\n" + "|FOLLOWERS GAINED|".center(TERMINAL_WIDTH) + "\n" + ("\\"+ "="*16 + "/").center(TERMINAL_WIDTH))

    for i in range(0, len(followers_gained), names_per_row):
        print("".join(f"{x:<{col_width}}" for x in followers_gained[i:i+names_per_row]))

    print("="*TERMINAL_WIDTH)
    print(("/"+ "="*14 + "\\").center(TERMINAL_WIDTH) + "\n" + "|FOLLOWERS LOST|".center(TERMINAL_WIDTH) + "\n" + ("\\"+ "="*14 + "/").center(TERMINAL_WIDTH))

    for i in range(0, len(followers_lost), names_per_row):
        print("".join(f"{x:<{col_width}}" for x in followers_lost[i:i+names_per_row]))

    print("="*TERMINAL_WIDTH)
    print(("/"+ "="*8 + "\\").center(TERMINAL_WIDTH) + "\n" + "|FOLLOWED|".center(TERMINAL_WIDTH) + "\n" + ("\\"+ "="*8 + "/").center(TERMINAL_WIDTH))

    for i in range(0, len(followed), names_per_row):
        print("".join(f"{x:<{col_width}}" for x in followed[i:i+names_per_row]))

    print("="*TERMINAL_WIDTH)
    print(("/"+ "="*10 + "\\").center(TERMINAL_WIDTH) + "\n" + "|UNFOLLOWED|".center(TERMINAL_WIDTH) + "\n" + ("\\"+ "="*10 + "/").center(TERMINAL_WIDTH))

    for i in range(0, len(unfollowed), names_per_row):
        print("".join(f"{x:<{col_width}}" for x in unfollowed[i:i+names_per_row]))
    
    print(f"{'='*TERMINAL_WIDTH}\n"+"END OF COMPARISON".center(TERMINAL_WIDTH)+f"\n{'='*TERMINAL_WIDTH}\n")