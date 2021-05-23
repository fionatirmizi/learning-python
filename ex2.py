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
