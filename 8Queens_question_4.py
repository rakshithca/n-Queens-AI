#solving N-queens using min-conflicts local search.

import sys
import random
import time

#global variable decleration
starting_time = time.time()

#Inputting the number of queens by defining the board size

def BOARD_SIZE(n):
   print_board(minimum_conflicts(list(range(n)), n))

#----------Printing the solution
   
def print_board(ans):
    n = len(ans)
    for pos in ans:
        for i in range(pos):
            sys.stdout.write( ". ")
        sys.stdout.write( "Q ")
        for i in range((n-pos)-1):
            sys.stdout.write( ". ")

        print

#---------Selecting the value for minimum conflicts 
def row_location(x):
    return x>0

def col_location(x,X):
    return x == min(X)

def minimum_conflicts(ans, n):
   def random_pos(x, y, verticle):
     if(verticle):
         return random.choice([i for i in range(n) if y(x[i],x)])
     else:
         return random.choice([i for i in range(n) if y(x[i])])
     
        
#conflicted variables
   for k in range(10000):
      Placements = solution(ans, n)
      if sum(Placements) == 0:
         print(ans)
         global starting_time
         print((time.time() - starting_time))
         return ans
      column =random_pos(Placements, row_location, 0)
      New_Placements = [total(ans, n, column, row) for row in range(n)]
      ans[column] = random_pos(New_Placements , col_location, 1)

#choosing minConflicts value
def solution(ans, n):
    return [total(ans, n, column, ans[column]) for column in range(n)]

def total(ans, n, column, row):
   total = 0
   for i in range(n):
      if i == column:
         continue
      if ans[i] == row or abs(i - column) == abs(ans[i] - row):
         total += 1
   return total

# Number of queens is being passed.

BOARD_SIZE(8)

