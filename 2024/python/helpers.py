"""
various helper functions meant to be imported
"""

from os import environ
from os.path import isfile

import requests
from dotenv import load_dotenv


# load the .env file
load_dotenv()


def get_input(year: int, day_num: int) -> str:
    """get the input for the day number"""
    filename = f"input/day{day_num}"
    # check if the file exists, if it does, read it and return the list
    if isfile(filename):
        with open(filename, encoding="utf-8") as inputfile:
            return inputfile.read()

    # if the file doesn't exist, load it from the site and then save it to a file
    else:
        headers = {"Cookie": f"session={environ.get('COOKIE', '')}"}
        fetch_input = requests.get(
            f"https://adventofcode.com/{year}/day/{day_num}/input",
            headers=headers,
            timeout=10,
        )

        with open(filename, "w", encoding="utf-8") as inputfile:
            inputfile.write(fetch_input.text)

        return fetch_input.text
