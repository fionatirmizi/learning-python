def add(a, b):
  print("Adding %d + %d"%(a,b))
  return a + b

def subtract(a, b):
  print("Subtracting %d - %d" %(a, b))
  return a-b

def multiply(a, b):
  print("multiplying %d * %d" %(a, b))
  return a * b

def divide(a, b):
  print("divinding %d * %d" %(a, b))
  return a / b

print("lets do some math with just functions")

#in below functions it runs whatever is inside the function, thus returning vales of the fucntion performed tooo
age = add(30,5)
height = subtract(78,4)
weight = multiply(20,5)
iq = divide(100,2)

print("Age: %d, height: %d, weight: %d, iq: %d" % (age, height, weight, iq))

#A puzzle for extra credit
what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print(" that becomes:", what, "Can you do it by hand?")
#do the extra puzzle by hand to check the value. is it the same? should be -2391.0 

