# -*- coding: GB18030 -*-
import os
import sys
import subprocess


def readfile(filename):
    with open(filename, 'r') as f:
        file = f.read()
        print(file)


def chekfile(filename):
    if not os.access(filename, os.R_OK):
        print("access denied")
        sys.exit(0)
    else:
        try:
            readfile(filename)
        except UnicodeDecodeError:
            with open(filename, 'rt', encoding='gb18030') as f:
                file = f.read()
                print(file)


def find(file):
    cmd = 'find / -name %s 2>/dev/null' % file
    h = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    h.wait()
    g = h.communicate().__str__()
    myfile = open('test.txt', 'w+')
    myfile.write(g)
    myfile.seek(0)
    f = myfile.readlines()
    myfile.close()
    print(f)
    file = input('Please choose you file path:  ')
    chekfile(file)


def path(filename):
    if os.path.isfile(filename):
        chekfile(filename)
    else:
        find(filename)


def main():
    if len(sys.argv) == 1:
        filename = input("Enter your filename: ")
        path(filename)
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        print(os.path.dirname(filename))
        path(filename)

if __name__ == "__main__":
    main()
