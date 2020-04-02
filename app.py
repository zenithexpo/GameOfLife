"""
@author: Diksha Verma
"""

from gameoflife import Life
import numpy as np
l = Life()
patterns = l.lstPatterns()

print("_______________________________________________________________________________")
print("-------------------W E L C O M E To The Game Of Life---------------------------")
print("_______________________________________________________________________________")
print("==M E N U==")
print("1.View list of available patterns")
print("2.Show the board of pattern name")
print("3.Enter pattern name to start the game")
print("4.exit - to exit from game")

def lst():
    for k in patterns.keys():
        print(k)

def view_pattern(pat):
    if pat not in patterns:
        print("Invalid pattern_name")
    else:
        print(np.array(patterns[pat], dtype=np.uint8))

def iterations(n):
    for i in range(int(n)):
        print("\n>>{}:".format(i+1))
        l.applyRule()
        print(l.get_board())

def select_pattern(pat):
    if not l.select(pat):
        print("No pattern called {} exists!".format(pat))
    else:
    	n=input("Enter number of iterations\n")
    	iterations(n)

while True:
    choice = input("Your Choice (1-4)?\n")

    if choice == "1":
    	lst()
    elif choice == "2":
    	pat=input("Enter pattern name\n")
    	view_pattern(pat)
    elif choice == "3":
    	pat=input("Enter board pattern\n")
    	select_pattern(pat)
    elif choice == "4":
    	exit()
    else:
    	print("Invalid input\n")
