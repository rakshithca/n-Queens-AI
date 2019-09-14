import sys
import time
import random
import copy

start_time = time.time()
BOARD_SIZE = 8
MAX_STEPS = 50
TRAILS = 10


def under_attack(col, queens):
    return col in queens or \
           any(abs(col - x) == len(queens)-i for i,x in enumerate(queens))

def conflicts(completeAssignment,m,n):
 x = completeAssignment[m]
 y = completeAssignment[n]
 if (x == y) or (abs(m-n) == abs(x-y)):
  return 1
 else:
  return 0

def CurrentConflicts(completeAssignment,var,n):
 numOfConflicts = 0
 for i in range(n):
  if i == var:
   continue
  if conflicts(completeAssignment,i,var):
   numOfConflicts += 1
 return numOfConflicts

def IsConsistentAssignment(completeAssignment,n):
 numOfConflicts = 0
 for i in range(n):
  for j in range(n):
   if i == j:
    continue
   if conflicts(completeAssignment,i,j):
    return 0
 return 1

def FindMinConflicts(completeAssignment,var,currentConflicts,n):
 value = completeAssignment[var]
 newConflicts = 0
 for i in range(n):
  changedAssignment = copy.copy(completeAssignment)
  if i == changedAssignment[var]:
   continue
  changedAssignment[var] = i;
  newConflicts = CurrentConflicts(changedAssignment,var,n)
  if newConflicts < currentConflicts:
   value = i
 return value

def MIN_CONFLICTS(n,max_steps):
 solution = random.sample(xrange(0,n), n)
 
 print '\nInitial random assignment :',solution

 for i in range(max_steps):
  if IsConsistentAssignment(solution,n):
   print '\nA consistent Assignment found! Steps taken to find the solution = {0}'.format(i - 1)
   return solution
  randomlyChosenVariable = random.choice(range(n))
  conflicts = CurrentConflicts(solution,randomlyChosenVariable,n)
  if conflicts > 0:
   value = FindMinConflicts(solution,randomlyChosenVariable,conflicts,n)
   solution[randomlyChosenVariable] = value
  if i == max_steps - 1:
   print '\nCould not find a solution in specified number of steps'
   return []
 
def print_board(queens):
    row = 0
    n = len(queens)
    for pos in queens:
        for i in range(pos):
            sys.stdout.write( ". ")
        sys.stdout.write( "Q ")
        for i in range((n-pos)-1):
            sys.stdout.write( ". ")
        print

listOfAllAssignmenst = []
for i in range(TRAILS):
 print '\nTrial number :',i
 start_time = time.time() 
 ans = MIN_CONFLICTS(BOARD_SIZE,MAX_STEPS)
 print '\nTime taken : ',(time.time() - start_time)
 if ans:
  print '\nConsistent Assignment : {0}\n'.format(ans)
  print
  print_board(ans)
  break
 else:
  print '\nSorry, could not find a consistent assignment in {0} steps'.format(MAX_STEPS)
  print