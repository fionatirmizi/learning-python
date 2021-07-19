print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.') 

poem = """
\tThe lovely world
with logic so firmly planted
cannot discen \n the needs of love
nor comprehend passion from inutiion
and requires an explanation
\n\t\twhere there is none
"""

print("-----------------")
print(poem)
print("-----------------")


five = 10-2 + 3 - 6
print("this should be five:%s" % five)

def secret_formula(started):
  jelly_beans = started * 500
  jars = jelly_beans/1000
  crates = jars / 100
  return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)  ##NOTICE THAT HERE WE DIDNT USE THE SAME VARIABLES AS IN THE FUNCTIONS.
#we used beans instead of jelly_beans. This is because in functions the variables used are independent and only temporary. 
#we can assign new vairables later to return the same values.
#i couldve written code like this too: name1, name2, name3  = secret_formula(start_point)   and it would return the same resultS!!

print("with a starting point of: %d" % start_point)
print("we'd have %d beans, %d jars, and %d crates."%(beans, jars, crates))

start_point = start_point / 10

print("we can also do that this way")
print("we'd have %d beans, %d jars, %d crates"% secret_formula(start_point))
#here we directly used the function instead of assigning values separately to invidual variables outside the function) 


