import os
from sys import argv


def pid(name):
    command = 'ps -e | grep %s' % name
    pid_txt = os.popen(command).readlines()
    if len(pid_txt) == 0:
        print("None")
        return
    else:
        for line in pid_txt:
            colum = line.split()
            pid = colum[0]
            command = "kill -9 %d" % int(pid)
            rc = os.system(command)
            if rc == 0:
                print("Success! kill %s" % name)
            else:
                print("Faled! kill %s" % name)
    return


if __name__ == "__main__":
    if len(argv) == 1:
        name = raw_input("Enter process name: ")
    else:
        name = argv[1]
    pid(name)
