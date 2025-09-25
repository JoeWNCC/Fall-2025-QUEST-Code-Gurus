"""
    QUEST game
    Author: Joe Scott

    NOTES: To get the program to work, you must install utils from your console!
"""

from time import sleep
import utils
import os
from random import randint

# Menu
os.system('cls')
print(utils.title(" QUEST "))
sleep(3)

# ----- VARIABLES ----- #
# Weapons
sword = 0
Scary_axe = 0

# Trinkets/Items
map = 0
Magic_Meal = False
Stick = False
Torch = False
Neck_Cloth = True # Spend it to make a torch when you have a stick
rations = 0

# Allies/Hires
Rogue = 0
Chef = 0
Werewolf = False
Ally = "To be decided"

# Event Variables
Stalked = False
Focus = False
chance = 0

Player_Name = "Knight Guy"

# SKIP FUNCTION
DEBUG = False
if DEBUG == True:
    sec = 0
else:
    sec = 3


# ----- CHANCE FUNCTIONS ----- #
# 50%
def chance_50():
    random = randint(1, 2)
    if random == 1:
        chance = random
    elif random == 2:
        chance = random
    return chance

# 75%
def chance_75():
    random = randint(1, 4)
    if random == 1 or 2 or 3:
        chance = random
    elif random == 4:
        chance = random
    return chance


# ----- ROOMS ----- #
def drab_town():
    
    print(utils.UnderLN("Drab Town"))
    sleep(sec)
    print("You wander your way into a quaint little town after taking on a quest\n"
          "issued from the castle by the village smithy, Ivar, to rescue his beloved\n"
          "daughter.")
    sleep(sec)
    print("\nYou are making your way to his hut to talk about the details of the quest.\n"
          "You approach his house and step through his door.")
    sleep(sec)
    print("\nYou can see him drowning away his sorrows at his workbench with fine mead.\n"
          "A bit much, actually. He notices his new visitor, you, gawking and straightens\n"
          "up swiftly")
    sleep(sec)
    print("\nIVAR: Oh, erm, the mercenary! Pay me no mind, you likely know how a fath'r is\n"
          "without 'is good ol daughter.")
    sleep(sec)
    print("\nIVAR: I don't want to waste any of ye time, or my little lady's time, so we'll get straight\n"
          "to business...")
    sleep(sec)
    Player_Name = input("\nIVAR: First off, what's yer name, lad!:\n\nYour name?: ")
    print(f"\nIVAR: Haha, ye look like a {Player_Name}!")
    sleep(sec)
    print("Enough jesting, I tell the details now...\n")
    sleep(sec)
    print("\nIVAR: Me daught'r has been taken! Flown off with an evil figure I couldn't get a good look at, "
          "dare I say beast!\n"
          "I can tell ye that the jerk flew off towards those strange ruins, in case ye need directions.\n"
          "I'd go chasin' after 'er but years of poundin' metal are rough on a body..."
          )
    sleep(sec)
    print("\nIVAR: You strange-folk and young'uns are after the thrill o' life anyway, so better give\n"
          "the next generation a fightin' chance!")
    sleep(sec)
    print("Alright, no mo' nice words! Get out and save me lass!\n")
    sleep(sec)
    print("\nYou jump out of your seat eagerly and clank your way out of the door. Time for adventure!\n")
    sleep(sec)
    
    input("Press any key to proceed: ")
    
    os.system('cls')
    sleep(sec)
    print("You make it to the town square and look around. There are shops all around you filled with\n"
          "different odds and ends, and some places that peak your interest; The armory.")
    sleep(sec)
    print("\nBesides the armory, you see a cartography shop, (Maps) a butchers stand, and a nearby pub that\n"
          "other adventurers flood to. You check your pockets... You got enough coin to visit two of\n"
          "these places.")
    sleep(3)
    
    shop_stops = 2
    while shop_stops != 0:
        print(f"\nYou have {shop_stops} shop stops left.")

        choice1 = input("\nSo where to? [1. Armory,  2. Cartographer,  3. Butcher,  4. Pub]:")
        os.system('cls')
        # Armory
        if choice1 == "1":
            print("\nYou jog over to the armory and stare at the one humongous blade displayed neatly over\n"
                  "the fireplace. You think you might need that sword...")
            sleep(sec)
            print("The smith guy sees you staring at it with childlike wonder and comes up to\n"
                  "you.")
            armory = input("\nARMORY CLERK: Didja want it, son? [y/any key] [WILL EXHAUST A SHOP STOP]: ")
            if armory == "y":
                print("\nARMORY CLERK: Tis yours now! Thank ye for the gold!")
                sleep(sec)
                print("\nYou got the BIG SWORD!")
                sleep(sec)
                proceed = input("Press anything to proceed: ")
                sword = 1
                shop_stops -= 1
                
            else:
                print("\nARMORY CLERK: All good, son! Does plenty good lookin pretty for me business!")
                sleep(sec)
                print("You walk back to town square.")

        # Cartographer
        elif choice1 == "2":
            print("\nYou make your way over to the super fancy place of scrolls and maps and walk through\n"
                  "the fancy door.")
            sleep(sec)
            print("\nYou go to the counter and ring the little service bell. A skinny bearded man shuffles\n"
                  "towards you.")
            sleep(sec)
            print("\nCARTOGRAPHER: Uh, oh! Hey little guy! What'cha lookin' for?")
            sleep(sec)
            Cartography = input("\nDo you want the ruins map? [y/any key] [WILL EXHAUST A SHOP STOP]: ")
            
            if Cartography == "y":
                print("\nCARTOGRAPHER: Ah, yes! A great map, but our real question is why would you go to the ruins?")
                sleep(sec)
                print("\nCARTOGRAPHER: -uh, pay that question no mind! I think I know what you're doing! Here is this\n"
                      "map for you! I wish you the best luck!")
                sleep(sec)
                print("\nYou got the MAP!\n")
                map = 1
                sleep(sec)
                print("You leave the store with a little sense of security knowing you should know the\n"
                      "way to go!")
                sleep(1)
                proceed = input("Press anything to proceed: ")
                shop_stops -= 1

            else:
                print("\nCARTOGRAPHER: You sure? You think you can find the way just fine? Well, alright little man! Cya later!..\n"
                      "Hopefully!")
                sleep(sec)
                print("\nYou headed back to town square.")

        
        # Butcher
        elif choice1 == "3":
            print("\nYou wander over to the butcher shop, alured by the wonderful scent of cured ham. A gruff man\n"
                  "slaves away at his stand, focused as ever on perfecting his slices.")
            sleep(sec)
            print("\nBUTCHER GUY: Yo, small metal man, lookin' for quality cuts for the journey? No one gets far\n"
                  "without a right and proper meal!")
            sleep(sec)
            Butcher = input("\nDo you want rations? [y/any key] [WILL EXHAUST A SHOP STOP]: ")
            if Butcher == "y":
                print("\nBUTCHER GUY: Wise choice, mate! No starving out there, little man!")
                sleep(sec)
                print("\nYou got the RATIONS! [You have three uses of this]")
                rations = 3
                sleep(sec)
                print("You leave the stand knowing you'll have energy and pump out there.")
                sleep(1)
                proceed = input("Press anything to proceed: ")
                shop_stops -= 1
            else:
                print("\nBUTCHER GUY: If you plan to hunt with your current weapons, I wish you luck!")
                sleep(sec)
                print("You head down to town square.")
        # Pub
        elif choice1 == "4":
            print("\nYou end up getting stuck in the crowd of the pub. After you find some space, two individuals pique\n"
                  "your interest.")
            sleep(sec)
            print("\nYou can see a hooded figure, probably a rogue, leaning against the far wall. They doesn't seem to be\n"
                  "actively searching for people to hire them... Perhaps they're shy?")
            sleep(sec)
            print("\nAnd the hardly hidden chef guy trying to convince a group to hire him. He's making a lot of noise and\n"
                  "seems to only be scaring adventurers away...")
            sleep(sec)
            
            #if rations == 3:
                #print("\nYou did buy rations... Who knows what he could do with them.")
                #sleep(2)
            

            hiring = 0
            while hiring == 0:
                hire = input("\nWho do you wanna talk to? [1. Chef,  2. Rogue,  3. Leave]: ")

                # CHEF
                if hire == "1":
                    print("\nYou shout as loud as you can under your helmet and get the short cook's attention!")
                    sleep(sec)
                    print("\nCOOK: Ah, mama maria! Could you be the one who takes me in? No one else seems to hear me! Please, sir knight!")
                    sleep(sec)
                    cook = input("\nTake him into your party? [y/any key] [WILL EXHAUST A SHOP STOP]: ")
                    if cook == "y":
                        print(f"\nCHEF: YES! YIPPIE! You won't regret this! I am chef Tonio, but just call me Tony. And you are?.. {Player_Name}?\n"
                              "A yes, a fine name! Pleasure to meet you!")
                        Ally = "Tonio"
                        sleep(sec)
                        print(f"\nYou hired {Ally} the chef!")
                        Chef = 1
                        sleep(sec)
                        print(f"\nYou both find your way out of the bar, {Ally} skipping jovially behind!")
                        sleep(1)
                        proceed = input("Press anything to proceed: ")
                        hiring = 1
                        shop_stops -= 1
                    else:
                        print("CHEF: Good greif! I gotta change my approach!")
                        sleep(sec)
            

                # ROGUE
                elif hire == "2":
                    print("\nYou swim through the sea of people to the hooded figure. they glance over at you for but a second, but you can see\n"
                          "from that glance that they have been waiting for somebody to approach for who knows how long.")
                    sleep(sec)
                    print("\nA young womans voice speaks;")
                    sleep(sec)
                    print("\nROGUE: ... Did you, uh... Wanna hire me?.. You could use someone with strong senses in your team... considering your...\n"
                          "helmet.")
                    rogue = input("\nGive the rogue a chance? [y/any key] [WILL EXHAUST A SHOP STOP]: ")
                    if rogue == "y":
                        print(f"\nROGUE: ... Thanks... I mean it. The names Kanra. Somebody told me your name is {Player_Name}. Suits you.")
                        Ally = "Kanra"
                        sleep(sec)
                        print(f"\nYou hired {Ally} the Rogue!")
                        sleep(1)
                        input("Press anything to proceed: ")
                        Rogue = 1
                        hiring = 1
                        shop_stops -= 1
                    else:
                        print("ROGUE: ... You seem to trust yourself, or maybe you lack trust in me... Shouldn't be surprised...")
                        sleep(sec)

                elif hire == "3":
                    print("You changed your mind. The crowd here is kind of strange.")
                    sleep(sec)
                    hiring = 1

    print("\n---\nAfter getting what you would call the necessities, you notice the sun begins to sink below the horizon. Since you see that the road\n"
          "ahead leads to Wood Woods, You think to yourself...\n")
    sleep(5)
    sleep_or_embark = input("Should I embark or rest until morning? [1. REST,  2. EMBARK]: ")
    
    # REST
    if sleep_or_embark == "1":
        print("\nYou decide that it's probably best to tackle the forest in the daylight. Who knows what's out in the dark of night. You stay in the nearby inn.")
        sleep(sec)
        if Rogue or Chef == 1:
            print(f"\nAfter the sun rises over the horizon, you wake up {Ally} and pack up your little camp on the outskirts of town. Your adventure truly begins!")
            sleep(sec)
        else:
            print(f"After the sun rises over the horizon, you awaken, pack up your little camp on the outskirts of town, and begin your quest!")
        wood_woods_day()
    
    # EMBARK
    elif sleep_or_embark == "2":
        print("\nThe blacksmith's princess cannot wait! We must make haste! This darkness is nothing!")
        sleep(sec)
        if Rogue or Chef == 1:
            print(f"\nYou and {Ally} make your way into the forest. Your silhouettes slowly sink into the darkness."
                  "\nWho knows what you'll run into at this hour...")
        else:
            print("\nYou summon up your courage and press on into the dark of the woods. Who knows what you'll see and what will happen...")
        wood_woods_night()
    os.system('cls')
    return Rogue or Chef or sword or map or rations or Ally
    

def wood_woods_day():
    print(utils.UnderLN("Wood Woods"))
    print("\nCOMING SOON!")

def wood_woods_night():
    print(utils.UnderLN("Wood Woods"))
    print("\nCOMING SOON!")

def cave():
    print(utils.UnderLN("The Cave"))

def ruins():
    print(utils.UnderLN("Ruins of Peculiarly Good Smells"))

def sanctum():
    print(utils.UnderLN("Sanctum"))
