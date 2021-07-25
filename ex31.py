print("You enter a dark room with two doors. Do you go through door 1 or door 2?")

door = input(">")

if door == "1":
  print("There's a giant bear here eating a cheesecake. What do you do?")
  print("1. Take the cake.")
  print("2. Scream at the bear.")

  bear = input(">")

  if bear == "1": 
    print("The bear eats your face off. Good job")
  elif bear == "2":
    print("the beat eats your legs off. Good job!")
  else: 
   print("Well, doing %s is probably better. Bear runs away"% bear)

#we wrote if statements within an IF statement, to make a series of decicisions based on users input

#below is what happens if user selects door 2
elif door == "2":
  print("You stare into the endless abyss")
  print("1. Blueberries\n2. Yellow jacket clothespin\n3. Understanding revolvers yelling melodies")

  insanity = input(">")

  if insanity == '1' or insanity == '2':
    print("Your body survives powdered by a mind of jello. Good job")
  else: 
    print("Insanity rots your eyes into a pool of muck")


#below is what happens if user selects anything other than 1 or 2
else: 
  print("You stumble around and fall on a knife and die!")
