#!/usr/bin/python
import math
# Head ends here
def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")
        return
    else:
        mdist = 0;
        shortest = 25;
        for i in range(0,5):
            for j in range(0,5):
                if board[i][j] == 'd':
                    mdist = abs(posr-i) + abs(posc-j) # manhattan distance
                    if mdist < shortest:
                        shortest = mdist
                        p1 = i
                        p2 = j
        if posr-p1 > 0:
            print("UP");
        elif posc-p2 > 0:
            print("LEFT")
        elif posr-p1 < 0:
            print("DOWN")
        else:
            print("RIGHT")
        return

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
