import cmd
import textwrap
import sys
import os
import time
import random
from time import sleep



######Class setup########
class player():
	def __init__(self):
		self.name = ''
		self.hp = 100
		self.mp = 100
		self.strength = 30
		self.defense = 20
		self.level = 1
		self.status_effects = []
		self.location = "a1"
		self.job = ""
		self.game_over = False
		self.weapon = ""
		self.skillpoint = 0

userplayer = player()

############ ENEMY CLASSES ##################
class enemy():
	def __init__(self):
		self.name = ""
		self.hp = ""
		self.strength = 20
		self.level = 1

panther = enemy()
panther.name = "Panther"
panther.hp = 150
panther.strength = 25
panther.defense = 10
panther.level = 1

wolverine = enemy()
wolverine.name = "Wolverine"
wolverine.hp = 300
wolverine.strength = 40
wolverine.defense = 30
wolverine.level = 15

wyvern = enemy()
wyvern.name = "Ice Sieger Wyvern"
wyvern.hp = 750
wyvern.strength = 200
wyvern.level = 50

bear = enemy()
bear.name = "Hungry Bear"
bear.hp = 250
bear.strength = 65
bear.level = 10

bandit = enemy()
bandit.name = "Chief Bandit"
bandit.hp = 300
bandit.strength = 75
bandit.level = 30

citybandit = enemy()
citybandit.name = "City Bandit"
citybandit.hp = 250
citybandit.strength = 50
citybandit.level = 20

robber = enemy()
robber.name = "Highway Man"
robber.hp = 150
robber.strength = 35
robber.level = 7




####################### NPC CLASSES ###################

class npc():
	def __init__(self):
		self.name = ""
		self.description = ""
		self.dialogue = ""
		self.bond = "Neutral"

dungeonguy = npc()
dungeonguy.name = "Edward Elric"
dungeonguy.description = "A budding Alchemist with mysterious skills and a metal arm and leg.\nHe is planning on exploring the cave in hopes of finding any clues.\nHe may have something to say."
dungeonguy.dialogue = "Oh, you came out the cave?\nDid you see anything or any weird things?\nNo..., well then, looks like I have to look somewhere else.\nAnyway, you look a bit weak, so have this steak.\nDon't worry, I caught it myself, I'm very good at traps."
dungeonguy.bond = "Neutral"

oldman = npc()
oldman.name = "Old Man"
oldman.description = "No one knows who he is or what he does.\nHe spends his days sitting in the chair outside."
oldman.dialogue = "It's y-you. I-It can't b-b-be.\nIt's way t-too early in the timestream\nCome back when it is done.\nFor now, take either this sword or dagger, I hope it will aide you."
oldman.bond = "REDACTED"

monk = npc()
monk.name = "Head Priest"
monk.description = "He heads the Divine Belief in Arkansis City.\nDivine Belief is a religion/cult who believe that they are here as a punishment.\nThe Priest has had some issues with people due to his strong beliefs."
monk.dialogue = "We are living in dire times.\nWe are being punsished and we must atone.\nThis land has only one holy shrine left, hidden in the deep forest.\nWe must be aware of each other. "
monk.bond = "Neutral"

king = npc()
king.name = "King Eizenhower"
king.description = "The monarchy stands strong in Arkansis, as the King is the most powerful person in the empire\nHowerver, this makes him a target to many foes and enemeies."
king.bond = "Honoured"

guide = npc()
guide.name = "Mountain Guide"
guide.description = "A mysterious person who stands guard at the bottom of Mount Sieger."
guide.dialogue = "Oh, a fellow adventurer.\nAt the top of this mountain liesa vicious wyvern.\nTo provide some help, take this magic staff."
guide.bond = "Neutral"

princess = npc()
princess.name = "Princess Angel"
princess.description = "The only daughter of King Eizenhower, she has grown up to rejct the monarchy and become rebellious.\nHowever, this has also made her a prime target."
princess.dialogue = "You saved me oh brave adventurer.\nMy hear flutters at the sight of your bravery.\nPlease take me back to my father."
princess.bond = "Admired"

####################### WEAPON CLASSES #############

class weapon():
	def __init__(self):
		weapon.name = ""
		weapon.description = ""
		weapon.type = ""
		weapon.rarity = ""
		weapon.damage = 10

barefists = weapon()
barefists.name = "Bare Fists"
barefists.description = "It's just your fists. Nothing else"
barefists.type = "Meele"
barefists.rarity = "Common"
barefists.damage = 20

startsword = weapon()
startsword.name = "Starting Sword"
startsword.description = "It's a classic sword though it's quite heavy and old."
startsword.type = "Meele"
startsword.rarity = "Common"
startsword.damage = 20

shrinestaff = weapon()
shrinestaff.name = "Divine Staff"
shrinestaff.description = "A holy staff imbued with magic and healing powers."
shrinestaff.type = "Magic"
shrinestaff.rarity = "Rare"
shrinestaff.damage = 50

cliffdagger = weapon()
cliffdagger.name = "Dagger of Despair"
cliffdagger.description = "The dagger has been fused with the many souls that have been taken at the cliff."
cliffdagger.type = "Meele"
cliffdagger.rarity = "Rare"
cliffdagger.damage = 70

guidestaff = weapon()
guidestaff.name = "Inferno Staff"
guidestaff.description = "Potent against ice monsters, this fiery staff can burn enemies and summon a minion."
guidestaff.type = "Magic"
guidestaff.rarity = "Rare"
guidestaff.damage = 65

wyvernsword = weapon()
wyvernsword.name = "Ice Sword"
wyvernsword.description = "Nice sword, bro"
wyvernsword.type = "Magic"
wyvernsword.rarity = "Epic"
wyvernsword.damage = 75


shadowdagger = weapon()
shadowdagger.name = "Dagger of Death"
shadowdagger.description = "A mysterious weapon which holds immese power and the strange power to control the darkness."
shadowdagger.type = "Meele"
shadowdagger.rarity = "Primordial"
shadowdagger.damage = 150

justicesword = weapon()
justicesword.name = "Sword of Justice"
justicesword.description = "A sword passed down for genrations capable of using mana and magic."
justicesword.type = "Magic"
justicesword.rarity = "Primordial"
justicesword.damage = 150


######## Title Screen ###########3
def menu_options():
	option = input("--> ")
	if option.lower() == "play":
		setup_game()
	elif option.lower() == "quit":
		print("Goodbye.")
		sys.exit()
	elif option.lower() == "help":
		help_menu()
	else:
		print("Enter a valid option.")
		option = input("-->")


def title_screen():
	os.system('clear')
	print("---------------- Welcome to the Arkansis RPG ------------------")
	print("                          - Play -                                  ")
	print("                          - Help -                                  ")
	print("                          - Quit -                                  ")
	print("                - Copyright 2020, Void Corp -                       ")
	menu_options()


def help_menu():
	print("---     ------- Welcome to the Arkansis RPG ------------")
	print("         - Type in your commands to play the game-         ")
	print("             - Inspect / Examine all areas. -              ")
	print("              ------------------------------                ")
	print("                   | A1 | B1 | C1 | D1|               ")
	print("              ------------------------------                ")
	print("                   | A2 | B2 | C2 | D2|               ")
	print("              ------------------------------                ")
	print("                   | A3 | B3 | C3 | D3|               ")
	print("              ------------------------------                ")
	print("                   | A4 | B4 | C4 | D4|               ")
	print("              ------------------------------                ")
	print("                      - Good Luck -                          ")
	print("               - Copyright 2020, Void Corp -                ")




  

#############  -Main Game-  ############




############## MAP ###############

#a1 b2 c3 d4 e5
#

AREANAME = "name"
DESCRIPTION = "description"
EXAMINATION = "info"
SOLVED = False
ENEMY = False
LOOT = False
NPC = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "east"
RIGHT = "right", "west"

solved_places = {"a1": False, "a2": False, "a3": False, "a4": False, "a5": False, 
                 "b1": False, "b2": False, "b3": False, "b4": False, "b5": False,
                 "c1": False, "c2": False, "c3": False, "c4": False, "c5": False, 
                 "d1": False, "d2": False, "d3": False, "d4": False, "d5": False,
                 "e1": False, "e2": False, "e3": False, "e4": False, "e5": False, 
           		}

zonemap = { "a1": {AREANAME:"Starting Cave",
				DESCRIPTION:"You have woken up and don't know where you are.",
				EXAMINATION:"There seems to be nothing around you except a chest.",
				SOLVED:False,
				ENEMY:False,
				LOOT:True,
				NPC:False,
				UP: "",
				DOWN : "a2",
				LEFT : "",
				RIGHT : "b1",
				},
			"a2": {AREANAME : "Cave Entrance",
				DESCRIPTION : "The entrance to the cave you started from.",
				EXAMINATION : "There seems to be someone outside the cave.",
				SOLVED : False,
				ENEMY:False,
				LOOT:False,
				NPC:True,
				UP : "a1",
				DOWN : "a3",
				LEFT : "",
				RIGHT : "b2",
				},
			"a3": {AREANAME : "Forest",
				DESCRIPTION : "The forest are full of rare plants and beautiful plants.\nHowever, there also seems to some enemies.",
				EXAMINATION : "info",
				SOLVED : False,
				ENEMY:True,
				LOOT:False,
				NPC:False,
				UP : "a2",
				DOWN : "a4",
				LEFT : "",
				RIGHT : "b3",
				},
			"a4": {AREANAME : "Shrine",
				DESCRIPTION : "description",
				EXAMINATION : "info",
				SOLVED : False,
				ENEMY:False,
				LOOT:True,
				NPC:False,
				UP : "a3",
				DOWN : "",
				LEFT :"",
				RIGHT : "b4",
				},
			################################### BBBBBBBBBBBBBBBBBBBBBBBBBBB
			"b1": {AREANAME : "Old Lodge",
				DESCRIPTION : "description",
				EXAMINATION :"info",
				SOLVED : False,
				ENEMY:False,
				LOOT:False,
				NPC:True,
				UP : "",
				DOWN : "b2",
				LEFT : "a1",
				RIGHT : "c1",
				},
			"b2": {AREANAME : "Pathway",
				DESCRIPTION : "description",
				EXAMINATION : "info",
				SOLVED : False,
				ENEMY:True,
				LOOT:False,
				NPC:False,
				UP : "b1",
				DOWN : "b3",
				LEFT : "a2",
				RIGHT : "c2",
				},
			"b3": {AREANAME : "Forest",
				DESCRIPTION : "nice",
				EXAMINATION : "info",
				SOLVED : False,
				ENEMY:True,
				LOOT:True,
				NPC:False,
				UP : "b2",
				DOWN : "b4",
				LEFT : "a3",
				RIGHT : "c3",
				},
			"b4": {AREANAME :"Cliff",
				DESCRIPTION : "description",
				EXAMINATION : "info",
				SOLVED : False,
				ENEMY:False,
				LOOT:True,
				NPC:False,
				UP : "b3",
				DOWN : "",
				LEFT : "a4",
				RIGHT : "c4",
				},
			######################################## CCCCCCCCCCCCCCC
			"c1": {AREANAME : "Arkansis City",
				DESCRIPTION : "description",
				EXAMINATION : "info",
				SOLVED : False,
				ENEMY:False,
				LOOT:False,
				NPC:True,
				UP : "",
				DOWN : "c2",
				LEFT : "b1",
				RIGHT : "d1",
				},
			"c2": {AREANAME : "City Gate",
				DESCRIPTION : "description",
				EXAMINATION : "info",
				SOLVED : False,
				ENEMY:False,
				LOOT:False,
				NPC:True,
				UP : "c1",
				DOWN : "c3",
				LEFT : "b2",
				RIGHT : "d3",
				},
			"c3": {AREANAME : "Hunting Grounds",
				DESCRIPTION : "description",
				EXAMINATION : "info",
				SOLVED : False,
				ENEMY:True,
				LOOT:False,
				NPC:False,
				UP : "c2",
				DOWN : "c4",
				LEFT : "b3",
				RIGHT : "d3",
				},
			"c4": {AREANAME : "Bandit Hideout",
				DESCRIPTION : "description",
				EXAMINATION : "info",
				SOLVED : False,
				ENEMY:True,
				LOOT:False,
				NPC:True,
				UP : "c3",
				DOWN : "",
				LEFT : "b4",
				RIGHT : "d4",
				},
			#################################### DDDDDDDDDDDDDDDDDDDDDDDDDD
			"d1": {AREANAME : "Palace",
				DESCRIPTION : "description",
				EXAMINATION : "info",
				SOLVED : False,
				ENEMY:False,
				LOOT:True,
				NPC:True,
				UP : "",
				DOWN : "d2",
				LEFT : "c1",
				RIGHT : "",
				},
			"d2": {AREANAME : "City Gate",
				DESCRIPTION : "description",
				EXAMINATION : "info",
				SOLVED : False,
				ENEMY:True,
				LOOT:False,
				NPC:False,
				UP : "d1",
				DOWN : "d3",
				LEFT : "c2",
				RIGHT : "",
				},
			"d3": {AREANAME :"Pathway to Mount Sieger",
				DESCRIPTION : "description",
				EXAMINATION : "info",
				SOLVED : False,
				ENEMY:False,
				LOOT:True,
				NPC:True,
				UP : "d2",
				DOWN : "d4",
				LEFT :"c3",
				RIGHT : "",
				},
			"d4": {AREANAME : "Mount Sieger",
				DESCRIPTION : "description",
				EXAMINATION : "info",
				SOLVED : False,
				ENEMY:True,
				LOOT:True,
				NPC:False,
				UP : "d3",
				DOWN : "",
				LEFT : "c4",
				RIGHT : "",
				},

}

######### INTERACTIVITY #############

def print_location():
	print("\n" + "-" * (4 + len(userplayer.location)))
	print("-" + userplayer.location.upper() + "-")
	print("-" + zonemap(userplayer.location)(DESCRIPTION) + "-")
	if zonemap(userplayer.location[SOLVED]) == False:
		print('-' + "This area has not been completed." + "-")
	print("\n" + "-" * (4 + len(userplayer.location)))


def prompt():
    looks = ["inspect", "interact", "look", "examine"]
    movement = ["travel", "go", "move", "walk"]
    print("\n" + "==================")
    print("What do you want to do?")
    action = input("--->")
    if action == "quit":
        print("Goodbye.")
        sys.exit()
    elif action in movement:
        player_move()
    elif action in looks:
        player_examine()
    elif action == "stats":
        stats()
    else:
        print("Choose a valid option.")
        action = input("--->")

def stats():
	print("Stats -->\nName:", userplayer.name, 
		 "HP: ",userplayer.hp,
		 "Strength: ", userplayer.strength, 
		 "Defense: ", userplayer.defense,
		 "Level: ", userplayer.level,
		 "Equipped Weapon: ", userplayer.weapon
		 )

def combatprompt():
	global command
	command = int(input("Do you want to:\n1.Light attack\n2.Heavy attack\n3.Defend\n4.Special Ability\n--> "))
	return command

weapone = userplayer.weapon

def enemyattack(e):
	var = random.randint(1,4)
	if var == 1:
		userplayer.hp = userplayer.hp - e.strength
		print("The enemy has dealt ", e.strength, "damage.\nYou have ", userplayer.hp, "health left.")
	elif var == 2:
		userplayer.hp = userplayer.hp - (e.strength * 1.5)
		print("The enemy has dealt ", e.strength * 1.5, "damage.\nYou have ", userplayer.hp, "health left.")
	else:
		print("errororr")
		sys.exit()


def battle(e, w):
  while e.health > 0:
    combatprompt()
    if command == 1:
      e.health = (e.health + e.defense) - (userplayer.strength + w.damage)
      print("You have dealt", (userplayer.strength + w.damage), ".\nThe enemy now has", e.health, "left.")
      enemyattack(e)
      combatprompt()
    elif command == 2:
      e.health = (e.health + e.defense) - ((w.damage + userplayer.strength)  * 2)
      print("You have dealt", ((w.damage + userplayer.strength)  * 2), ".\nThe enemy now has", e.health, "left.")
      enemyattack(e)
      combatprompt()
    elif command == 3:
      userplayer.health = userplayer.health - (e.strength - (userplayer.strength))
      print("You have", userplayer.health, "health left", "\nThe enemy has", e.health, "left.")
      enemyattack(e)
      combatprompt()
    elif command == 4:
        if w.ability == "Not available":
          print("Special ability is not available.\nChoose another method.")
          enemyattack(e)
          combatprompt()
        else:
          print("Special ability taking place.")
          combatprompt()
    else:
      ("Choose a valid option.")
      combatprompt()
  if e.health <= 0:
    print("You have defeated the", e.name, ".\nYou have gained a skill point.")
    prompt()


def player_move():
	ask = "Where do you want to go?\n--->"
	dest = input(ask)
	if dest in  ["up", "north"]:
		destination = zonemap[userplayer.location][UP]
		movement_handler(destination)
	elif dest in ["down", "south"]:
		destination = zonemap[userplayer.location][DOWN]
		movement_handler(destination)
	elif dest in ["left", "east"]:
		destination = zonemap[userplayer.location][LEFT]
		movement_handler(destination)
	elif dest in ["right", "west"]:
		destination = zonemap[userplayer.location][RIGHT]
		movement_handler(destination)

def movement_handler(destination):
	print("-" + "You have moved to the " + zonemap[userplayer.location][AREANAME] + "-")
	userplayer.location = destination
	print_location()

def player_examine():
	if zonemap[userplayer.location][SOLVED]:
		print("You have already done this zone.")
	else:
		if zonemap[userplayer.location][ENEMY] == True:
			print("An enemy is nearby.")
			battleask = input("Do you want to fight?\ny/n\n---> ")
			if battleask == "y" or "yes":
				if zonemap[userplayer.location] == "a3":
					battle(panther, weapone)
				elif zonemap(userplayer.location) == "b2":
					battle(robber, weapone)
				elif zonemap(userplayer.location) == "b3":
					battle(wolverine, weapone)
				elif zonemap(userplayer.location) == "c3":
					battle(bear, weapone)
				elif zonemap(userplayer.location) == "c4":
					battle(bandit, weapone)
					princess.bond = "Loved"
					king.bond = "Trusted"
				elif zonemap(userplayer.location) == "d2":
					battle(citybandit, weapone)
				elif zonemap(userplayer.location) == "d4":
					battle(wyvern, weapone)
				else:
					prompt()
		elif zonemap[userplayer.location][NPC] == True:
			print("An NPC is nearby.")
			npcask = "Do you want to interact?\ny/n\n"
			if npcask == "y" or "yes":
					if zonemap(userplayer.location) == "a2":
						npcd(dungeonguy)
						print("The steak has healed you to full health.")
						userplayer.hp = 100
					elif zonemap(userplayer.location) == "b1":
						npcd(oldman)
					elif zonemap(userplayer.location) == "c1":
						npcd(monk)
					elif zonemap(userplayer.location) == "d1":
						npcd(king)
					elif zonemap(userplayer.location) == "d3":
						npcd(guide)
					else:
						prompt()
		elif zonemap[userplayer.location][LOOT] == True:
			print("A chest is nearby.")
			chestask = "Do you want to interact?\ny/n\n"
			if chestask == "y" or "yes":
					if zonemap(userplayer.location) == "a1":
						  wponchest(startsword, weapone)
					elif zonemap(userplayer.location) == "a4":
						  wponchest(shrinestaff, weapone)
					elif zonemap(userplayer.location) == "b4":
						  wponchest(cliffdagger, weapone)
					elif zonemap(userplayer.location) == "d1":
						if princess.bond == "Love":
							wponchest(shadowdagger, justicesword)
					elif zonemap(userplayer.location) == "d3":
						  wponchest(guidestaff, weapone)
					elif zonemap(userplayer.location) == "d4":
						  wponchest(wyvernsword, weapone)
      else: 
        prompt()
    else:
      print("This option is not available.")

      

def skilltree():
	print("========= SKILL TREE =========")
	print("====.  Enhanced Strength  .===")
	print("====.   |             |   .===")
	print("=. Increased       Increased .=")
	print("=.  Defense        Vitality .=")
	print("===.   |               |   .===")
	print("==. Minion          Healing .==")
	skilllevel = 0
	if userplayer.skillpoint > 0:
			if skilllevel == 0:
				askzs = input("Enter y or yes if you want to invest your skillpoint in:\nEnhanced Strength\nIncreases the strength of the user")
				if askzs == "y" or "yes":
					userplayer.skillpoint -= 1
					userplayer.strength += 25
					print("Enhanced Strength has been acquired.\nGives the user additinal strength.\nYou can now obtain new skills. ")
					skilllevel = 1
				else:
					prompt()
			elif skilllevel == 1:
				askos = input("Enter y or yes if you want to invest your skillpoint in:\nEnhanced Vitality\nIncreases the health of the user")
				if askos == "y" or "yes":
					userplayer.skillpoint -= 1
					userplayer.strength += 100
					print("Enhanced Vitality has been acquired.\nGives the user additinal health.\nYou can now obtain new skills. ")
					skilllevel = 1
				else:
					prompt()





def npcd(a):
	print("You have met ", a.name, ".\n", a.description)
	npcaskt = input("Do you want to talk with them?\ny/n\n---> ")
	if npcaskt == "y" or "yes":
		print(a.dialogue)




def wponchest(a, b):
	print("Name: ", a.name + ("-" * (10 + len(a.name))) + "Name: ", b.name )
	print("Type: ", a.type + ("-" * (10 + len(a.type))) + "Type: ", b.type )
	print("Description: ", a.description + 
		("-" * (10 + len(a.description))) + "Description: ", b.description )
	print("Damage: ", a.damage + ("-" * (10 + len(a.damage))) + "Damage: ", b.damage )

	action = input("Which do you pick?\n---> ")
	if action is a.name:
		userplayer.weapon = a.name
		print(a.name, "has been equipped.")
		prompt()
	elif action is b.name:
		userplayer.weapon = b.name
		print(b.name, "has been equipped.")
		prompt()
	else:
		print("Write the name of the weapon.")
		action = ("---> ")


##########3 FUNTINALITY ###########	

def main_game_loop():
	while userplayer.game_over is False:
		prompt()
		#BOSS KILLER

def intro():
    	print("Welcome to the land of Arkansis.\nYou start your tale in a cave as a", userplayer.job + 
    	".\nExplore the land, defeat the monsters, win the hearts of the people and defeat the Archlich.")
    	prompt()

def setup_game():
    os.system('clear')

    player_name = input("Enter your name\n---> ")
    userplayer.name = player_name
    

    player_class = input("Choose your class.\nWarrior\nMage\nAssassin\n---> ")
    valid_classes = ["warrior", "mage", "assassin"]
    userplayer.job = player_class
    print("You are now a " + userplayer.job + ".")
    intro()
    if player_class not in valid_classes:
      print("Choose a valid class.")
      player_class = input("---> ")

    if userplayer.job == "warrior":
      userplayer.hp = 150
      userplayer.mp = 50
      userplayer.strength = 100
      userplayer.defense = 30
      pass
      prompt()
    elif userplayer.job == "mage":
      userplayer.hp = 100
      userplayer.mp = 150
      userplayer.strength = 50
      userplayer.defense = 20
      prompt()
    elif userplayer.job == "assassin":
      userplayer.hp = 100
      userplayer.mp = 75
      userplayer.strength = 150
      userplayer.defense = 25
      prompt()
    else:
      sys.exit()

    ############### INTRO.  ###############



title_screen()




