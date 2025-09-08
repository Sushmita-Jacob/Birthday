# Introduction
money = 100
points = 0
guessAge = 0
guessCup = ""
guessBalloon = ""
print("You are planning a birthday party for your friend, Heidi! You have $100 to spend. Make sure not to go into debt!")

# Buy a gift
print("First, what will be your gift?")
gift = ""
while gift != "A" and gift != "a" and gift != "B" and gift != "b" and gift != "C" and gift != "c":
    gift = input("(A) A coin purse - $10\n(B) A set of armor - $50\n(C) A candle - $5\nYour choice: ")
    if gift == "A" or gift == "a":
        money = money - 10
        points = points + 15
        print("Heidi loved the new coin purse! It looks just like him.")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (+15)")
        break
    elif gift == "B" or gift == "b":
        money = money - 50
        points = points + 5
        print("The armor couldn't fit... but it was shiny!")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (+5)")
        break
    elif gift == "C" or gift == "c":
        money = money - 5
        points = points - 10
        print("Ouch! Heidi burnt his tail.")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print ("Heidi happiness: " + str(points) + " (-10)")
        break
    else:
        print("Hmm... that doesn't look like an option. Try again!")

# Make a cake
print("\nNext, let's buy a cake. What size will you buy?")
cakeSize = ""
while cakeSize != "A" and cakeSize != "a" and cakeSize != "B" and cakeSize != "b" and cakeSize != "C" and cakeSize != "c":
    cakeSize = input("(A) Small - $5\n(B) Medium - $10\n(C) Large - $15\nYour choice: ")
    if cakeSize == "A" or cakeSize == "a":
        money = money - 5
        points = points - 5
        print("A little too small for a party...")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (-5)")
        break
    elif cakeSize == "B" or cakeSize == "b":
        money = money - 10
        points = points + 5
        print("Perfect! Just the right amount for everyone plus some leftovers.")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next time try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (+5)")
        break
    elif cakeSize == "C" or cakeSize == "c":
        money = money - 15
        points = points - 5
        print("Too much cake! Some of it had to be fed to the racoons...")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (-5)")
        break
    else:
        print("Hmm... that doesn't look like an option. Try again!")

print("\nWhat is your base flavor?")
cakeFlavor = ""
while cakeFlavor != "A" and cakeFlavor != "a" and cakeFlavor != "B" and cakeFlavor != "b" and cakeFlavor != "C" and cakeFlavor != "c":
    cakeFlavor = input("(A) Plain - $10\n(B) Chocolate - $15\n(C) Rainbow - $20\nYour choice: ")
    if cakeFlavor == "A" or cakeFlavor == "a":
        money = money - 10
        points = points - 5
        print("The cake was dry and pretty boring. Spice it up with frosting!")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (-5)")
        break
    elif cakeFlavor == "B" or cakeFlavor == "b":
        money = money - 15
        points = points + 10
        print("Heidi loves chocolate! Yummy!")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness " + str(points) + " (+10)")
        break
    elif cakeFlavor == "C" or cakeFlavor == "c":
        money = money - 20
        points = points + 5
        print("So many pretty colors!")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (+5)")
        break
    else:
        print("Hmm... that doesn't look like an option. Try again!")

print("\nWhat frosting will you put on the cake?")
frostingFlavor = ""
while frostingFlavor != "A" and frostingFlavor != "a" and frostingFlavor != "B" and frostingFlavor != "b" and frostingFlavor != "C" and frostingFlavor != "c":
    frostingFlavor = input("(A) None - $0\n(B) Vanilla - $5\n(C) Cream cheese - $10\nYour choice: ")
    if frostingFlavor == "A" or frostingFlavor == "a":
        money = money - 0
        points = points + 0
        print("Frosting is overrated anyway!")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print ("Heidi happiness: " + str(points) + " (no change)")
        break
    elif frostingFlavor == "B" or frostingFlavor == "b":
        money = money - 5
        points = points + 5
        print("Vanilla's always a classic!")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (+5)")
        break
    elif frostingFlavor == "C" or frostingFlavor == "c":
        money = money - 10
        points = points + 10
        print("Cream cheese is Heidi's favorite! How'd you know?")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (+10)")
        break
    else:
        print("Hmm... that doesn't look like an option. Try again!")

print("\nFinally, what finishing touches should we add onto the cake?")
addOns = ""
while addOns != "A" and addOns != "a" and addOns != "B" and addOns != "b" and addOns != "C" and addOns != "c":
    addOns = input("(A) None - $0\n(B) Chocolate chips - $5\n(C) Sprinkles - $5\nYour choice: ")
    if addOns == "A" or addOns == "a":
        money = money - 0
        points = points + 0
        print("Keeping it basic...")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (no change)")
        break
    elif addOns == "B" or addOns == "b":
        money = money - 5
        points = points + 5
        print("So chocolately! Milk, dark, and white!")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (+5)")
        break
    elif addOns == "C" or addOns == "c":
        money = money - 5
        points = points + 5
        print("Sprinkle the sprinkles!")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" +str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (+5)")
        break
    else:
        print("Hmm... that doesn't look like an option. Try again!")

# Get the food
print("\nNow that we're done with cake, let's get the other food! What snacks will you buy?")
snacks = ""
while snacks != "A" and snacks != "a" and snacks != "B" and snacks != "b" and snacks != "C" and snacks != "c":
    snacks = input("(A) Chips - $5\n(B) Cookies - $5\n(C) Popcorn - $5\nYour choice: ")
    if snacks == "A" or snacks == "a":
        money = money - 5
        points = points + 10
        print("Chips and cake go so well together!")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (+10)")
        break
    elif snacks == "B" or snacks == "b":
        money = money - 5
        points = points - 10
        print("You already have cake - sweet cookies will give you a bellyache!")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (-10)")
        break
    elif snacks == "C" or snacks == "c":
        money = money - 5
        points = points - 5
        print("Heidi could choke on popcorn! Irresponsible!")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (-5)")
        break
    else:
        print("Hmm... that doesn't look like an option. Try again!")

print("\nLast but not least to eat, the drinks. What should we drink at the party?")
drinks = ""
while drinks != "A" and drinks != "a" and drinks != "B" and drinks != "b" and drinks != "C" and drinks != "c":
    drinks = input("(A) Water - $0\n(B) Juice - $5\n(C) Soda - $10\nYour choice: ")
    if drinks == "A" or drinks == "a":
        money = money - 0
        points = points + 5
        print("Heidi needs to stay hydrated! Great thinking!")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (+5)")
        break
    elif drinks == "B" or drinks == "b":
        money = money - 5
        points = points + 5
        print("So many juice varieties! Apple, orange, lemonade, punch...")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (+5)")
        break
    elif drinks == "C" or drinks == "c":
        money = money - 10
        points = points - 5
        print("Heidi doesn't like soda. Too fizzy!")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (-5)")
        break
    else:
        print("Hmm... that doesn't look like an option. Try again!")

# Decorations
print("\nAnd now the fun part, decorations! What colored balloons will you put up?")
balloons = ""
while balloons != "A" and balloons != "a" and balloons != "B" and balloons != "b" and balloons != "C" and balloons != "c":
    balloons = input("(A) Black - Free\n(B) Red - Free\n(C) Green - Free\nYour choice: ")
    if balloons == "A" or balloons == "a":
        money = money - 0
        points = points + 10
        print("Heidi's favorite color is black! Yay!")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (+10)")
        break
    elif balloons == "B" or balloons == "b":
        money = money - 0
        points = points + 5
        print("Heidi likes red! Matches the color of roses")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (+5)")
    elif balloons == "C" or balloons == "c":
        money = money - 0
        points = points - 5
        print("Heidi hates green! It looks like grass. Yuck!")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (-5)")
    else:
        print("Hmm... that doesn't look like an option. Try again!")

print("\nTime to make a poster! What should it say?")
poster = ""
while poster != "A" and poster != "a" and poster != "B" and poster != "b" and poster != "C" and poster != "c":
    poster = input("(A) Cakes and Candles - $5\n(B) Congratulations, you escaped the womb! - $10\n(C) Wish you well - Free\nYour choice: ")
    if poster == "A" or poster == "a":
        money = money - 5
        points = points - 10
        print("Trying to be nonchalant won't impress Heidi.")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (-10)")
    elif poster == "B" or poster == "b":
        money = money - 10
        points = points + 15
        print("Heidi found it hilarious! Good job!")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (+15)")
    elif poster == "C" or poster == "c":
        money = money - 0
        points = points - 5
        print("Heidi's a little disappointed by the lack of effort... try to personalize it!")
        print("Cash left: $" + str(money))
        if money < 20 and money > 0:
            print("*Be careful! You only have $" + str(money) + " left! Don't go into debt!*")
        if money < 0:
            print("*You're in debt! You can keep playing, but next year try to stay in the budget!*")
        print("Heidi happiness: " + str(points) + " (-5)")
    else:
        print("Hmm... that doesn't look like an option. Try again!")

# Guess Heidi's age
print("\nTime for the party! Heidi bets $10 you can't guess his age! Let's take the challenge!")
while guessAge != 20:
    guessAge = int(input("How old is Heidi? "))
    if guessAge > 20:
        print("Heidi isn't THAT old now. Try again!")
    if guessAge < 20:
        print("Heidi isn't a baby! Try again!")
    if guessAge == 20:
        money = money + 10
        print("You did it! Here's your $10!")
        print("Cash left: $" + str(money))
        break

#Sing happy birthday
print("\nLet's sing Happy Birthday together! Press enter to continue the lyrics.")
input("\nHappy birthday to you,")
input("Happy birthday to you,")
input("Happy birthday, dear Heidi,")
input("Happy birthday to you!")

# Watch Heidi blow out the candles
candlesOne = "tttt"
candlesTwo = "tttt"
candlesThree = "tttt"
candlesFour = "tttt"
candlesFive = "tttt"

print("\n" + candlesOne + candlesTwo + candlesThree + candlesFour + candlesFive)
print("Look at how bright the birthday candles shine on the cake! Hype up Heidi as he blows them out!")
blow = input("Type 'blow' to blow out the flames. ")
if blow == "blow":
    print(candlesOne + candlesTwo + candlesThree + candlesFour)
    blow = ""
blow = input("Keep going! Type out 'blow': ")
if blow == "blow":
    print(candlesOne + candlesTwo + candlesThree)
    blow = ""
blow = input("Almost halfway there! Type out 'blow': ")
if blow == "blow":
    print(candlesOne + candlesTwo)
    blow = ""
blow = input("Just a few more! Type out 'blow': ")
if blow == "blow":
    print(candlesOne)
    blow = ""
blow = input("Only one more set of candles left! Type out 'blow' one last time! ")
if blow == "blow":
    blow = ""
print("You did it, Heidi!")

# Choose the cup
firstCup = "O"
secondCup = "O"
thirdCup = "O"

print("\nOnto the party games! Choose which cup the ball is under!")
while guessCup != "3":
    print(firstCup + " " + secondCup + " " + thirdCup)
    guessCup = input("Type in 1, 2, or 3 to choose a cup! ")
    if guessCup == "1":
        firstCup = " "
        print("Incorrect! The cup was empty. Try again!")
    elif guessCup == "2":
        secondCup = " "
        print("Incorrect! The cup was empty. Try again!")
    elif guessCup == "3":
        thirdCup = "o"
        print(firstCup + " " + secondCup + " " + thirdCup)
        print("Correct! The ball was under the third cup! Congrats.")
    elif guessCup != "1" and guessCup != "2" and guessCup != "3":
        print("Please choose a number from 1 to 3. Try again!")

# Pop the balloons
firstBalloon = "Q"
secondBalloon = "Q"
thirdBalloon = "Q"
fourthBalloon = "Q"
fifthBalloon = "Q"

print("\nThrow a dart at a balloon for $10. Get a chance to win a cash prize!")
print(firstBalloon + " " + secondBalloon + " " + thirdBalloon + " " + fourthBalloon + " " + fifthBalloon)
if money < 10:
    print("Sorry, you can't afford a dart. Try again next year!")
while money >= 10:
    guessBalloon = input("Type a number from 1 to 5 to pop a balloon! Type exit to exit! ")
    if guessBalloon == "1" and firstBalloon == "Q":
        firstBalloon = "X"
        money = money - 10
        money = money + 5
        print("Congratulations, you got $5!")
        print("Cash: $" + str(money))
        print(firstBalloon + " " + secondBalloon + " " + thirdBalloon + " " + fourthBalloon + " " + fifthBalloon)
    elif guessBalloon == "2" and secondBalloon == "Q":
        secondBalloon = "X"
        money = money - 10
        money = money + 15
        print("Congratulations, you got $15!")
        print("Cash: $" + str(money))
        print(firstBalloon + " " + secondBalloon + " " + thirdBalloon + " " + fourthBalloon + " " + fifthBalloon)
    elif guessBalloon == "3" and thirdBalloon == "Q":
        thirdBalloon = "X"
        money = money - 10
        money = money + 0
        print("Sorry, your balloon was empty!")
        print("Cash: $" + str(money))
        print(firstBalloon + " " + secondBalloon + " " + thirdBalloon + " " + fourthBalloon + " " + fifthBalloon)
    elif guessBalloon == "4" and fourthBalloon == "Q":
        fourthBalloon = "X"
        money = money - 10
        money = money + 25
        print("Congratulations, you got $25")
        print("Cash: $" + str(money))
        print(firstBalloon + " " + secondBalloon + " " + thirdBalloon + " " + fourthBalloon + " " + fifthBalloon)
    elif guessBalloon == "5" and fifthBalloon == "Q":
        fifthBalloon = "X"
        money = money - 10
        money = money + 10
        print("Congratulations, you got $10!")
        print("Cash: $" + str(money))
        print(firstBalloon + " " + secondBalloon + " " + thirdBalloon + " " + fourthBalloon + " " + fifthBalloon)
    elif guessBalloon == "1" and firstBalloon == "X":
        print("Sorry, you already popped Balloon 1. Try a different one!")
    elif guessBalloon == "2" and secondBalloon == "X":
        print("Sorry, you already popped Balloon 2. Try a different one!")
    elif guessBalloon == "3" and thirdBalloon == "X":
        print("Sorry, you already popped Balloon 3. Try a different one!")
    elif guessBalloon == "4" and fourthBalloon == "X":
        print("Sorry, you already popped Balloon 4. Try a different one!")
    elif guessBalloon == "5" and fifthBalloon == "X":
        print("Sorry, you already popped Balloon 5. Try a different one!")
    elif guessBalloon.lower() == "exit":
        break
    else:
        print("Your response is invalid. Type in a number from 1 to 5!")

# Ending
if points > 5:
    print("\nCongratulations! It's the end of Heidi's birthday. He loved celebrating it with you!")
if points <= 5:
    print("\nCongratulations! It's the end of Heidi's birthday. He appreciated you spending time with him!")
print("Heidi had " + str(points) + " happiness points today!")
print("At the end of the day, you had $" + str(money) + "!")
if money > 25:
    print("You're basically rich!")
if money <= 25 and money > 0:
    print("You didn't go into debt!")
if money < 0:
    print("You went into debt, but at least it was for a friend (or from gambling...)")
print("Thank you for playing!")