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
sword = 1
Scary_axe = 0

# Trinkets/Items
map = 0
Magic_Meal = 0
Stick = 0
Torch = 0
Neck_Cloth = 1 # Spend it to make a torch when you have a stick
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
lives = 3

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
    return random

# 75%
def chance_75():
    random = randint(1, 4)
    return random


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
    sleep(sec)
    
    shop_stops = 2
    while shop_stops != 0:
        print(f"\nYou have {shop_stops} shop stops left.")

        choice1 = input("\nSo where to? [1. Armory,  2. Cartographer,  3. Butcher,  4. Pub]: ")
        os.system('cls')
        # Armory
        if choice1 == "1":
            print("\nYou jog over to the armory and stare at the one humongous blade displayed neatly over\n"
                  "the fireplace. You think you might need that sword...")
            sleep(sec)
            print("The smith guy sees you staring at it with childlike wonder and comes up to\n"
                  "you.")
            armory = input("\nARMORY CLERK: Didja want it, son? [y/any key] [WILL EXHAUST A SHOP STOP]: ").lower()
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
        try: 
            if Rogue or Chef == 1:
                print(f"\nAfter the sun rises over the horizon, you wake up {Ally} and pack up your little camp on the outskirts of town. Your adventure truly begins!")
                sleep(sec)
        except:
            print(f"After the sun rises over the horizon, you awaken, pack up your little camp on the outskirts of town, and begin your quest!")
        wood_woods_day_choice(map)
    
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
    # Return necessary variables
    try:
        if Ally != "To be decided":
            if Rogue == 1:
                return Rogue
            elif Chef == 1:
                return Chef
            return Ally
    except:
        pass
    try:
        if sword == 1:
            return sword
    except:
        pass
    try:
        if map == 1:
            return map
    except:
        pass
    try:
        if rations > 0:
            return rations
    except:
        pass


# Make choice Map/Trail
def wood_woods_day_choice(map):
    # Title
    os.system('cls')
    print(utils.UnderLN("\nWood Woods"))
    sleep(sec)
    # If you have map, this gets run.
    try:
        if map == 1:
            print("\nYou pull out the map that you got from the cartographer and think to yourself...")
            choice = int(input("Use map or follow trail?: [1: Map / 2: Off Trail]: "))
            if choice == 1:
                print("\nYou decide that it would be foolish to even consider going outside the map's directions and follow it's directions.")
                sleep(sec)
                proceed = input("\nPress anything to proceed: ")
                wood_woods_day_map()
            elif choice == 2:
                print("You decide to see where the off-roads take you.")
                sleep(sec)
                proceed = input("\nPress anything to proceed: ")
                wood_woods_day_trail()
            return map
    except:
        # This runs if you don't have map.
        print("\nSince there was no obvious path and you have no map, you decided to just keep moving into the forest blindly...")
        sleep(sec)
        proceed = ("\nPress anything to proceed: ")
        wood_woods_day_trail()
        

# Starting Wood Woods with a map
def wood_woods_day_map():
    print("\nBecause of your wise purchase of a map, you're able to know where the bad areas of the forest are and the direct path to the"
          " cave is. Just as things seem to go well, a tall knight in a black surcoat stands on a bridge, staring off into the distance.")
    sleep(sec)
    print("At his feet lies those who apparently fell before him. You wonder how he did such a thing, as this knight is missing an arm"
          " and a leg...")
    sleep(sec)
    print("You attempt to pass him, but he hops in your way with his one leg.")
    sleep(sec)
    print("\n???: NONE SHALL PASS...")
    sleep(sec)
    print("\nYou stare at the man confuzzled. Who is he to tell you what to do with only two limbs?")
    sleep(sec)
    # This choice is intentional!
    choice1 = int(input("What do you do? [1=Push him over / 2=Push him over]: "))
    print("This man is clearly not gonna move. You point out a bird in the sky and he turns around.")
    sleep(sec)
    print("\n???: Where!?")
    sleep(sec)
    print("\nYou walk up to him and simply topple him over. He cannot pick himself up.")
    sleep(sec)
    print("\n???: Ah, DANG IT! I'm invincible I'll have you know! We'll meet again!")
    sleep(sec)
    print("\nYou walk off feeling a little guilty about what you've done, but your quest waits for no one!")
    sleep(sec)
    print("\nYou make it to the mouth of the cave. With all the strangeness of the forest you've been told of, you feel"
          " like you got through this very well. The map follows into the mouth of the cave, so you summon your courage and disappear"
          " into the darkness of the path ahead...")
    sleep(sec)
    proceed = input("Press anything to proceed: ")
    cave()

# Start of Wood Woods
def wood_woods_day_trail():
    print("As you walk amongst the forest aimlessly, you find a nice looking stick and think about"
          " how you may need a torch if it gets dark out. You found some space for it in your pack and"
          " kept on your merry way.")
    # You got a stick!
    Stick = 1

    print("\nHours have passed, none you have kept track of, but suddenly, stifling the peace is a growl"
          " of a large creature...")
    wood_woods_lumberjack(lives) 

# Initiate the lumberjack
def wood_woods_lumberjack(lives):
    # If you have the rogue:
    if Rogue == 1:
        print(f"\n{Ally}: Hey, {Player_Name}, that isn't a monster behind those shrubs... It's a man. I'll let you decide how we play this out.")
    
    choice = int(input("\nWhatever it is, it hasn't noticed you... How should you proceed? [1. Investigate / 2. Sneak away / 3. Throw your stick at it]: "))
    # Investigate the noise.
    if choice == 1:
        print("\nYou decide that you need to see what this is. Your armor should hold you up fine if it comes down to a fight.")
        print("You breathe in... and then out, and swipe the brush away, and...")
        print("\nCRASH!")
        print("\nThe tree ahead hammers the earth right in front of you. The grunting is from no beast, but rather a hulking man in plaid;"
              " A lumber jack!")
        
        print("\nLUMBERJACK: Stubborn pine! took ye long enough to come down!")
        print("\nHe turns around to fell the next pine and sees your small frame, fixated on the fallen tree.")
        wood_woods_lumberjack_intro()
        
    # Sneak by the creature.
    if choice == 2:
        if Rogue == 1:
            print("You decide not to draw attention to yourself. Who knows if this guy is truly trustworthy. Let's just not bother...")
        else:
            print("You decide it's best not to play with fire. No need to make any silly decisions when your full focus should be to your quest.")
    
    # Throw your stick at the sound!
    if choice == 3:
        print("\nYour intrusive thoughts get the better of you. You take out the stick from your pack and stare at it for a moment.")
        print("You throw it straight past the bush and you here a momentarily satisfying thunk.")
        print("\n???: OW! the hell!?")
        print("\nA huge, plaid, burly man jumps out of the bush on all-fours. He looks very irritated.")
        print("\nYou begin to panick. In the breif moment of thought that you have, you...\n")
        
        if sword == 1:
            choice4 = int(input("[1. or 2. Don't Fight / 3. Fight]: "))
            if choice4 == 3:
                # Draw your sword
                print("\nYou reach for your blade in a hurry and try to find a stance to fight.")
                print("Without a chance to think, he swings his axe sideways!")
                chance = chance_50()
                if chance == 1:
                    print("\nYou manage to duck quickly and strike the hulking man in the temple with the pommel of your sword.")
                    print("He slides against the forest floor five feet behind you, out cold. You breathe a sigh of relief.")
                else:
                    print("\nWHACK!")
                    lives -= 1
                    print(f"\nHe struck you in the side for a chunk of your life!")
                    print(f"HEALTH REMAINING: {lives}/3")
                    print("\nYou pick yourself back up and swing wildly in the guy's direction and nick him once. He reels back!")
                    print("He turns completely and runs away from you, shouting swears as he disappears behind the tree filled hills.")
                    
                # if Chef is in your party
                try:
                    if Chef == 1:
                        print(f"\n{Ally}: I hate to say this so early, my man {Player_Name}, but I want no part of this if I'm going to be" 
                                " in that kind of danger...")
                        print(f"{Ally}: Just take this and I'll be on my way, good luck, guy!")
                        Chef = 0
                        Ally = "No one!"
                        lives += 1
                        print("\nIt's a hastily put together first-aid kit. It's convenient but we've already lost our ally... Dang it...")
                        print(f"HEALTH REMAINING: {lives}/3")
                        return lives
                except:
                    pass
                # if Rogue is in your party
                try:
                    if Rogue == 1:
                        print(f"\n{Ally}: Good fighting, {Player_Name}. As well as you did, I think this could have gone better...")
                        print(f"{Ally}: As much as I loathe talking or trusting people, even I would try talking your way out sometimes.")
                        print("You feel silly, but at least you've got something of a friend to give suggestions to.")
                except:
                    pass
                
                choice5 = int(input("\nAfter your adrenaline finally settles, you see that he dropped his axe... Take it? [1. Yes / 2. No]: "))
                if choice5 == 1:
                    print("\nIt looks quite strong... Given your quest, you're sure something out there will forgive you for taking it.")
                    Scary_axe = 1
                    print("\nYou got the SCARY AXE!")
                    
                else:
                    print("\nYou don't take what you don't absolutely need. You don't need this axe, he does.")
                    print("Maybe you can make ammends after this is all over.")
                
                print("\nYou brush yourself off, stretch, and keep moving forward despite the ever approaching night.")
                wood_woods_night()
                return Scary_axe, lives
            
        choice4 = int(input("[1. Run / 2. Beg for mercy]: "))
        # Run away
        if choice4 == 1:
            print("\nFear seizes your heart and without a thought, you run in any direction that is away from the monster man.")
            print("\nAfter running for until you couldn't hear his swearing anymore, you finally stop to breathe and recover from that sprint.")
            print("\nYou then turn your head up and see that the cave is right before your eyes. You've heard that, although perilous, this"
                  " is one of the better ways to get to the ruins. Why waste this opportunity perfectly placed in front of you?")
            cave()

        # Beg for mercy
        elif choice4 == 2:
            
            print("\nYou fall to the floor and curl up into a ball. You cry out to the man not to hurt you!")
            print("\nLUMBERJACK: Oh geez, sorry about that! Ahem-")
            wood_woods_lumberjack_intro()
        
    return lives

# Meet the lumberjack
def wood_woods_lumberjack_intro():
    print("\nLUMBERJACK: Hey little guy! What are you doing out here? Nobody comes through here for a frolick besids the foolish!")
    choice2 = int(input("\nHow do you answer? [1. I'm out to save the blacksmith's daughter! / 2. None of your business!]: "))
    # I'm saving Ivar's Daughter!
    if choice2 == 1:
        print("\nLUMBERJACK: You mean old man Ivar? You could have used his name! He and I go way back. He used to bug me all the"
                " time about lumber and charcoal for his forge!")
        print("\nLUMBERJACK: Besides that, his daughter isn't safe? I find that hard to believe... She's a fighter with a good noggin"
                " on her shoulders, she wouldn't just be kidnapped, there's gotta be something more to this.")
        print("\nLUMBERJACK: My best tip for you, lad is to also think rationally. You may not have to resort to fighting with good chattin'"
                " skills.")
    # I'm keeping my secrets!
    else:
        print("\nLUMBERJACK: All good buddy! When it's just you and man-eating creatures out here, a good word from a stranger is"
                " entertaining!")
    if map == 1:
        print("Say little man, you need any pointers for these parts? I do live here.")
        choice3 = int(input("\n[1. Yeah, can you read my map? / 2. I'm ok, thanks!]"))
        if choice3 == 1:
            print("\nLUMBERJACK: Yeah, give it here!")
            print("\nHe takes the map from you and squats down so you can see where he is pointing to. It's all making sense now!")
            print("\nLUMBERJACK: Thanks for giving ol' redbeard a chance to help! Hope we meet again some other day, if nothing bad happens!")
            print("\nYou leave with a clear image in your head of the path you must take! No take the wrong turns for this guy!")
            input("Enter any button to continue: ")
            # You travel to the ruins this way, skipping the cave!
            ruins()
        if choice3 == 2:
            print("\nLUMBERJACK: I like your confidence, metal man! A good spirit will take you far!")
            print("\nLUMBERJACK: Take care, don't get yourself hurt!")
            print("\nYou are not sure how you feel about being so protective of your quest, but you can rest well knowing you will not"
                    " likely not be followed.")
            print("\nAs night begins to fall, you approach the foot of a cave. Supposedly, this cave is the best way to the ruins and you have"
                " no better choice than to trust this.")
            input("Enter any button to continue: ")
            # Enter the cave
            cave()

    print("\nLUMBERJACK: It's good to meet friendly faces once in a while, you take care little guy!")
    print("\nYou wave back at him and keep following the path, knowing you made a good friend today.")
    print("\nYou approach the cave after a nice walk through the woods and meet the ominous mouth of the cave. It seems to be the only way to"
          " the ruins, so without wasting any more time, you summon your courage and disappear into the darkness forward.")
    input("Press any button to continue: ")
    cave()

# Start Wood Woods at Night
def wood_woods_night():
    print(utils.UnderLN("Wood Woods"))
    sleep(sec)
    print("It's dark out. Very dark out, but nonetheless your spirits remain high. As far as you can see, it's just tall trees\n"
          "and ever-spanning hills. One of these directions leads to the cave you heard about. Supposedly, through the cave is the\n"
          "way to the ruins. You've got no choice but to follow that tip for right now, since anything could happen to Ivar's daughter.\n")
    sleep(sec)
    print("\nEven if you had a map, it's too dark to see it.")

# Cave
def cave():
    print(utils.UnderLN("The Cave"))
    print("\nCOMING SOON!")

# Ruins
def ruins():
    print(utils.UnderLN("Ruins of Peculiarly Good Smells"))
    print("\nCOMING SOON!")

# Sanctum
def sanctum():
    print(utils.UnderLN("Sanctum"))
    print("\nCOMING SOON!")
