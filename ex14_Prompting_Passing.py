#Prompting and Passing from book
#using argv and raw input together
from sys import argv
script, username = argv
prompt = '> '

print("Hi %s, I'm the %s script"%(username, script))
print("Do you like me %s?"%(username))

likes = input(prompt)
print("Where do you live?")

lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
#each time the program will pause to ask the user for an input using input(prompt)
#this is different from argv where you assign values in the beginning like script name and username! 
#argv doesnt need to stop the code from running, it takes the values given and keeps running
#input stops until you give it a value
print(""" Alright, so you said %r about liking me.
You live in %r.
And you have %r computer"""%(likes, lives, computer))


#note you dont need to use the word or variable "prompt"
#you can simply use input(). See below. Same results!! 

#Prompting and Passing from book
#using argv and raw input together
from sys import argv
script, username = argv


print("Hi %s, I'm the %s script"%(username, script))
print("Do you like me %s?"%(username))

likes = input()
print("Where do you live?")

lives = input()
print("What kind of computer do you have?")
computer = input()
#each time the program will pause to ask the user for an input using input(prompt)
#this is different from argv where you assign values in the beginning like script name and username! 
#argv doesnt need to stop the code from running, it takes the values given and keeps running
#input stops until you give it a value
print(""" Alright, so you said %r about liking me.
You live in %r.
And you have %r computer"""%(likes, lives, computer))

