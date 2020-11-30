#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-

from main import CommandLineInterface as CLI
import argparse


def run(arg):
    my_cli = CLI(arg.letter)

    try:
        my_cli.cmdloop()

    except Exception as err:
        print("Please try again! The exception is: ", err)


def main():
    parser = argparse.ArgumentParser(description=
                                     "This is a program which can generate UML diagram from JS Source Codes")
    parser.add_argument("-name",
                        help="optional: when a user input a name, can  show the name in cmd.",
                        dest="letter",
                        type=str,
                        default=">")
    parser.set_defaults(func=run)
    arg = parser.parse_args()
    arg.func(arg)

if __name__ == '__main__':
    main()