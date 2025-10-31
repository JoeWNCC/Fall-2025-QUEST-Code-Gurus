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
has_map = 0
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

# ---------------- DEBUGGING ---------------- #
DEBUG = False
if DEBUG == True:
    sec = 0
else:
    sec = 3
# ---------------- DEBUGGING ---------------- #


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
    global sword, has_map, rations, Rogue, Chef, Ally, Player_Name, sec, lives

    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")

    # Cross-platform clear screen (Thanks ChatGPT!)
    os.system('cls' if os.name == 'nt' else 'clear')

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
          "up swiftly.")
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
          "I'd go chasin' after 'er but years of poundin' metal are rough on a body...")
    sleep(sec)
    print("\nIVAR: You strange-folk and young'uns are after the thrill o' life anyway, so better give\n"
          "the next generation a fightin' chance!")
    sleep(sec)
    print("Alright, no mo' nice words! Get out and save me lass!")
    sleep(sec)
    print("\nYou jump out of your seat eagerly and clank your way out of the door. Time for adventure!\n")
    sleep(sec)

    input("Press any key to proceed: ")

    os.system('cls' if os.name == 'nt' else 'clear')
    print("You make it to the town square and look around. There are shops all around you filled with\n"
          "different odds and ends, and some places that pique your interest; The armory.")
    sleep(sec)
    print("\nBesides the armory, you see a cartography shop (maps), a butcher’s stand, and a nearby pub that\n"
          "other adventurers flood to. You check your pockets... You got enough coin to visit two of\n"
          "these places.")
    sleep(sec)

    shop_stops = 2
    while shop_stops != 0:
        print(f"\nYou have {shop_stops} shop stops left.")
        choice1 = input("\nSo where to? [1. Armory,  2. Cartographer,  3. Butcher,  4. Pub]: ")
        os.system('cls' if os.name == 'nt' else 'clear')

        # ---------- ARMORY ---------- #
        if choice1 == "1":
            if sword == 1:
                print("\nARMORY CLERK: Little one, even if I did have an extra sword, you would not be able to carry it reasonably... Check out the other places lad!")
                sleep(sec)
                continue

            print("\nYou jog over to the armory and stare at the humongous blade displayed neatly over\n"
                  "the fireplace. You think you might need that sword...")
            sleep(sec)
            print("The smith guy sees you staring at it with childlike wonder and comes up to\n"
                  "you.")
            armory = input("\nARMORY CLERK: Didja want it, son? [y/any key] [WILL EXHAUST A SHOP STOP]: ").lower()
            if armory == "y":
                print("\nARMORY CLERK: Tis yours now! Thank ye for the gold!")
                sleep(sec)
                print("\nYou got the BIG SWORD!")
                sword = 1
                shop_stops -= 1
            else:
                print("\nARMORY CLERK: All good, son! Does plenty good lookin’ pretty for me business!")
            sleep(sec)
            os.system('cls' if os.name == 'nt' else 'clear')

        # ---------- CARTOGRAPHER ---------- #
        elif choice1 == "2":
            if has_map == 1:
                print("\nCARTOGRAPHER: I already gave you my best map! What more do you want?")
                sleep(sec)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            print("\nYou make your way over to the fancy place of scrolls and maps and walk through\n"
                  "the ornate door.")
            sleep(sec)
            print("\nYou go to the counter and ring the little service bell. A skinny bearded man shuffles\n"
                  "towards you.")
            sleep(sec)
            print("\nCARTOGRAPHER: Uh, oh! Hey little guy! What'cha lookin' for?")
            sleep(sec)
            Cartography = input("\nDo you want the ruins map? [y/any key] [WILL EXHAUST A SHOP STOP]: ").lower()
            if Cartography == "y":
                print("\nCARTOGRAPHER: Ah, yes! A great map, but why would you go to the ruins?")
                sleep(sec)
                print("\nCARTOGRAPHER: —uh, pay that question no mind! Here is the map, and I wish you the best of luck!")
                has_map = 1
                shop_stops -= 1
                sleep(sec)
                print("\nYou got the MAP!\n")
            else:
                print("\nCARTOGRAPHER: You sure? You think you can find the way just fine? Well, alright little man! Cya later!")
            sleep(sec)
            os.system('cls' if os.name == 'nt' else 'clear')

        # ---------- BUTCHER ---------- #
        elif choice1 == "3":
            if rations > 0:
                print("\nYou already have enough rations for your trip.")
                sleep(sec)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            print("\nYou wander over to the butcher shop, lured by the scent of cured ham. A gruff man\n"
                  "slaves away at his stand, focused as ever on perfecting his slices.")
            sleep(sec)
            print("\nBUTCHER GUY: Yo, small metal man, lookin' for quality cuts for the journey? No one gets far\n"
                  "without a proper meal!")
            sleep(sec)
            butcher = input("\nDo you want rations? [y/any key] [WILL EXHAUST A SHOP STOP]: ").lower()
            if butcher == "y":
                print("\nBUTCHER GUY: Wise choice, mate! No starving out there, little man!")
                rations = 3
                shop_stops -= 1
                print("\nYou got the RATIONS! [Three uses]")
            else:
                print("\nBUTCHER GUY: If you plan to hunt with your current weapons, I wish you luck!")
            sleep(sec)

        # ---------- PUB ---------- #
        elif choice1 == "4":
            if Rogue == 1 or Chef == 1:
                print(f"\n{Ally}: Seriously? I think I'm enough, don't go back in there...")
                sleep(sec)
                continue

            print("\nYou end up getting stuck in the crowd of the pub. After you find some space, two individuals pique\n"
                  "your interest.")
            sleep(sec)
            print("\nYou can see a hooded figure leaning against the far wall, and a short, noisy chef trying\n"
                  "to convince a group to hire him.")
            sleep(sec)

            hire = input("\nWho do you wanna talk to? [1. Chef,  2. Rogue,  3. Leave]: ")

            # Chef path
            if hire == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nYou shout at the top of your lungs to get the short guys attention. He jumps off a table and pleads to you.")
                sleep(sec)
                print("\n???: O' please, sir knight! I'va been lookin' for someone to take me in! How do people not need a good cook in their quest!?")
                sleep(sec)
                cook = input("\nTake him into your party? [y/any key] [WILL EXHAUST A SHOP STOP]: ").lower()
                if cook == "y":
                    Chef = 1
                    Ally = "TONIO"
                    print(f"\n{Ally}: Many thanks to you, sir knight! If you have any meals you wish to prep, make great use of my culinary abilities!")
                    sleep(sec)
                    print(f"\n{Ally}: And your name is... {Player_Name}? Wonderfully picked! I'ma still call you sir knight though... I Hope you don't mind!")
                    sleep(sec)
                    print(f"\nYou hired {Ally} the Chef!")
                    shop_stops -= 1
                else:
                    print("\nCHEF: Good grief! I gotta change my approach!")
                sleep(sec)
                

            # Rogue path
            elif hire == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nYou swim through the sea of people and make it to the hooded figure in the corner. The voice of a woman breaks the silence...")
                sleep(sec)
                print("???: ... Hey... Did you need something?")
                rogue = input("\nHire the rogue? [y/any key] [WILL EXHAUST A SHOP STOP]: ").lower()
                if rogue == "y":
                    Rogue = 1
                    Ally = "KANRA"
                    print(f"\n{Ally}: You want me for a quest? I've been looking for something to do... Thanks.")
                    sleep(sec)
                    print(f"\n{Ally}: Someone told me your name is {Player_Name}. Yeah, gotta say it suits you. Let's get going.")
                    print(f"\nYou hired {Ally} the Rogue!")
                    shop_stops -= 1
                else:
                    print("\n???: ...You seem to trust yourself, or maybe you lack trust in me. Shouldn’t be surprised...")
                sleep(sec)
            else:
                print("\nYou changed your mind. The crowd here is kind of strange.")
                sleep(sec)
        else:
            print("\nThat’s not a valid choice.")

    # ---------- POST-SHOP DECISION ---------- #
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n---\nAfter getting what you would call the necessities, you notice the sun begins to sink below the horizon. Since you see that the road\n"
          "ahead leads to Wood Woods, You think to yourself...\n")
    sleep(sec)
    sleep_or_embark = input("Should I embark or rest until morning? [1. REST,  2. EMBARK]: ")

    if sleep_or_embark == "1":
        print("\nYou decide that it's probably best to tackle the forest in the daylight. You stay in the nearby inn.")
        if Ally != "To be decided":
            print(f"\nAfter the sun rises, you wake up {Ally} and pack up your little camp on the outskirts of town. Your adventure truly begins!")
        else:
            print(f"\nAfter the sun rises over the horizon, you awaken, pack up, and begin your quest!")
        input("Press any key to proceed: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        wood_woods_day_choice()
    else:
        print("\nThe blacksmith's princess cannot wait! We must make haste! This darkness is nothing!")
        if Rogue == 1 or Chef == 1:
            print(f"\nYou and {Ally} make your way into the forest. Your silhouettes slowly sink into the darkness...")
        else:
            print("\nYou summon your courage and press on into the dark of the woods alone.")
        input("Press any key to proceed: ")
        wood_woods_night()

    # Return necessary variables (May be redundant now)
    if Ally != "To be decided":
        if Rogue == 1:
            return Rogue, sword, has_map, rations
        elif Chef == 1:
            return Chef, sword, has_map, rations
    else:
        return sword, has_map, rations


# Make choice Map/Trail
def wood_woods_day_choice():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")

    # Title
    print(utils.UnderLN("\nWood Woods"))
    sleep(sec)
    # If you have a map, this gets to run.
    if has_map == 1:
        print("\nYou pull out the map that you got from the cartographer and think to yourself...")
        choice = int(input("Use your map or follow trail?: [1: Map / 2: Off Trail]: "))
        if choice == 1:
            print("\nYou decide that it would be foolish to even consider going outside the map's directions and follow it's directions.")
            sleep(sec)
            proceed = input("\nPress anything to proceed: ")
            wood_woods_day_has_map()
        elif choice == 2:
            print("You decide to see where the off-roads take you.")
            sleep(sec)
            proceed = input("\nPress anything to proceed: ")
            wood_woods_day_trail()
    else:
        # This runs if you don't have a map.
        print("\nSince there was no obvious path and you have no map, you decided to just keep moving into the forest blindly...")
        sleep(sec)
        proceed = ("\nPress anything to proceed: ")
        wood_woods_day_trail()
    
# Starting Wood Woods with a map
def wood_woods_day_has_map():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")
    
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
    choice1 = int(input("What do you do? [1: Push him over / 2: Push him over]: "))
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
    proceed = input("\nPress anything to proceed: ")
    cave()

# Start of Wood Woods
def wood_woods_day_trail():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("As you walk amongst the forest aimlessly, you find a nice looking stick and think about"
          " how you may need a torch if it gets dark out. You found some space for it in your pack and"
          " kept on your merry way.")
    # You got a stick!
    Stick = 1
    sleep(sec)
    print("\nHours have passed, none you have kept track of, but suddenly, stifling the peace is a growl"
          " of a large creature...")
    sleep(sec)
    wood_woods_lumberjack(lives) 

# Initiate the lumberjack
def wood_woods_lumberjack(lives):
    global sword, has_map, rations, Rogue, Chef, Ally, Player_Name, sec, Stick, Neck_Cloth
    os.system('cls' if os.name == 'nt' else 'clear')

    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")

    # If you have the rogue:
    if Rogue == 1:
        print(f"\n{Ally}: Hey, {Player_Name}, that isn't a monster behind those shrubs... It's a man. I'll let you decide how we play this out.")

    sleep(sec)
    choice = int(input("\nWhatever it is, it hasn't noticed you... How should you proceed? [1. Investigate / 2. Sneak away / 3. Throw your stick at it]: "))
    # Investigate the noise.
    if choice == 1:
        print("\nYou decide that you need to see what this is. Your armor should hold you up fine if it comes down to a fight.")
        sleep(sec)
        print("You breathe in... and then out, and swipe the brush away, and...")
        sleep(sec)
        print("\nCRASH!")
        sleep(sec)
        print("\nThe tree ahead hammers the earth right in front of you. The grunting is from no beast, but rather a hulking man in plaid;"
              " A lumber jack!")
        sleep(sec)
        print("\nLUMBERJACK: Stubborn pine! took ye long enough to come down!")
        sleep(sec)
        print("\nHe turns around to fell the next pine and sees your small frame, fixated on the fallen tree.")
        sleep(sec)
        wood_woods_lumberjack_intro()
        
    # Sneak by the creature.
    if choice == 2:
        if Rogue == 1:
            print("You decide not to draw attention to yourself. Who knows if this guy is truly trustworthy. Let's just not bother...")
            sleep(sec)
        else:
            print("You decide it's best not to play with fire. No need to make any silly decisions when your full focus should be to your quest.")
            sleep(sec)
    
    # Throw your stick at the sound!
    if choice == 3:
        print("\nYour intrusive thoughts get the better of you. You take out the stick from your pack and stare at it for a moment.")
        sleep(sec)
        print("You throw it straight past the bush and you here a momentarily satisfying thunk.")
        sleep(sec)
        print("\n???: OW! the hell!?")
        sleep(sec)
        print("\nA huge, plaid, burly man jumps out of the bush on all-fours. He looks very irritated.")
        sleep(sec)
        print("\nYou begin to panick. In the breif moment of thought that you have, you...\n")
        sleep(sec)
        if sword == 1:
            choice4 = int(input("[1. or 2. Don't Fight / 3. Fight]: "))
            if choice4 == 3:
                # Draw your sword
                print("\nYou reach for your blade in a hurry and try to find a stance to fight.")
                sleep(sec)
                print("Without a chance to think, he swings his axe sideways!")
                sleep(sec)
                while True:
                    chance = chance_50()
                    if chance == 1:
                        print("\nYou manage to duck quickly and strike the hulking man in the temple with the pommel of your sword.")
                        sleep(sec)
                        print("He slides against the forest floor five feet behind you, out cold. You breathe a sigh of relief.")
                        sleep(sec)
                        break
                    else:
                        print("\nWHACK!")
                        lives -= 1
                        sleep(sec)
                        print(f"\nHe struck you in the side for a chunk of your life! You hit the ground hard, wheezing.")
                        print(f"HEALTH REMAINING: {lives}/3")
                        sleep(sec)
                        if lives <= 0:
                            print("\nYou were struck too many times... You tried to reach for your sword in with your last breath, but you felt a strong grip grab the back of your armor.")
                            sleep(sec)
                            print("\nBefore you could stop the brute, a strong punch bent through your armor and...\neverything went black...")
                            sleep(sec)
                            game_over()
                        else:
                            print("As you attempt to get up, he bounds toward you again!")
                            sleep(sec)
                            continue
                    
                # if Chef is in your party
                try:
                    if Chef == 1:
                        print(f"\n{Ally}: Scary fight, sir knight, {Player_Name}, glad you made it in one piece...")
                        print(f"\n{Ally}: Take this real quick! It's a salve, something my mama came up with!")
                        if lives < 3:
                            lives += 1
                        print("\nIt's a hastily put together first-aid kit. It's convenient but we've already lost our ally... Dang it...")
                        print(f"HEALTH REMAINING: {lives}/3")
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
    global sword, has_map, rations, Rogue, Chef, Ally, Player_Name, sec, Stick, Neck_Cloth
    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")
    
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
    if has_map == 1:
        print("Say little man, you need any pointers for these parts? I do live here.")
        choice3 = int(input("\n[1. Yeah, can you read my map! / 2. I'm ok, thanks!]"))
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
    global sword, has_map, rations, Rogue, Chef, Ally, Player_Name, sec, Stick, Neck_Cloth
    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")
    
    print(utils.UnderLN("\nWood Woods"))
    sleep(sec)
    print("It's dark out. Very dark out, but nonetheless your spirits remain high. As far as you can see, it's just tall trees\n"
          "and ever-spanning hills. One of these directions leads to the cave you heard about. Supposedly, through the cave is the\n"
          "way to the ruins. You've got no choice but to follow that tip for right now, since anything could happen to Ivar's daughter.\n")
    sleep(sec)
    if has_map == 1:
        print("\nUnfortuantely, you can't see the contents of your map... If only you had some kind of light.")
    else:
        print("\nEven if you had a map, it's too dark to see it.")
    sleep(sec)
    if Stick != 1:
        print("Amidst your walking, you stumble upon a nice stick. You manage to find room in\n"
              "your bag for it and stash it away.")
    sleep(sec)
    print("\nGiven it's night, it might not be a bad idea to light your torch. You could use your neck scarf\n"
          "to add kindling to the stick... but you would lose it.")
    # Make a torch spending your only neck scarf
    choice = int(input("\nMake and set a torch alight? [1. Yes / 2. No ][ Uses Neck Scarf]: "))
    if choice == 1:
        Neck_Cloth = 0
        print("\nNot being able to see would hinder your ability to navigate. Why try to get through this\n"
              "darkness when you have this opportunity?")
        sleep(sec)
        proceed = ("\nPress anything to proceed: ")
        wood_woods_night_torch()
    else:
        print("\nYou trust your gut. You believe that you can navigate through these woods with your internal\n"
              "compass. You steady yourself and then press forward.")
        sleep(sec)
        proceed = ("\nPress anything to proceed: ")
        wood_woods_night_dark()

def wood_woods_night_torch ():
    os.system('cls')
    print("COMING SOON")

def wood_woods_night_dark ():
    os.system('cls')
    print("COMING SOON")

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

def game_over():
    utils.title("YOU HAVE FALLEN...")
    os._exit()