#!/usr/bin/env python
import time
import random

#this is a role playing game with six rooms

def getName():
    print('What is your name?')
    playerName = input()
    return(playerName)

def displayIntro(playerName):
    print('You are standing in front of an old house in a dark wood.')
    print('The paint is peeling. Windows are broken. Cobwebs sit in the')
    print('corners. It is dark outside, and the full moon peeks out from')
    print('Behind the clouds.')
    time.sleep(2)
    print('You notice the mailbox is open. An envelope inside has one name')
    print('on it:')
    time.sleep(1)
    print(playerName)
    print('Do you open the letter? (yes or no)')
    answer = input()
    return(answer)
    
def displayLetter(playerName):
    print("You open the letter. It reads...")
    print("Dear " + playerName + ",")
    print("If you are reading this letter, you have found the home of")
    print("my ancestors. Inside is an ancient family treasure.")
    print("If you  find it, it is yours to keep.")
    print("I want no more to do with this accursed house or its contents.")
    time.sleep(2)
    print("")

def showInstruction():
    print("RPG Game")
    print("========")
    print("Commands:")
    print("'go [direction]'")
    print("'get [item]'")
    print("'inventory'")
    print("'quit'")

def showItems():
    print("In the room you find:")
    #iterate the list of items in the room
    for i in range(len(rooms[currentRoom]["items"])):
        print("a " +rooms[currentRoom]["items"][i])
 
def showBattle(currentRoom):
    #loop while the monster's hp is greater than 0
    while npc[rooms[currentRoom]["npc"][0]]["hp"] > 0:
        print("You are attacked by a " + rooms[currentRoom]["npc"][0])
        print("You can [r] Run or [a] Attack.")
        #Get the player's move
        battleMove = input()
        #if the player chooses to run...find out which direction
        if battleMove == "r":
            print("Which direction?")
            runDir = input()
            if runDir in rooms[currentRoom]:
                #set the current room to the new room
                currentRoom = rooms[currentRoom][runDir]
                return(currentRoom)
            #there is no door (link) to the new room
            else:
                print("You can't go that way!")
                print("")
                return(currentRoom)
        elif battleMove == "a":
            print("You attack the " + rooms[currentRoom]["npc"][0] )
            #each attack takes 5 hp from monster. TO DO: randomize and add a weapon boost
            npc[rooms[currentRoom]["npc"][0]]["hp"] -=5
            #the lines below don't work (need to add playerHP to the call and the return
            #print("The " + rooms[currentRoom]["npc"][0] + " attacks you.")
            #playerHP -= 5
    print("You defeat the " + rooms[currentRoom]["npc"][0] )
    #the monster is defeated. remove it from the room.
    del(rooms[currentRoom]["npc"][0])
    return(currentRoom)
        
    
def showStatus():
    #print the player's current status
    print("-----------------------------")
    print(rooms[currentRoom]["text"])
    print("-----------------------------")
    
def showInventory():
    #print the player's current inventory
    print("In your trusty knapsack you have:")
    #iterate over the inventory list
    for i in range(len(inventory)):
        print("a " +inventory[i])
    print("")

rooms = {

            1 : {   "name"      : "Outside" ,
                    "text"      : "You are standing in front of an old house in a dark wood. \n The front door to the house is directly north. \n The paint is peeling. Windows are broken. Cobwebs sit in the \n corners. It is dark outside, and the full moon \n peeks out from behind the clouds." ,
                    "north"     : 2 ,
                    "items"     : [] ,
                    "npc"       : [] } ,
            2 : {   "name"      : "Hall" ,
                    "text"      : "You are standing in the front hall of a great house. \n There is a door to the west, one to the north, and another to the south." ,
                    "west"      : 3 ,
                    "south"     : 1 ,
                    "north"     : 4 ,
                    "items"     : ["shovel", "knife"] ,
                    "npc"       : [] } ,
            3 : {   "name"      : "Kitchen" ,
                    "text"      : "You are standing in the kitchen. There is a door to the east." ,
                    "east"      : 2 ,
                    "items"     : [] ,
                    "npc"       : [] } ,
            4 : {   "name"      : "Family Room" ,
                    "text"      : "You are standing in the family room. \n There is a door to the south and one to the east." ,
                    "south"     : 2 ,
                    "east"      : 5 ,
                    "items"     : ["sword"] ,
                    "npc"       : [] } ,
            5 : {   "name"      : "Secret Hall" ,
                    "text"      : "You are standing in a secret hall. \n There is a door to the west and another to the north." ,
                    "west"      : 4 ,
                    "north"     : 6 ,
                    "items"     : ["torch"] ,
                    "npc"       :  [] } ,
            6 : {   "name"      : "Dungeon" ,
                    "text"	: "You are standing in a dungeon. There is a door to the south." ,
                    "south"     : 5 ,
                    "items"     : [] ,
                    "npc"       : ["Gorgon"] } 
        }

items = {
            "torch"     : { "attack"    : 1 } ,
            "sword"     : { "attack"    : 5 } ,
            "knife"     : { "attack"    : 3 }
        }

npc = {
            "Gorgon"    : { "attack"        : 10 ,
                            "hp"            : 10 ,
                            "status"        : 1 } 
        }


#assign some variables
inventory = []
playerHP = 50                  
currentRoom = 1
answer = ""

#start the game...first instructions
showInstruction()
#get the player's name
playerName=getName()
#loop intro to either read letter or not
while answer != "yes" and answer != "no":
    answer = displayIntro(playerName)
    if answer == "yes":
        displayLetter(playerName)
    elif answer == "no":
        continue
    
#loop infinitely
while True:
    #TO DO: need to make playerHP a part of the game
    while playerHP > 0:
        #while in the room with a monster run the battle script
        while rooms[currentRoom]["npc"]:
            currentRoom = showBattle(currentRoom)
        showStatus()
        if rooms[currentRoom]["items"]:
            showItems()
        #get the player's next move
        move = input(">").lower().split()

        #if the player types "go" first
        if move[0] == "go":
            #check that they are allowed to go there
            if move[1] in rooms[currentRoom]:
                #set the current room to the new room
                currentRoom = rooms[currentRoom][move[1]]
            #there is no door (link) to the new room
            else:
                print("You can't go that way!")
                print("")

        #if the player types "get" first
        if move[0] == "get":
            #if the room contains the item add it to the inventory
            if move[1] in rooms[currentRoom]["items"]:
                #add the item to their inventory
                inventory += [move[1]]
                #display a helpful message
                print("You now have the " + move[1] + "!")
                print("")
                #delete the item from the room
                rooms[currentRoom]["items"].remove(move[1])
            #otherwise, if the item isn't there to get
            else:
                #tell the player the item isn't there
                print("Can't get " + move[1] + "!")
                print("")

        #if the player types "inventory"
        if move[0] == "inventory":
            showInventory()

        #if the player types "quit"
        if move[0] == "quit":
            break
    break
print("Good Bye")
