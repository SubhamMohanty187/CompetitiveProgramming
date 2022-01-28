#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    left=0;right=0;up=0;down=0
    leftup=0;leftdown=0;rightup=0;rightdown=0 # For diagonal path
    
    right = n - c_q
    left = c_q - 1
    up = n - r_q
    down = r_q - 1
    
    if left < up:     # For left diagonal
        leftup = left
    else:
        leftup = up
        
    if left < down:
        leftdown = left
    else:
        leftdown = down
        
    if right < up:       # For right diagonal
        rightup = right
    else:
        rightup = up
        
    if right < down:
        rightdown = right
    else:
        rightdown = down
        
    for i in range(k):
        ro = obstacles[i][0]
        co = obstacles[i][1]
        
        if r_q == ro and c_q > co:
            if c_q - co - 1 < left:
                left = c_q - co - 1
        elif r_q == ro and c_q < co:
            if co - c_q - 1 < right:
                right = co - c_q - 1
        elif c_q == co and r_q < ro:
            if ro - r_q - 1 < up:
                up = ro -r_q -1
        elif c_q == co and r_q > ro:
            if r_q - ro - 1 < down:   
                down = r_q -ro - 1
                
        elif co < c_q and ro > r_q:
            if (c_q - co) == (ro - r_q):
                if ro - r_q - 1 < leftup:
                    leftup = ro - r_q -1
        elif co < c_q and ro < r_q:
            if (c_q - co) == (r_q - ro):
                if c_q - co - 1 < leftdown:
                    leftdown = c_q -co -1
        elif co > c_q and ro > r_q:
            if (co - c_q) == (ro - r_q):
                if ro - r_q - 1 <rightup:
                    rightup = ro - r_q - 1
        elif co > c_q and ro < r_q:
            if (co - c_q) == (r_q - ro):
                if co - c_q - 1 < rightdown:
                    rightdown = co - c_q - 1
    
    return left + right + up + down + leftup + leftdown + rightup + rightdown

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
