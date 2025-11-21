# Creating command line utility in python:

# A command line utility is a program that is designed to be run from the command line interface (CLI) of an operating system. It allows users to perform specific tasks or operations by entering commands and arguments in a terminal or command prompt.
# A command-line utility in Python is simply a Python script that you can run from the terminal using commands—just like git, pip, or ls.
# You can build one easily using argparse, click, or typer.

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

# Run this command in terminal to download any image from the internet:
# curl https://www.sexyloops.com/movies/background.jpg --output shubh.jpg

import argparse
import requests

def download_file(url,local_filename):
    
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename


parser = argparse.ArgumentParser()
# Add comand line arguments 
parser.add_argument("Url", help = "Url of the fole to download ")
parser.add_argument("output", help = "Bu which name do you want to save your file ")

args = parser.parse_args()

print(args.Url)
print(args.output) 
download_file(args.Url,args.output)
