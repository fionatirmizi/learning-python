 from sys import exit

def wolves():
    print("Now select your weapon of choice.")
    weapon_list = ['sword', 'hand grenade', '9 mm']
    for i in weapon_list:
        print(i)

    chosen = input(">")

    if chosen == "sword":
        dead(
            "You are surrounded by two wolves, you stabbed one in the eye, and slashed the throat of the other. You win!"
        )
    elif chosen == 'hand grenade':
        dead("You accidentally blew yourself up!!!")
    elif chosen == "9 mm":
        dead(
            "You shot one in the eye, but the other one got you from behind and bit into your neck. You're dead!"
        )
    else:
        print("Not a valid selection, dude!")
        wolves()


def zombies():
    print(
        "Fighting zombies is no easy task. You have two options. You can fight them alone, and risk dying! Or you can fight with your family, but risk losing a family member. Which challenge do you accept? Select from the list below"
    )
    challenge = ['Last man standing', 'Dear Family']
    for i in challenge:
      print(i)
    alive = True
    chosen = input(">")

    if chosen == 'Last man standing' and alive:
      dead("Well, you risked it but you have a furry friend by your side. Together you both will defeat them!")
    elif chosen == 'Dear Family' and alive:
      dead("Sorry, that was the wrong call bud. They overpowered you and turned your family into zombies. You're a zombie now.")
    else:
      print("That's not a valid selection.")
      zombies()

def darth_vader():
  print("Welcome to the Millenium Falcon. Select your weapon of choice!")
  weapon_list2 = ['lightsaber', 'the force', 'my bare hands']
  for i in weapon_list2:
    print(i)
  defeats = True

  while True:
    chosen = input(">")

    if 'lightsaber' in chosen and defeats:
      print("great, you get to choose another saber, or you can continue with the fight. Dont get too greedy!")
      defeats = False
    elif 'lightsaber' in chosen and not defeats:
      dead("Well, both the lightsabers were no match for Darth Vader. You're dead!")
    elif 'continue' in chosen:
      dead("Smart move, you singlehandedly defeated Darth! Comgrats!")
    elif 'the force' in chosen:
      dead("You did it! You defeated all evil!!!")
    elif 'my bare hands' in chosen:
      dead("Well that was really stupid. You're dead")
    else:
      print("Please make a suitable seleciton next time.")


def dead(result):
    print(result, "Game over.")
    exit(0)        


def start():
    print("""Choose the enemy you wish to fight from the list below!""")
    enemy_list = ['Wolves', 'Zombies', 'Darth Vader']
    for i in enemy_list:
        print(i)

    chosen = input(">")

    if chosen == "1" or chosen == "Wolves":
        wolves()
    elif chosen == "2" or chosen == "Zombies":
        zombies()
    elif chosen == "3" or chosen == "Darth Vader":
        darth_vader()
    else:
        print("That's not a valid selection.")
        start()


start()
