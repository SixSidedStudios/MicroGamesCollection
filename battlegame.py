#Sorry for the lack of commentating. I wasn't going to make a general GitHub when I first made this. I'll add more soon
print "Welcome to the battle game!"
GOLD = 0
def start():
    ans = raw_input("Do you want to FIGHT or BUY:")
    if ans.lower() == "fight":
        fight()
    elif ans.lower() == "buy":
        buy()
    else:
        print "That is not a command. Try again."
        start()
def fight():
    print "You choose to fight!"
    fans = raw_input("Choose a number 1-4 to get an enemy:")
    if fans == "1":
        print "You encounter an ORC!"
        orc()
def orc():
    fans2 = raw_input("You can ATTACK, DEFEND, or RUN:")
    if fans2.lower() == "attack":
        print "YOU attack! ORC has 5/10 HP!"
        fans2 = raw_input("You can ATTACK, DEFEND, or RUN:")
        if fans2.lower() == "attack":
            print "YOU attack! ORC has 0/10 HP! You win the battle and gain 10 GOLD!"
            global GOLD
            GOLD = GOLD + 10
            start()
    elif fans2.lower() == "defend":
        print "ORC attacks! YOU have 5/10 HP!"
        fans2 = raw_input("You can ATTACK, DEFEND, or RUN:")
        if fans2.lower() == "defend":
            print "ORC attacks! YOU have 0/10 HP! YOU lose the battle!"
            print "YOU die and lose all your gold!"
            global GOLD
            GOLD = 0
            start()
    elif fans2.lower() == "run":
        print "YOU run away from the ORC!"
        start()
    else:
        print "That doesn't work. Try again."
        orc()
start()
