#!/bin/python3
def nextMove(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")
        return
    else:
        for i in range(0,5):
            for j in range(0,5):
                if board[i][j] == 'd':
                    if posr-i > 0:
                        print("UP");
                    elif posc-j > 0:
                        print("LEFT")
                    elif posr-i < 0:
                        print("DOWN")
                    else:
                        print("RIGHT")
                    return

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
