from time import sleep
import sys

name = ""
wisdom= 0 
strength= 0
dexterity= 0
health = 2
# Initialise stats

score = 2
ans = 0
# Used for puzzles

hasphone = 0
# Used if they pick up the phone

speed = 0.05
# Used for the speed of the typewriter effect

def type(lines): # This function replaces 'print', input must be a list for it to print correctly
    global speed
    print("")
    for line in lines:          # for each line of text (or each message)
        for c in line:          # for each character in each line
            print(c, end='')    # print a single character, and keep the cursor there.
            sys.stdout.flush()  # flush the buffer
            sleep(speed)         # wait a little to make the effect look good.
        print('')

def typefast(lines): # This function is used exclusively to type banners quickly
    print("")
    for line in lines:          # for each line of text (or each message)
        for c in line:          # for each character in each line
            print(c, end='')    # print a single character, and keep the cursor there.
            sys.stdout.flush()  # flush the buffer
            sleep(0.001)         # wait a little to make the effect look good.
        print('')

def intro(): # sets text speed, gives the introduction, asks them for their name and if they want to start the game
    global name
    global speed
    global wisdom
    global strength
    global dexterity
    global health

    type(["How fast do you want text to appear?"])
    type(["1: Normal"])
    speed = 0.1
    type(["2: Slow"])
    speed = 0.03
    type(["3: Fast"])
    speed = 0.01
    type(["4: VERY Fast"])
    choice = input(">> ")
    if choice == "2": # set the text speed to slow
        speed = 0.1
        type(["Setting text speed to slow..."])
    elif choice == "3": # set the text speed to fast
        speed = 0.03
        type(["Setting text speed to fast..."])
    elif choice == "4": # set the text speed to very fast (thinking of naming this programmer mode)
        speed = 0.01
        type(["Setting text speed to very fast..."])
    else: # normal or no answer given, set to default which is normal speed
        speed = 0.05
        type(["Setting text speed to default (normal)..."])

    type(["You awaken in a dark and shadowy forest, your head pounding, a knife in your hand and something around your neck.", 
    "Your mind is in a haze, only remembering faint glimpses of what led you here, you had gone backpacking in Australia after hearing about the beautiful 'forest of lost souls', that had become quite the tourist attraction.",
    "You arrived at this beautiful forest, being welcomed by it's lucious embrace, you entered... and that's the last memory you have before waking up.",
    "\"What's my name?! I don't remember\""])

    name = (input(">> ").strip().lower())

    if name == "demi" or name == "yasir": # if you are our lord and saviour Demi or Yasir
        strength = 10
        wisdom = 10
        dexterity = 10
        health = 10
        type([f"{name.upper()}, YOU ARE THE CHOSEN ONE...",
        "-- M A X I M U M  S T A T S  U N L O C K E D --"])
    else:
        type([f"\"Yes now I remember! My name is {name.capitalize()}!\""])

    type(["You only just about remember your name, as you awaken the beautiful facade has faded and left you in a gloomy, cold, depreciated forest with a threatening aura.",
    "Twisted trees, a viscous fog that blocks your vision, and horrific sounds of screeching and pain surrounding you.",
    "As you stand up you feel a twinge in your leg, there's some light bruising and a small cut which has been roughly dressed.",
    "It's clear that you've been in some kind of fight, which means that you're not alone here...",
    "You need to get out of here fast if you ever have a chance of leaving..."])

    typefast([" ,--,--'.        .-,--'                .              ,           .    .---.         .     ",
          " `- |   |-. ,-.   \|__ ,-. ,-. ,-. ,-. |-   ,-. ,\"    )   ,-. ,-. |-   \___  ,-. . . |  ,-.",
          "  , |   | | |-'    |   | | |   |-' `-. |    | | |-   /    | | `-. |        \ | | | | |  `-.",
          "  `-'   ' ' `-'   `'   `-' '   `-' `-' `'   `-' |    `--' `-' `-' `'   `---' `-' `-^ `' `-'",
          "                                                '"])

    type(["Start game?", "1: Yes", "2: No"])
    start_game(input(">> "))

# print("""You start with zero wisdom points, zero dexterity points and zero strength points. 
# You need to increase your points to be able to overcome obstacles and escape the haunted forest""")

def start_game(answer): # Start of the game
    if answer == "2": # if they say no, exit game
        type(["Goodbye..."])
        exit()
    elif answer == "1": # if they say yes present them with the first choice
        type(["You are presented with two pathways...", "The left side looks like an off-shoot, almost no definition to the path, it's covered in foliage.", "The right path that appears heavily used, the trees are somewhat curved away to allow passage."])
        type(["Which path do you take?", "1: Left", "2: Right"])
        choice(input(">> "))
    else: # loop until they give a valid answer
        type(["Please pick 1 or 2."])
        start_game(input(">> "))

def choice(answer): # first choice, left or right
    if answer == "1": # left path, presents you with the choice of the first puzzle
        type(["You take the left path because it appears less populated and therefore safer.", "A figure pours from the darkness, his sharp fangs and pale flesh gleaming even in this poor light.",
        "You are gripped by his cold and mesmerising gaze"])
        type(["\"I have lost a fine vintage of blood somewhere nearby, if you cannot find my fine blood, I will drain yours in it's place...\""])
        type(["What would you like to do?", "1: Help them find their blood", "2: Try to run away"])
        choice_1(input(">> "))
    elif answer== "2": # right path, presents you with the choice of the first fight
        type(["You take the beaten path, it beckons you with the call of combat.", "You draw your knife, testing the edge, this could come in handy for wild animals.", "Amongst other things..."])
        type(["After travelling a little while you see something up ahead, it's a pack of wolves, hungrily scenting the air.", "They look tough, but half-starved..."])
        type(["What do you do?", "1: Run away very quickly", "2: Approach them and fight"])
        choice_2(input(">> "))
    else: # loop until they give a valid answer
        type(["Please pick 1 or 2."])
        choice(input(">> "))

def attempt(): # used to track attempts in puzzle 1
    global score
    score -= 1
    if score != 0: #if they have attempts remaining, tell them how many
        type([f"{score} attempts remaining."])
    else: # if they have no attempts left, kill them
        type(["The undead monster seizes you in an iron embrace and drains the blood coursing through your veins. If your lucky, you are dead by now..."])
        loss()
        
def question_A1(answer): # first question of the first puzzle
    if answer == "1" or answer == "2": # incorrect, mark an attempt and try again
        attempt()
        type(["You find nothing, try again."])
        question_A1(input(">> "))
    elif answer == "3": # correct, move on
        type(["You find three bottles...", f"Which do you give to the monster? ({score} attempts remaining).", "1: A faintly clear and refreshing odour comes from the contents in this bottle", "2: A metallic, coppery odour pervades this bottle, it turns the stomach", "3: A sweet and fruity scent emanates from this bottle"])
    else: # loop until they give a valid answer
        type(["That isn't an option, try again."])
        question_A1(input(">> "))

def question_A2(answer): # second question of the first puzzle
    if answer == "1" or answer == "3": # incorrect, mark an attempt and try again
        attempt()
        type(["Wrong answer. try again."])
        question_A2(input(">> "))
    elif answer == "2": # correct, move on
        type(["You placate the undead monster and slip away whilst he savours some poor souls blood. Blood you found for him...", "You continue on the path, questioning what on earth could appear next.",
        "You feel your wisdom increase..."])
    else: # loop until they give a valid answer
        type(["That isn't an option. try again."])
        question_A2(input(">> "))

def choice_1(answer): # puzzle A (first puzzle)
    
    if answer == "2": #running away towards the right path (first fight)
        global dexterity 
        dexterity+= 1
        type(["You flee before you can even tell what this monstrous beast is, you escape barely but alive and find yourself on the right path.", "You feel your dexterity increase..."])
        type(["After running for a while you see something up ahead, it's a pack of wolves, hungrily scenting the air.", "They look tough, but half-starved..."])
        type(["What do you do?", "1: Run away very quickly", "2: Approach them and fight"])
        choice_2(input(">> "))
    elif answer == "1": # begins the first puzzle, if they complete it add wisdom and present them with the choice of the second puzzle 
        global score
        global wisdom
        # global strength
        type([f"You have {score} attempts to complete this.", "Where would you like to begin your search?", "1: Around the tree", "2: Behind the rock", "3: Under the leaves"])
        question_A1(input(">> "))
        question_A2(input(">> "))
        wisdom+= 1
        # strength+= 1
        # I though adding strength would be good as you need at least one strength point to fight the person at the end.
        type(["An old, but not at all frail woman appears before you, her yellow bloodshot eyes glowing with a terrible power."])
        type(["\"This is my dominion, Human, if you answer my questions you will leave alive, if you get more wrong than right, I will use your innards for potion ingredients!\""])
        type(["What would you like to do?", "1: Answer her questions", "2: Try to run away"])
        choice_3(input(">> "))
    else: # loop until they give a valid answer
        type(["Please pick 1 or 2."])
        choice_1(input(">> "))

def tally(point): # keeps a tally of correct answers
    global ans
    ans += point

def question_B1(answer): # second puzzle first question
    if answer == "1": # wrong, move on
        type(["\"Close, but not quite good enough...\""])
    elif answer == "2": # wrong, move on
        type(["\"You fool, they walk no other way!\""])
    elif answer == "3": # correct, + 1 tally
        type(["\"A lucky guess, I'm sure.\""])
        tally(1)
    else: # loop until they give a valid answer
        type(["\"There are 3 answers only, DO NOT TEST ME MORTAL!\""])
        question_B1(input(">> "))
    
def question_B2(answer): # second puzzle second question
    if answer == "1": # wrong, move on
        type(["A hedgehog would fare better than you!"])
    elif answer == "2": # correct, + 1 tally
        type(["You're bright, for one of such limited experience..."])
        tally(1)
    elif answer == "3": # wrong, move on
        type(["Wrong part of the day, or night as it were..."])
    else: # loop until they give a valid answer
        type(["\"There are 3 answers only, DO NOT TEST ME MORTAL!\""])
        question_B2(input(">> "))
    
def question_B3(answer): # second puzzle third question
    if answer == "1": # correct, + 1 tally
        type(["You actually got that one, how infuriating of you..."])
        tally(1)
    elif answer == "2": # wrong, move on
        type(["You're dense as one with an answers like that!"])
    elif answer == "3": # wrong, move on
        type(["Not quite good enough!"])
    else: # loop until they give a valid answer
        type(["\"There are 3 answers only, DO NOT TEST ME MORTAL!\""])
        question_B3(input(">> "))

def questions(): # asks the second puzzles 3 questions in order
    type(["Which of these animals does not walk on two legs?", "1: Bear", "2: Chicken", "3: Tiger"])
    question_B1(input(">> "))

    type(["I am famed for my ability to illuminate the darkness, I control the tides of the seven seas, what am I?", "1: A Hedgehog", "2: The Moon", "3: The Sun"])
    question_B2(input(">> "))

    type(["I give life yet have none of my ownm, if you consume a little of me every day you live long, if you are consumed by me you will die, what am I?", "1: Water", "2: Trees", "3: Fire"])
    question_B3(input(">> "))
    
def choice_3(answer): # puzzle B (second puzzle)
    if answer == "1": # answer her questions, depending on outcome grants passage to the gate and stranger choice
        global wisdom
        global ans
        questions()
        if ans == 3: # 3/3 grants you passage and wisdom
            wisdom+=1
            type(["The foul witch darts forward, inches from your face."])
            type(["\"You win your freedom and all that goes with it, worthless human NOW LEAVE ME!\""])
            type(["You run, feeling glad to be away from her at last", "You feel your wisdom increase..."])
        elif ans == 2: # 2/3 grants passage but not wisdom
            type(["The withes face contorts in rage."])
            type(["\"Not enough RIGHT ANSWERS!\""])
            type(["You turn to run as fast and as far away as possible, never more grateful for your organs as you escape with them."])
        elif ans == 1: # 1/3 death
            type(["She calmly smiles, in an almost sickening manner"])
            type(["\"You may keep your innards, but I always wanted a pet rat!\""])
            type(["She gestures and your limbs, body, your entire being contracts and warps into that of a rat.", "You will never leave..."])
            loss()
        else: # 0/3 death
            type(["The witch points at you and your limbs are immobilised, but you still feel as her long, sharp fingernails dig into your stomach.", "This will hurt..."])
            loss()
        type(["You aimlessly pursue further into the forest, you discover a large metal gate that looks to be an exit!",
        "As you approach the gate, a man beckons to you, asking you to help hold the gate for him to get through."])
        type(["\"Please help me! If you do, I'll hold it for you too so we can both get out of here!\""])
        type(["What do you do?", "1: Help him", "2: Fight him", "3: Run away"])
        choice_4(input(">> "))
    elif answer == "2": # running away, gives dexterity and leads to the gate and stranger choice
        global dexterity
        dexterity+=1
        type(["You narrowly dodge her gnarled fingers, terrible crashing sounds resounding amongst the tree limbs but you emerge near a gate.",
        "You feel your dexterity increase..."])
        type(["There's a man standing infront of the gate, somehwat in a panic.",
        "As you approach the gate, a man beckons to you, asking you to help hold the gate for him to get through."])
        type(["\"Please help me! If you do, I'll hold it for you too so we can both get out of here!\""])
        type(["What do you do?", "1: Help him", "2: Fight him", "3: Abandon him"])
        choice_4(input(">> "))
    else: # loop until they give a valid answer
        type(["Please pick 1 or 2."])
        choice_3(input(">> "))

def choice_4(answer): # the gate and the stranger you can help or fight
    global wisdom
    global strength
    global hasphone
    if answer == "1" and wisdom <2: #help him when not wise, death
        type(["You agree to help the man in return for your escape, he seems overjoyed.",
        "As you are holding the gate, you feel a searing pain, the man you were helping just stabbed you in the back and you bleed to death..."])
        loss()
    elif answer == "2" and strength >1: #fight when strong, win
        type(["You approach the stranger completely unphased, you aren't fooled by his presence and draw your weapon.",
        "The stranger clumsily swings a knife at you, but you dodge easily and bury your dagger in his ribs.", "He should have chosen an easier target..."])
        type(["After you deal with the stranger, the gate appears tall and heavy but is exceptionally easy to move.",
        "You press onto the gate and without hesitation run towards the faint amber glow of a street lamp, you have escaped!"])
        victory()
    elif answer == "2" and strength <2: #fight when not strong enough, death
        type(["Somewhat perturbed, you remember what you've witnessed in this forest, nothing's is ever this easy.", "Not wanting to be caught offguard, you hesitantly make the first strike"])
        type(["He see's the punch coming a mile off, slips to the side and laughs, driving a knife deep into your gut.", "This will not be a quick death..."])
        loss()
    elif answer == "3": # run away to the random path choice that leads to the shore, edge or death
        if wisdom >1: # running with wisdom, you get some flavour text
            type(["Using your wisdom, you trust your judgement and dart off before he has chance to react.", "You hear some distant yelling, but he's long gone, you successfully escaped the encounter."])
            type(["You continue running until you arrive at a the paths end, you are surrounded by trees and the path from which you came."])
        else: # no wisdom, no flavour text
            type(["You choose to not trust the complete stranger you found in a forest of awful things, and begin moving away."])
            type(["\"NO PLEASE DON'T LEA... Ha.. haha, g- g- get baCK HERE!\""])
            type(["He begins to chase you with haste, his eyes blood red and knife in hand, but you're too fast for him.",
            "You continue running until you arrive at a the paths end, you are surrounded by trees and the path from which you came."])
        if hasphone == 1: # if you have the phone you have unobscured options
            type(["You've been here before! You use the phone to choose your next route"])
            type(["Where do you go?", "1: To the shoreline", "2: A dead end", "3: To the forest edge", "4: Back the way you came"])
        elif wisdom >1: # if you have wisdom you know some options
            type(["Using your hearing, you can hear the faint wooshing of a shoreline, the cry of the water bird beckons you.", "You can also pick up on some faint sounds of cars, civilization, this could be the way out!"])
            type(["Which way?", "1: Towards the shoreline", "2: ???", "3: Towards civilization", "4: Back the way you came"])
        else: # no phone or wisdom, random options
            type(["With no indication of where to go, this is a gamble."])
            type(["Which way?", "1: ???", "2: ???", "3: ???", "4: Back the way you came"])
        hasphone = 0
        choice_6(input(">> "))
    elif answer == "1" and wisdom >1: # helping when wise, lets you reasess, you can make the same choices with some flavour text
        type(["As you move closer, you see dark red drops on his cuff and a knife handle in his belt.", "Knowing this, you should choose your next move wisely..."])
        type(["What would you like to do?", "1: Help him", "2: Fight him", "3: Run away"])
        choice = input(">> ")
        if choice == "1": #helping AGAIN when wise
            type(["Even knowing the risks, you agree to help the man in return for your escape, he seems overjoyed.",
            "You're a kind soul who still believes in the duty to help those in need, without judgement."])
            type(["... maybe you should have judged this person a bit harder.", "As you are holding the gate, you feel a searing pain, the man you were helping just stabbed you in the back and you bleed to death..."])
            loss()
        else: # catches the other 2 choices and any non valid inputs
            choice_4(choice)
    else: # loop until a valid input is reached
        type(["Please pick 1, 2 or 3."])
        choice_4(input(">> "))

def choice_2(answer): # the right path, this is the first fight
    global dexterity
    if answer == "1": # choosing to run left towards puzzle B (second puzzle)
        dexterity+= 1
        type(["You manage to escape whilst they hunt in a confused frenzy, chasing the scent not the person.", "You run for what feels like forever, but upon turning around you can see that they haven't chased you, safety at last.",
        "You feel your dexterity increase..."])
        type(["But upon looking forwards again, an old, but not at all frail woman appears before you, her yellow bloodshot eyes glowing with a terrible power."])
        type(["\"This is my dominion, Human, if you answer my questions you will leave alive, if you get more wrong than right, I will use your innards for potion ingredients!\""])
        type(["What would you like to do?", "1: Answer her questions", "2: Try to run away"])
        choice_3(input(">> "))
    elif answer == "2": # choosing to fight the first fight
        type(["As you approach them, brandishing your blade, one of the wolves charges you..."])
        type(["What do you do?", "1: Stab the stomach", "2: Go for the eyes", "3: Stab the heart", "4: Dodge away"])
        fight_1(input(">> "))
        #randomise death or I have allowed the player to choose where to hit to win below (i put this in a function)
        type(["Further along the path you see a number of shadows hunched over something, then realise it is a man.", "These ghastly figures haven't noticed you, but they will kill him unless you intervene.", "Upon approaching these ghouls, your amulet begins to glow."])
        type(["What do you do?", "1: Fight them and save him", "2: Leave him to his fate and run", "3: Use your amulet"])
        choice_5(input(">> "))
    else: # loop until a valid answer is given
        type(["Please pick 1, or 2."])
        choice_2(input(">> "))

def fight_1(answer):
    global strength
    global health
    if answer == "3": # the heart results in the quickest death, + strength
        type(["As the wolf charges, you bring the blade up underneath with precision, piercing it's heart",
        "The remaining wolves appear threatened by your first kill, and choose to run away.", "They got a bigger meal than they could handle this time."])
        strength+= 1
        type(["You feel your strength increase..."])
    elif answer == "2": # complete miss, death
        type(["As the wolf charges you aim straight for the eyes, resulting in an unfortunate swing and a miss.",
        "This allows the wolf to pounce upon your chest, tearing you open, quickly alerting the others to this fresh meal."])
        type(["The wolves ravenously feast upon you, until you mercifully fade from this life."])
        loss()
    elif answer == "1": # gets the kill but loses a life, + strength
        type(["As the wolf charges you swing your knife directly into it's side, breaking a rib and puncturing the stomach.", "The wolf retaliates by clamping down on your arm with force, generating such incredible pain, but you feel the wolfs jaw relax as he dies.",
        "The remaining wolves appear threatened by your first kill, and choose to run away.", "They got a bigger meal than they could handle this time."])
        strength+= 1
        health-= 1
        type(["You feel your strength increase, but you have sustained some damage..."])
    elif answer == "4": # not smart and results in death
        type(["As the wolf charges you dodge out of the way, successfully avoiding the beast and landing to the side.",
        "As you land just infront of the bushes, you hear panting, snarling, and suddenly see a set of eyes!", "Without time to react this wolf quickly goes for the neck, ripping it out."])
        type(["You can't even scream for help as your body is torn limb from limb."])
        loss()
    else: # loop until a valid answer is given
        type(["Please pick 1, 2, 3 or 4."])
        fight_1(input(">> "))

def fight_2(answer):
    global strength
    global health
    if answer == "4": # best answer, + strength
        type(["As it lunges forward you tuck to the side, this opens the creature up to a strike from behind which eliminates the ghostly foe.",
        "The remaining shadows have disappeared, leaving the man behind."])
        strength+= 1
        type(["You feel your strength increase..."])
    elif answer == "2": # death
        type(["As it lunges forward you hold the dagger out and stab it in the chest, the ghostly form encompases you.", 
        "The ghouls feed on both of you, slowly drawing the very life out of you until you are both shrivelled husks."])
        loss()
    elif answer == "1" and health >1: # mid answer, + strength but lose a life
        type(["As it lunges forward you swing the dagger at it's head, you take some ghostly damage to the swinging arm but the shadow disipates.",
        "The remaining shadows have disappeared, leaving the man behind."])
        strength+= 1
        health-= 1
        type(["You feel your strength increase, but you have sustained some damage..."])
    elif answer == "1" and health <2: # mid answer when low on health, death
        type(["As it lunges forward you swing the dagger at it's head, you take some ghostly damage to the swinging arm but the shadow disipates.",
        "The remaining shadows have disappeared, leaving the man behind."])
        type(["Before you talk to him, your body feels limp, it seems as a result from your earlier injuries, this damage is irrepairable.",
        "Your soul starts leaving your body, you collapse onto the ground"])
        type(["You lie there, an empty, soulless husk."])
        loss()
    elif answer == "3": # death
        type(["As it lunges forward you duck underneath, the ghostly form encompases you.", 
        "The ghouls feed on both of you, slowly drawing the very life out of you until you are both shrivelled husks."])
        loss()
    else: # loop until a valid answer is given
        type(["Please pick 1, 2, 3 or 4."])
        fight_2(input(">> "))

def choice_5(answer): #The right path, this is the second fight
    global hasphone
    global dexterity
    global wisdom
    if answer == "3": # Use the amulet, get the phone and wisdom
        hasphone = 1
        wisdom+= 1
        type(["The amulet suddenly emits a painfully bright burst of light, reducing the accursed monsters to naught but ashes.", "You feel your wisdom increase...",
        "The man attempts to thank you, but his voice is almost silent, his skin is grey, he breaths his last breath before passing you something in his hand, it's a phone!"])
        type(["What number do you call?"])
        phone = input(">> ")
        if phone == "000": # correct number, win
            type(["You key in the number for the Australian emergency services and manage to arrange a rescue.",
            "You are actually free from this foul and unending nightmare! Though perhaps not the memories or the knowledge of what you have seen.", "That lasts forever..."])
            victory()
        else: # incorrect, continue
            type(["You hear a tone... this number is unreachable and that's the last of the phones credit!",
            "Even so, the phone does have a map and a light, these could still be invaluable in finding a way out of this place.",
            "Inspecting the map on the phone gives you multiple routes to take from here..."])
            type(["Where do you go?", "1: To the shoreline", "2: A dead end", "3: To the forest edge", "4: To the gate"])
            choice_6(input(">> "))
    elif answer == "2": # running away to the gate and stranger
        type(["The man calls for help but you don’t know if your mere steel will be enough to overcome these living shadows or not.",
        "You escape to the best of your abilities, life can be cruel.", "You feel your dexterity increase..."])
        dexterity+= 1
        type(["You emerge near a gate, with a man standing before it.",
        "As you approach the gate, a man beckons to you, asking you to help hold the gate for him to get through."])
        type(["\"Please help me! If you do, I'll hold it for you too so we can both get out of here!\""])
        type(["What do you do?", "1: Help him", "2: Fight him", "3: Abandon him"])
        choice_4(input(">> "))
    elif answer == "1": # choosing to fight in the second fight
        type(["As you approach them, the ghastly figures notice you and make a lunge!"])
        type(["What do you do?", "1: Swing at the head", "2: Stab the chest", "3: Dodge under", "4: Dodge to the side"])
        fight_2(input(">> "))
        hasphone = 1
        type(["The man attempts to thank you, but his voice is almost silent, his skin is grey, he breaths his last breath before passing you something in his hand, it's a phone!"])
        type(["What number do you call?"])
        phone = input(">> ")
        if phone == "000": # correct number, win
            type(["You key in the number for the Australian emergency services and manage to arrange a rescue.",
            "You are actually free from this foul and unending nightmare! Though perhaps not the memories or the knowledge of what you have seen.", "That lasts forever..."])
            victory()
        else: # incorrect, continue
            type(["You hear a tone... this number is unreachable and that's the last of the phones credit!",
            "Even so, the phone does have a map and a light, these could still be invaluable in finding a way out of this place.",
            "Inspecting the map on the phone gives you multiple routes to take from here..."])
            type(["Where do you go?", "1: To the shoreline", "2: A dead end", "3: To the forest edge", "4: To the gate"])
            choice_6(input(">> "))
    else: # loop until a valid answer is given
        type(["Please pick 1, 2 or 3."])
        choice_5(input(">> "))

def choice_6(answer):
    global hasphone
    if answer == "1": # pathway to the shoreline
        type(["You follow this pathway until you end up at the shoreline.", "You see a small jetty with a slightly worn looking boat in the water."])
        type(["What do you do?", "1: Use the boat", "2: Attempt to swim"])
        shore(input(">> "))
    elif answer == "2": # leads to a dead end
        type(["You follow this pathway until you arrive at a dead end, you then hear a horrific shriek from behind you",
        "A banshee is now towering over you, you have no where to go."])
        type(["The last thing you hear is its dreaded cry as even your soul is taken from you..."])
        loss()
    elif answer == "3": # leads to the forest edge
        type(["You follow this pathway until you end up at the forest edge.", "You see a fence on the edge of the forest."])
        type(["What do you do?", "1: Try to jump the fence", "2: Leave the area"])
        edge(input(">> "))
    elif answer == "4" and hasphone == 1: # if they have the phone they are coming from a different path and haven't been to the gate yet
        type(["You follow this pathway until you end up at a sturdy looking gate.",
        "As you approach the gate, a man beckons to you, asking you to help hold the gate for him to get through."])
        type(["\"Please help me! If you do, I'll hold it for you too so we can both get out of here!\""])
        type(["What do you do?", "1: Help him", "2: Fight him", "3: Abandon him"])
        choice_4(input(">> "))
    elif answer == "4" and hasphone == 0: # no phone and have already been to the gate, meaning death
        type(["For some reason you go back the way you just came, the angry stranger guts you before you have time to think.",
        "As you bleed out, you think about how you ended up here..."])
        loss()
    else: # loop until a valid answer is given
        type(["Please pick 1, 2, 3 or 4."])
        choice_6(input(">> "))

def shore(answer):
    global wisdom
    if answer == "1" and wisdom >1: # boat with wisdom, win
        type(["You quickly get the basics and row to freedom.", "You have escaped!"])
        victory()
    elif answer == "1" and wisdom <2: # boat without wisdom, death
        type(["You forget untie the boat and rear portion snaps off.", "You drown, cursing your own foolishness."])
        loss()
    elif answer == "2": # swim away, foolish, die
        type(["You attempt to swim for the far side but the currents sweep you away.",
        "The current drags you over the edge of a waterfall, breaking bone and leaving your lifeless body to wash up on a beach somewhere."])
        loss()
    else: # loop until a valid answer is given
        type(["Please pick 1 or 2"])
        shore(input(">> "))

def edge(answer): # jump the fence or turn around
    global dexterity
    if answer == "1" and dexterity >1: # jump the fence with dex, win
        type(["You nimbly work your over the fence and out of that terrible place.", "You have escaped!"])
        victory()
    elif answer == "1" and dexterity <2: # jump the fence without dex, loss
        type(["You awkwardly attempt to climb the fence, but get one leg stuck and fall breaking the leg in the fence.", "Something evil will be with you shortly..."])
        loss()
    elif answer == "2": # turn around, die
        type(["You turn around to head to a different path, but then hear a horrific shriek from behind you",
        "A banshee is now towering over you, you have no where to go."])
        type(["The last thing you hear is its dreaded cry as even your soul is taken from you..."])
        loss()
    else: # loop until a valid answer is given
        type(["Please pick 1 or 2"])
        shore(input(">> "))

def victory(): # victory text and exit
    typefast(["                       .  .          .-,--.                       .                      ",
              " . , . , . , . , . ,   |  | ,-. . .   `\__  ,-. ,-. ,-. ,-. ,-. ,-|   . , . , . , . , . ,",
              " -X- -X- -X- -X- -X-   |  | | | | |    /    `-. |   ,-| | | |-' | |   -X- -X- -X- -X- -X-",
              " ' ` ' ` ' ` ' ` ' `   `--| `-' `-^   '`--' `-' `-' `-^ |-' `-' `-^   ' ` ' ` ' ` ' ` ' `",
              "                       .- |                             |                                ",
              "                       `--'                             '"])
    type([f"Congratulations {name.capitalize()}, you have won the game!", "Thanks for playing!"])
    exit()

def loss(): # loss text and exit
    typefast(["                           .  .           .-,--.          .                          ",
              " . , . , . , . , . , . ,   |  | ,-. . .   ' |   \ . ,-. ,-|   . , . , . , . , . , . ,",
              " -X- -X- -X- -X- -X- -X-   |  | | | | |   , |   / | |-' | |   -X- -X- -X- -X- -X- -X-",
              " ' ` ' ` ' ` ' ` ' ` ' `   `--| `-' `-^   `-^--'  ' `-' `-^   ' ` ' ` ' ` ' ` ' ` ' `",
              "                           .- |                                                      ",
              "                           `--'"])
    type([f"Sorry {name.capitalize()}, you have lost the game...", "Thanks for playing!"])
    exit()

intro()