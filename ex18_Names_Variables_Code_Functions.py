#this one is like your scripts with argv
def print2(*args):
  arg1, arg2 = args
  print("arg1: %r, arg2: %r"%(arg1,arg2))

#ok, that *args is actually not needed, we can just do this
def print2_again(arg1, arg2):
  print("arg1: %r, arg2: %r"%(arg1,arg2))

#this just taked onr argument
def print1(arg1):
  print("arg1: %r" %(arg1)) 

#this one takes no arguments
def print_none():
  print("I got nothing")

print2("Fiona", "Tirmizi")
print2_again("Fiona", "Tirmizi")
print1("Newton")
print_none()


#fucntions define what you can do, they are like mini-scripts
