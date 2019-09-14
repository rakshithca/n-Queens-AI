import sys
import copy
import time

start_time = time.time()
BOARD_SIZE = 15

values = []

def updatePossibleValues(queens,n):
 global values 
 values = []
 for i in range(BOARD_SIZE):
  values.append(range(BOARD_SIZE))
 for k,x in enumerate(queens):
  for i in range(n):
   if k == i:
    values[i] = [x]
   else:
    if x in values[i]:
     values[i].remove(x)

def putArcs(dependencies,i,n):
 #print 'Inside putArcs : ',i , n
 for k in range((i+1),n):
  dependencies.append([i,k])
  '''
  j = (n - 1)
  while j >= i:
   if j == k:
    j -= 1
    continue
   dependencies.append([k,j])
   j -= 1
   '''

def under_attack(col, queens):
    #print 'Inside under_attack',col,queens
    return col in queens or \
           any(abs(col - x) == len(queens)-i for i,x in enumerate(queens))

def checkArcConsistency(n,local_dependencies,queens,value):
 #print 'Inside checkArcConsistency. Inputs : n = {0}, local_dependencies = {1} '.format(n,local_dependencies)
 while local_dependencies:
  arctoVerify = local_dependencies.pop(0) # take the first arc on the list
  if arctoVerify:
   i = arctoVerify.pop(0)
   j = arctoVerify.pop(0)
  else:
   return 1 # no arcs
  if RemoveInconsistentValues(queens+[value],i,j):
   #print 'local_dependencies before adding',local_dependencies
   for k in range((len(queens) + 1), n):
    if not ((k == i) or [k,i] in local_dependencies):
     local_dependencies.append([k,i])
     #print 'adding arc ({0},{1})'.format(k,i)
  #print 'constraints before returning : ',constraints 
  for temp_list in values:
   for j in temp_list:
    if j == -1:
     listIndex = temp_list.index(j)
     temp_list.remove(j)
  print 'Cleaned ',values
  for i in range(n):
   if not values[i]:
    #print 'No possible positions for ',i
    return 0
 return 1

def IsConsistentWithAssignedQueens(queens,col,value):
 for row,position in enumerate(queens):
  print row,position,col,value
  if (position == value) or (abs(col - row) == abs(value - position)):
   print 'Returning 0'
   return 0
 return 1

def RemoveInconsistentValues(queens,i,j):
 print 'Inside RemoveInconsistentValues. Inputs i = {0}, j = {1}, queens = {2}'.format(i,j,queens)
 removed = 0
 absValue = abs(i-j)
 print 'Possible values for {0} : {1}'.format(i,values[i])
 print 'Possible values for {0} : {1}'.format(j,values[j])
 for x in values[i]:
  print 'x = ',x
  if under_attack(x,queens):
   print 'removing {0} from {1}'.format(x,i)
   listIndex = values[i].index(x)
   values[i][listIndex] = -1
   continue
  flag = 1
  for y in values[j]:
   print 'Y = ',y
   if not IsConsistentWithAssignedQueens(queens,j,y):
    print 'removing {0} from {1}'.format(y,j)
    listIndex = values[j].index(y)
    values[j][listIndex] = -1
    continue
   if (x != y) and (abs(x-y) != absValue) : #there is a consistent value for the arc. i.e, positins of queens are not in same row
    flag = 0
    break #found a consistent pair(x,y) for this iteration, so contine continue checking for other values x
  if flag: #did not find a consistent value y for x
   values[i].remove(x)
   removed  = 1
   break
 #print 'removed = ',removed
 #print 'values : ',values 
 return removed

def rsolve(queens,n):
	global arguments
	#print 'Entered rsolve : ',n,queens
	if n == len(queens):
		#print(queens)
        	return queens
	else:
        	for i in range(n):
			if not under_attack(i,queens):
				for j in range(n):
                                 if i in values[j]:
                                  values[j].remove(i)
				values[len(queens)] = [i]
                                #print 'Possible values inside rsolve : ',values
				constraints = []
				print 'before putArcs'
				putArcs(constraints,len(queens + [i]),n)
				print constraints
				if not checkArcConsistency(n,constraints,queens,i):
				 #print 'detected Inconsistency'
				 updatePossibleValues(queens,n)
				 continue
				#print 'Possible values inside rsolve : ',values 
				#print queens+[i]
				arguments.append(queens+[i])
                		newqueens = rsolve(queens+[i],n)
				#print 'Printing newqueens ', newqueens
				updatePossibleValues(queens,n)
                		if newqueens != []:
                    			return newqueens
			else:
				#print values
				if i in values[len(queens)]:
                        	 values[len(queens)].remove(i)
				#print values 
        	return [] # FAIL

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

arguments = []
#constraints = []
#putArcs(constraints,BOARD_SIZE)
updatePossibleValues([],0)
#print 'Arcs stating the constraints : ',constraints
ans = rsolve([],BOARD_SIZE)
#print 'Answer = ',ans
print_board(ans)
print("Total number of assignments tried before arriving to the solutions are : {0}".format(len(arguments)))
print("Below are all the assignments tried :")
for listIndex in arguments:
	print(listIndex)

print '----%s----', (time.time() - start_time)