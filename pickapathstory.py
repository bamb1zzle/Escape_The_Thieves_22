#PickAPath Text Story - Andy H 20220606
import sys

from time import sleep

#Introduction

def intro():
     for x in i:
        sleep(0.005)
        sys.stdout.write(x)
        sys.stdout.flush()

i = "\n*************************************************\nWelcome to the game, Escape the Thieves!\n*************************************************\n\nIn this game you are playing a hotel guest who has just entered her best friends apartment to have dinner.\nAs you burst in unannounced as always, your clumsy foot awkwardly meets a patch of cold blood on the floor. As your eyes follow the blotched red carpet, you see it. Her lifeless body decorated the ground like a twister mat with all her culprits standing over it avoiding red. Your panic spikes as they finally notice you and proceed to chase you out of the apartment.\n\nYou flee into your apartment a few doors down and lock the door but they are quick on your tail and are trying to break the door as we speak!\n\nWhat do you do?"

#Fork 1 - Intro

def f1():
    for x in fork1:
        sleep(0.025)
        sys.stdout.write(x)
        sys.stdout.flush()

def f1fail():
    for x in fork1f:
        sleep(0.025)
        sys.stdout.write(x)
        sys.stdout.flush()

fork1 = "\n1. Open the door to the thieves, telling them you will pretend you didn't see anything and hope they spare your life.\n2. Sprint down the hall further away from the door.\n"
fork1f = "The murderers are not so merciful and decide to kill you. \n ***GAME OVER***"


#Fork 2 - Doors

def f2():
    for x in fork2:
        sleep(0.025)
        sys.stdout.write(x)
        sys.stdout.flush()

fork2 = "\nYou bolt down the hall and the thieves are seconds away from bursting your front door open. You meet two doors at the end of the hall. \nWhich door do you enter?\n1. Your bedroom door.\n2. Your bathroom door.\n"

#Fork 3 - Bedroom Door Path

def f3bed():
    for x in fork3bed:
        sleep(0.025)
        sys.stdout.write(x)
        sys.stdout.flush()

def f3bedcloset():
    for x in fork3bedcloset:
        sleep(0.025)
        sys.stdout.write(x)
        sys.stdout.flush()

fork3bed = "You enter your room but the thieves had just caught a glimpse of you whilst bursting open the door and proceed to run down the hall.\nDo you:\n1. Hide in your closet that looks too small to hide anything and hope they don't bother checking. \n2. Open your bedroom window and hop out to the fire escape.\n"
fork3bedcloset = "You squeeze into your tiny closet amongst your dainty dresses and fat coats. The thieves enter into your bedroom and ravage around trying to find you. As they approach the closet your nervousness peaks and you break out in a scream. You are now dead. \n ***GAME OVER***"

#Fork 4 - Fire Escape Path

def f4bedfireescape():
    for x in fork4bedfireescape:
        sleep(0.025)
        sys.stdout.write(x)
        sys.stdout.flush()

def f4bedfireescapeup():
    for x in fork4bedfireescapeup:
        sleep(0.025)
        sys.stdout.write(x)
        sys.stdout.flush()

def f4bedfireescapedown():
    for x in fork4bedfireescapedown:
        sleep(0.025)
        sys.stdout.write(x)
        sys.stdout.flush()

fork4bedfireescape = "You hop onto the fire escape.\nDo you go UP or DOWN the escape?"
fork4bedfireescapeup = "You proceed to run up the stairs all the way to the roof. The robbers have now caught up to you on the roof. There is no escape. They throw you off the building. \n ***GAME OVER***"
fork4bedfireescapedown = "You go down the fire escape but due to the old age of the building the ladder to the ground of the fire escape doesn't extend and you are caught by the robbers and disposed of in the garbage bins below the fire escape. \n***GAME OVER*** "

#Fork 5 - Bathroom Door Path

def f5bath():
    for x in fork5bath:
        sleep(0.025)
        sys.stdout.write(x)
        sys.stdout.flush()

def f5bathfail():
    for x in fork5bathfail:
        sleep(0.025)
        sys.stdout.write(x)
        sys.stdout.flush()

fork5bath = "You enter your bathroom and call the police to alert them what has happened. Although the locked door is sturdy, you know it wont be long until they break the door and the police are still 15 minutes away.\nWhat do you do?\n1. Grab the gun you hide in the tank of your toilet. \n2. Sit in the corner of your bathroom against the wall and wonder where your life went wrong.\n"
fork5bathfail = "As the thieves finally open the door after continuous barrage of kicks and body slams they are surprised to see you with a weapon. You shoot one of them but end up being tackled by the rest and die.\n***GAME OVER***"

#Fork 6 - Bathroom Panic Path 

def f6bathpanic():
    for x in fork6bathpanic:
        sleep(0.025)
        sys.stdout.write(x)
        sys.stdout.flush()

def f6bathpanicfail():
    for x in fork6bathpanicfail:
        sleep(0.025)
        sys.stdout.write(x)
        sys.stdout.flush()

fork6bathpanic = "While sitting against the corner of the bathroom and reflecting on your life you notice that some bricks are loose in the wall. You begin to probe the wall and notice two bricks that can be fully indented and pushed into the wall. \nWhich brick do you press into? The LEFT BRICK or RIGHT BRICK?\n"  
fork6bathpanicfail = "This brick turns on a hidden speaker system in the bathroom that plays disco music. The thieves enter and dance on your body. \n***GAME OVER***"

#END - Winning Path

def win():
    for x in end:
        sleep(0.025)
        sys.stdout.write(x)
        sys.stdout.flush()

end = "You open a trap door beneath you that gives you enough space to hide in. You hop into the space and leave the thieves flabbergasted as to how you have escaped.\nThe police have arrived and the thieves are captured. You survive.\n***YOU WIN***"
           
