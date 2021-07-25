#think: the variables in your functions, are not related to the variables in your script !! 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print("You have %d cheeses!"% cheese_count)
  print("You have %d boxes of crackers!"% boxes_of_crackers)
  print("Man that's enough for a party!")

#the printing takes place after the print statement lying outside the entire funciton
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)
#above the function is called or run when you simply type the function name with arguments inside


print("OR we can use variables for our script:")
amountofcheese = 10
amountofcrackers = 50
cheese_and_crackers(amountofcheese, amountofcrackers)

print("we can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print("and we can combine the too! varibales and math")
cheese_and_crackers(amountofcheese + 100, amountofcrackers + 1000)


###SOME MORE PRACTICE

#Returning values in a Function
def testfunc(num1, num2):
  return num1, num2

a, b = testfunc(5, 10)
print("returned from function:", a, ",", b)
print("----------------")

#Required Arguments
def division(first, second):
  value = first/second
  return value

#calling the function
output = division(10,2)
print("Output of your function is:", output)
print("----------------")

#Keyword Arguments

output = division(first=10, second=2)
print("the output is", output)
print("----------------")

#Default Arguments

#setting second argument as a default = 2
def division(first, second=2):
  value = first/second
  return value

output = division(10)
print("output with default divisor as 2 is:" , output)

#Variable number of arguments
def addition(*args):
  total = 0           #define a new varialbe with value = 0
  print(type(args))
  for i in args:
    total += i    #perform total
  return total  ##returns the total outside for loop, but inside the function

## calling the function
output = addition(10,14,15,1)   ##passing multiple arguments
print("Output of our function is:", output)
