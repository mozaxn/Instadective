# Imports
from instagrapi import Client
from pyfiglet import Figlet
import shutil
from yaspin import yaspin
import time
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
VERSION = "0.1.0"

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
    with yaspin(text="Processing..."):

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