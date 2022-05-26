"""
    Short Error Libary
"""

import sys

from termcolor import colored


def noinput(self) -> None:
    """
    The user has not provided any arguments.
    """
    print(colored("The user has not made an entry. Please check your input.", "red"))
    sys.exit(-1)


def commandlist(self) -> None:
    """
    The user gets a list of commands.
    """
    print("List of commands")
    sys.exit(-1)


def neednoargs(self) -> None:
    """
    The Command does not need arguments.
    """
    print(colored("The Command does not need arguments.", "red"))
    sys.exit(-1)


def commandnotfound(self) -> None:
    """
    The command was not found.
    """
    print(colored("The command was not found.", "red"))
    sys.exit(-1)
