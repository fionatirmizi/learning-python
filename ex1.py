print('Hello, world!')
print('Hello Fiona!')
# This is a comment. Lesson 1. 
mybirthday = "3rd july"
name = "Fiona"
print(name+"'s birthday is on "+ mybirthday)
dog = "Newton"
sentence = name + "'s dog is " + dog
print(sentence)


a = 5
b = 10
print( a + b)
print(5 + 10)
print('fiona', 'fiona')
name = "fiona"
print(name * 5)
# making more efficient
print('fiona '  * 5)
count = 10
# printing name multiple times, can edit name or count later
print( name , count)
print( (name + " ")  * count)



# Conditional statements
# comparing two values, greater than, lesser than , equal to 
if(24<5):
  print("lesser than")
# a = 24 
# b = 5
a = 5 # lesser than test
b = 24
string1 = str(a)
string2 = str(b)

if(a > b):
  print(string1 + ' is greater than ' +  string2)
if(a == b):
  print(string1 + " is equal to " + string2)
if(a < b):
  print(string1 + " is lesser than " + string2)
  
  
  my_name = 'Fiona'
dog = 'Newton'
age = 25
height = 155
hair_color = 'brown'

print( 'My name is ' + my_name)
# defining %s to insert strings
print( 'My name is %s'%(my_name))
print("My name is %s and my dog's name is %s"%(my_name,dog))
# defining %d to insert numbers (age = 25)
print("My age is %d and my hair color is %s"%(age,hair_color))
