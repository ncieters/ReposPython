import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.
max=0
itmax=0

# game loop
while True:
    for i in range(8):
        print("iteration " + str(i))
        mountain_h = int(input())  # represents the height of one mountain.
        if mountain_h>=0 and mountain_h<=9 and mountain_h>max:
            max = mountain_h
            itmax=i
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # The index of the mountain to fire on.
    #print("la montagne la plus haute est :" + str(max))
    print(str(itmax))