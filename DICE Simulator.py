import random

print("\n      WELCOME GUYS\n")
print(" This is a DICE Stimulator\n")
print("(You Can Use It For Ur Board Games. For Rolling It U Just Have To Press y)\n")

x = "y"

while x == "y":
    number = random.randint(1,6)

    if number == 1:
        print("\n----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------\n")
    if number == 2:
        print("\n----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------\n")
    if number == 3:
        print("\n----------")
        print("|      O |")
        print("|    O   |")
        print("| O      |")
        print("----------\n")
    if number == 4:
        print("\n----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------\n")
    if number == 5:
        print("\n----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------\n")
    if number == 6:
        print("\n----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------\n")
    x = input("PRESS y to Roll Again\n")
    
    



















    
