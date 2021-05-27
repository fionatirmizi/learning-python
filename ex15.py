import sys
script = sys.argv[0]
filename = sys.argv[1]
output = sys.argv[2]
#testing this code works
#print(script, filename)
#opening the file
txt = open(filename)
print("Here's your file %r:"%filename)
#assigned a variable to the contents of this file and printed it
var1 = txt.read()
print(var1)

#replace the word "file" in above textfile with "doggie"
print(var1.replace('file','doggie'))
# I want to open Outputfile and write the text from Testfile to Output file
#added a third argument called "output"
replaced_word = var1.replace('file','doggie')
#opening file named Outputfile in write-mode
#txt_2 = open(output,'w')
#writing to the file Outputfile
#Appending a file, to add new lines, without overwriting with write mode
txt_2 = open(output,'a')
txt_2.write("Adding a new line\n")
