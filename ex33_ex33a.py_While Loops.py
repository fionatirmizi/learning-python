i = 0
numbers = []

while i < 6:
  print("At the top i is %d" % i)
  numbers.append(i)

  i += 1
  print("Numbers now: ", numbers)
  print("At the bottom i is %d" % i)

print("The numbers: ", numbers)

for num in numbers:
  print(num)
  
  
#STUDY DRILL - convert it to a function and assign values from a vairable:
#-----------------------------------------------------------------------------
 
ex33a.py:
 
numbers = []
def alpha(x):
  i = 0
  while i < x:
    print("At the top i is %d" % i)
    numbers.append(i)

    i +=1
    print("At the bottom i is %d" % i)
    print("The numbers are: ", numbers)

alpha(8)
for num in numbers:
  print(num)
  
#----------------------------------------------------------------------
#STUDY DRILL - add in another variable, so you can change the amount of increments as wekk

numbers = []
def alpha(x,y):    #----->>>>>>>>>>>>>>>>>>>>> added another variable, to be referenced for increments i += y
  i = 0
  while i < x:
    print("At the top i is %d" % i)
    numbers.append(i)

    i +=y                       #-------------->  here, added another variable y for increment
    print("At the bottom i is %d" % i)
    print("The numbers are: ", numbers)

alpha(8,2)                     #----> calling out with two values assigned to those x,y vairables
for num in numbers:
  print(num)
#--------------------------------------------------------------------------------
#STUDY DRILL - do it using FOR loops and range


numbers = []
i = 0
def alpha(x,y):
  for i in range(0,x,3):
    print("At the top i is %d" % i)
    numbers.append(i)
    print(numbers)

alpha(12,3)
