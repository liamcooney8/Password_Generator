"""Provides the password generator CLI."""
# cli.py

from .password_generator import *


def main():
    print("\nHello, enter your info and I'll make you a password!")
    while True:
        check_length()
        exit_loop()
