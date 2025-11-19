# Creating command line utility in python:
# A command line utility is a program that is designed to be run from the command line interface (CLI) of an operating system. It allows users to perform specific tasks or operations by entering commands and arguments in a terminal or command prompt.

import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple greeting CLI tool")

    parser.add_argument("name", help="Enter your name")
    parser.add_argument("-u", "--uppercase", action="store_true",
                        help="Show the name in uppercase")

    args = parser.parse_args()

    if args.uppercase:
        print(f"HELLO {args.name.upper()}!")
    else:
        print(f"Hello {args.name}")

if __name__ == "__main__":
    main()
