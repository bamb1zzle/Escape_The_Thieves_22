#Escape The Thieves by Andy H 20220606

import pickapathstory
import winsound
from time import sleep

#INTRODUCTION


ready = input("Are you ready to play? ")
winsound.PlaySound("./etv_audio/bg.wav", winsound.SND_ASYNC)
if ready.lower() == "yes":
    pickapathstory.intro()
else:
    exit()

#FORK 1 - SURRENDER OR RUN

sleep(1)
pickapathstory.f1()

do = int(input(""))
if do == 1:
    winsound.PlaySound("./etv_audio/knife_kill1.wav", winsound.SND_LOOP)
    pickapathstory.f1fail()
else:
    pickapathstory.f2()

#FORK 2 - BEDROOM VS BATHROOM
do = int(input(""))
if do == 1:
    pickapathstory.f3bed()

    #FORK 3 - RUN OR HIDE
                
    do = int(input(""))
    if do == 1: 
        winsound.PlaySound("./etv_audio/foundyou.wav", winsound.SND_LOOP)
        pickapathstory.f3bedcloset()
        
    else:
        pickapathstory.f4bedfireescape()

    #FORK 4 - UP OR DOWN

    do = str(input(""))
    if do.lower() == "up":
        winsound.PlaySound("./etv_audio/mario_fall_death.wav", winsound.SND_LOOP)
        pickapathstory.f4bedfireescapeup()
    else: 
        winsound.PlaySound("./etv_audio/trash.wav", winsound.SND_LOOP)
        pickapathstory.f4bedfireescapedown()

else:
    #FORK 5 - BATH
    
    pickapathstory.f5bath()

    #FORK 5 - FIGHT OR FREEZE

    do = int(input(""))
    if do == 1:
        winsound.PlaySound("./etv_audio/gun.wav", winsound.SND_LOOP)
        pickapathstory.f5bathfail()
    else:
        pickapathstory.f6bathpanic()

    #FORK 6 - LEFT OR RIGHT

        do = str(input(""))
        if do.lower() in ("left", "left brick"):
            winsound.PlaySound("./etv_audio/we did it.wav", winsound.SND_LOOP)
            pickapathstory.win()
            winsound.PlaySound("./etv_audio/win.wav", winsound.SND_LOOP)
        else:
            winsound.PlaySound("./etv_audio/disco.wav", winsound.SND_LOOP)
            pickapathstory.f6bathpanicfail()
            winsound.PlaySound("./etv_audio/discodeath.wav", winsound.SND_LOOP)


#Thank you for playing. This game was inspired by the Hulu series, "Only Murders In The Building."
