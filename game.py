from sys import exit,argv
script, name = argv
print("Hello %s,let's play game" % name)


def gold_room():
    print("""Congratulations to last room
             This room is full of dollars
             How much do you want to take
             """)
    much = input("> ")
    if much.isdigit():
        money = int(much)
    else:
        print("Only enter numbers")

    if money < 1000:
        print("you win!")
        exit(0)
    else:
        gameover("You're greedy")


def Sphinx():
    print("""A Sphinx stuck in the road ahead
             Please answer the riddle
             What is the creature that walks on four legs in the morning
             two legs at noon and three in the evening?""")
    riddle = input("> ").lower()

    if "man" == riddle:
        print("Congratulations, let's go to the next room")
        gold_room()
    else:
        print("you are worng")
        gameover()


def left_room():
    print("""welcome,In front of a river
        How you want to cross the river
        swim or Looking for a boat?""")
    choose = input("> ").lower()

    if "boat" == choose:
        print("You thrilling escape the river monster")
        Sphinx()
    elif "swim" == choose:
        gameover("River monsters")
    else:
        print("Only two ways")
        exit(0)


def right_room():
    print("""In front of a prairie
        You are willing to pay all cash quickly passed?
        yes or no？""")
    choose = input("> ").lower()

    if "yes" == choose:
        print("you are very smart，arrived safely")
        Sphinx()
    elif "no" == choose:
        gameover("You're too stingy,Monster hit")
    else:
        print("Yes or No")


def middle_room():
    print("""In front of a mountain
        Do you want to go through it？
        Yes or No？""")
    choose = input("> ").lower()

    if "yes" == choose:
        print("Unfortunately you")
        gameover("get lost")
    elif "no" == choose:
        print("You too timid")
        gameover("Monster")


def gameover(why):
    print(why, "This is fun, good job")
    exit(0)


def start():
    print(" There are three doors in front of you, please select (left, middle, right)")
    doors = input("> ").lower()

    if "left" in doors and len(doors) <= 6:
        print("Let's go")
        left_room()

    elif "middle" in doors and len(doors) <= 6:
        print("Let's go")
        middle_room()

    elif "right" in doors and len(doors) <= 6:
        print("Let's go")
        right_room()

    else:
        print("Please follow the prompts to enter")
        start()

start()
