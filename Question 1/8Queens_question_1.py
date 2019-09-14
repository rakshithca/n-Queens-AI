#To count the total number of assignments attempted during a solution 

import sys
import time

start_time = time.time()
BOARDSIZE = 15

assignments = 0
 
def under_attack(column, queens):
    return column in queens or \
           any(abs(column - x) == len(queens)-i for i,x in enumerate(queens))

def rsolve(queens,x):
    global assignments
    global start_time
    if x == len(queens):
        #print(queens)
        print("Total Number of assignments: ",assignments)
        print((time.time() - start_time)* 1000)
        return queens

    else:
        for i in range(x):
            attack = under_attack(i,queens)
            #print(attack)
            if not attack:
                assignments = assignments + 1
                #print(assignments)

                newqueens = rsolve(queens+[i],x)
                if newqueens != []:

                    return newqueens
        return [] # FAIL



def print_board(queens):
    row = 0
    x = len(queens)
    for pos in queens:
        for i in range(pos):
            sys.stdout.write( ". ")
        sys.stdout.write( "Q ")
        for i in range((x-pos)-1):
            sys.stdout.write( ". ")
        sys.stdout.write("\n ")
        print


ans = rsolve([],BOARDSIZE)
print_board(ans)

