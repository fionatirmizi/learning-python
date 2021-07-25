#EX15 - Reading Files 
from sys import argv
script, filename = argv
#we open the file in Line 5
txt = open(filename)
print("Here's your file %r:"%(filename))
#we tell the function to read the text in the file and print it
print (txt.read())

#we ask user for the next file name?
print("type the file name again:")
file_again = input()

#we open the new text file
txt_again = open(file_again)
# we now read this new text file, and print whatever is it in
print(txt_again.read())


#can also remove the input(), and simply add 3rd argument called "file_again" in Line 3
#when you run it then, you will add the name of the second textfile 
# it will look like this when u want to run --> python ex15b.py File1 File2 
