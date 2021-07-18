from sys import argv
script, input_file = argv
#in REPL the inputfile is called 'ex20_input'

#here we first assign a function called print_all with argument f
def print_all(f):   ##f here is the file , as you will see we assign later
  print(f.read())  ##reading the argument here, which is actually file

def rewind(f):  ##rewind to the beginning of the file using seek(0), the 0 means position 0 , beginning of file. the very first byte.
  f.seek(0)


##second funcition is defined, where it will print the line count which we later assign when we create variable current_line, 
## and beside that f.readline will read the line in the second argument, which is actually assigned as current_file (our input file)
def print_a_line(line_count, f):
  print(line_count, f.readline()),

currentfile = open(input_file)

print("First let's print the whole file:\n")

print_all(currentfile)

print("now lets rewind, kind of like a tape")

rewind(currentfile)


print("lets print three lines:")

currentline = 1
print_a_line(currentline, currentfile),

currentline +=1
print_a_line(currentline, currentfile),

currentline = currentline + 1
print_a_line(currentline, currentfile),


##above can also be written as:
##currentline += 1
