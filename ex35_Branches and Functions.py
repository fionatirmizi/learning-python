from sys import exit

def gold_room():
  print("this room is full of gold. HOw much do you take?")

  next = input("> ")
  if "0" in next or "1" in next: ###this only lets you enter numbers with 0 or 1 in them. what if I want to enter the number 22 or 35? 
    how_much = int(next)  #converts a number you entered into an integer.  we assign the string as an integer to a variable. 

  else: 
    dead("Man, learn to type a number.")

  if how_much < 50:
    print("Nice, you got greedy, you win!")
    exit(0)
  else:
    dead("You greedy bastard!")

def bear_room():
  print("There is a bear here")
  print("The bear has a bunch of honey")
  print("the fat bear is in front of another door.")
  print("How are you going to move the bear?")
  bear_moved = False

  while True:    #while true: creates an infinite loop. You will see here it only stops when you put an input that takes you to the gold room or ends the game directly
    next = input("> ")

    if next == "take honey":
      dead("the bear looks at you then slaps your face off.")
    elif next == "taunt bear" and not bear_moved:    ###not bear_moved means not False = True. 
      print("The bear has moved from the door, you can go through now.")  ###notice that we used PRINT instead of dead(why) function, because we want the loop to continue from here.  
      bear_moved = True
    elif next == "taunt bear" and bear_moved:
      dead("The bear is pissed off and chews your leg off.")
    elif next == "open door" and bear_moved: ###If I directly put open door, it takes the initial value of bear_moved, which is False. which means it will consider it as anything else printed in the "else:" condition below. This is becayse open door and the TRUE condidtion have to be satified. since its FALSE outside of the if statements, it ignores the elif oopen door condition. and then repeat the loop as usual.
      gold_room()
    else:
      print("i got no idea what that means")


def chulu_room():
  print(""" Here you see the great evil chulu.
  He, it, whatever stares at you and you go insane.
  Do you flee for your life or eat your head?""")

  next = input("> ")

  if "flee" in next:
    start()
  elif "head" in next:
    dead("Well that was tasty")
  else:
    chulu_room() ### basically not accepting any value other than flee or head, as it takes you back to the start of chulu_room function and repeats.. 


def dead(why): ### basically ends the game here after printing out whatever statement is assigned to 'why'
  print(why, "Goodjob!")
  exit(0)

def start():  #this is where the game starts. 
  print("""You are in a dark room.
  There's a door to your right and left/
  Which one do you take?""")

  next = input("> ") ##you have to choose left or right, anything else and the game goes to dead function 

  if next == "left":
    bear_room()
  elif next == "right":
    chulu_room()
  else:
    dead("You stumble around the room until you starve.")

start()
#--------------------------------------------------
# Study DRILL - fixing the bug in function gold_room to be able to take in values more than those containing 0 or 1

def gold_room():
  print("this room is full of gold. HOw much do you take?")

  next = input("> ")
  if next.isdigit() == True: ## this checks if the string raw input has only digits in it
    how_much = int(next)  # we assign the string as an integer to a variable
  else:
    print("Not a number.Please enter a number")
    gold_room()   # I added this again so it takes it back to the start
    
  if how_much < 50:
    print("Nice, you got greedy, you win!")
    exit(0)
  else:
    dead("You greedy bastard!")




