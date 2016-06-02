import os
import sys


def readfile(filename):
    with open(filename, 'r') as f:
        file = f.read()
        print(file)


def chekfile(filename):
    if not os.path.isfile(filename):
        print("The file is does not exits")
        sys.exit(0)
    elif not os.access(filename, os.R_OK):
        print("access denied")
        sys.exit(0)
    else:
        readfile(filename)


def main():
    if len(sys.argv) == 1:
        filename = input("Enter your filename: ")
        chekfile(filename)
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        print(os.path.abspath(filename))
        chekfile(filename)

if __name__ == "__main__":
    main()
