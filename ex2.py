#using formatter)
formatter = "%r %r %r %r"
print (formatter % (1, 2, 3, 4))
print (formatter % ('''My name is Fiona''', '''I have a dog''',
'His name is Newton', 'We are a family'))
# you cant use \n for new line with %r. since this is raw data. 
#can use %s for strings -- it will give new lines with \n 
formatter2 = '%s %s %s %s'
print (formatter2 % ('I am on a mission\n', 'To become a good coder\n',
'it could take a while\n', 'but i will be consistent.'))


# Using more escape sequences
#using " to show inches, but not wanting to end the string! 
print ("I am 5'2\" tall")

#ex10 from book
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
# starts on a new line every line because I used """ , and didnt need 
#didnt need \n on every line 
fat_cat = """
I'll do a list:
\t* cat food 
\t* fishies
\t* catnip\n\t* grass """
print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)
