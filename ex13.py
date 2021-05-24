from sys import argv
#this is an ïmport" that add functions to Python
# The function constitutes of a Module or library
# argv is the argument variable that holds variables that u send or pass to Python
script, first, second, third = argv
print ("number 1:", script)
print ("number 2:", first)
print ("number 3:", second)
print ("number 4:", third)
# note that your code here will not run directly in console. need to run in shell
#you will need to type: python main.py cat dog bird in the shell to run it and assign the script and other 3 variables
# line 5 unpacks argv so that it gets assined to four variables instead of holding the arguments


