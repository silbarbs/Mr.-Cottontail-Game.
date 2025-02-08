print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Mr. Cottontail game!")
print("Your mom has to work late and so does your dad, so your mom drops you off at Mr. Cottontail.")
print("RULES: 1- Never lie. 2- Never eat his food. 3- Always be polite.")
print('Mr. Cottontail decided to take you to the garden today. "Weeds, weeds everywhere! But we are not afraid of hard work, right? He says with a bright smile. In truth, you are a bit worried about getting stung by the tan nettles.')
firstchoice= input('What do you say? 1- "Of course not! Let\'s go!" 2- "I\'m not afraid of hard work, but I\'m a bit worried about the nettles..." 3- "Those nettles scare me! Why are they so tall?!"')
if firstchoice== "1":
    print("Mr. Cottontail looks deeply into your eyes and senses your hasitation. Nothing angers him more than a lie...game over.")
elif firstchoice== "2":
    print('Mr. Cottontail removes his gloves and hands them to you. "They\'re a bit worn out, but they\'ll still protect you from stings. Before pulling weeds, let\'s find the snails hiding in the moist grass. Count how many you gather!"')
    secondchoice=input('How many did you find? 1- SIX. 2- SEVEN. 3- EIGHT.')
    if secondchoice == "1":
        print('"Six?! You didn\'t even try to find them all!" Mr. Cottontail exclaims, outraged, as he grabs a garden rake...game over.')
    elif secondchoice == "3":
        print('"Eight? Do you think I don\'t know how many snails I have in my darden? WHO ARE YOU TRYING TO FOOL?" Mr. Cottontail yells, stomping on the snails you gathered in a fit of range.')
    elif secondchoice== "2":
        print('"Great job! You\'ve got a keen eye champ!" Mr. Cottontail says with a friendly pat on your shoulder. Mr. Conttotail takes the snails from you and sits down at the table. "Now I\'ll show you how to prepare escargot using my great-grandfather\'s recipe" He says proudly.')
        thirdchoice = input('Then he adds "You\'ll try some, right?" 1- With pleasure! Thank you for the treat. 2- I\'d love to, but I\'m allergic to snails... 3- Sorry, my friend, I\'m a vegetarian. "')
        if thirdchoice == "1":
            print('You eagerly take a bite of the escargot, but suddenly the shell gets stuck in your throat. You can\'t breath...game over.')
        elif thirdchoice== "2":
            print ('" Me too, that\'s why I always carry antihistamine tablets. What\'s your allergen concentration for different species? I react most to Helix snails!" Mr. Conttotail realizes you\'re lying when you start to stammer, trying to answer his probing questions...game over."')
        elif thirdchoice== "3":
            print('Mr. Cottontail doesn\'t question your statement, as he believes that one can become a vegetarian overnight, making it hard to tell if you\'re lying.')
            print('After finishing his meal, Mr. Cottontail announces that it\'s time to get back to pulling weeds."Which tool do you want for yourself?" Mr. Cottontail asks.')
            fourthquestion=input('Select one tool for pulling weeds. 1- Hand Weeder. 2- Hori-Hori Knife. 3- Hoe.')
            if fourthquestion== "1":
                print('Mr. Cottontail hands you a tool, and together you both start working, humming your favorite songs.')
            elif fourthquestion== "2":
                print('" Ahhh, the Japanese art of gardening!" says Mr. Cottontail cheerfully. "One of my favorite tools!" Together, you both set o work, and the time passes quickly.')
            elif fourthquestion== "3":
                print('"WHAT DID YOU JUST CALL ME?" Before you can explain, Mr. Cottontail eyes flash with fury, and he lunges at you with terrifying speed. But then, he pauses, realizing you were referring to the tool. He bursts into laughter, the tension dissolving. "Oh, the hoe! I thought you were calling me names!" he says, still chuckling. "Anyway, let\'s get back to work!"')

            print('At a certain point, Mr. Cottontail looks up at the sky and says, "That\'s enough for today. It\'s already sunset: You set down your tool and gaze at the sky as well. The garden looks exceptionally beautiful at this hour. "Thank you for your help," says Mr. Cottontail. After a moment thought, he adds, "It was a good idea to let you out of the cage today."')
            print('Congratulations! You made it through thees safe and sound- you won!')

elif firstchoice== "3":
    print('Mr. Cottontail finds it very rude that you point out the neglected garden. " MAYBE IF SOMEONE HELPED ME MORE OFTEN, THEY WOULDN\'T BE SO TALL!!!" He shouts in fury...game over."')

