from sys import argv

script, filename = argv
print("We're going to erase %r"%(filename))
print("If you don't want that, hit CTRL-C (^C)") 
print("If you don't want that, hit RETURN. ")

input("?")

print("Opening the file now...")
target = open(filename, 'w')

#deleting whatever is in the files
print("truncating the file.. see ya!!")
target.truncate()

print("Now I'm going to ask you three lines, ok?")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

#writing the input from user into these files!
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And now we close the file...")
target.close()

------------------------------------
#I couldve just written all three lines in one go:

target.writelines([line1,"\n",line2,"\n",line3])

Look at Samplefile_ex16 in REPL --> textfile for output
--------------------------------

I could also write the lines like this:


target.writelines(""" %r
%r
%r""" % (line1, line2, line3))
------------------------------------------
