#Apple picker game
print 'Welcome to the Apple Picker game.'
gold = 0
apples = 0

def sell():
    global apples
    global gold
    gold = apples * 10
    apples = 0
    print "You have ",apples," apples."
    print "You got ",gold," gold."
    begin()

def begin():
    pick = raw_input('Would you like to pick an apple? Y/N:')
    if pick == 'y':
        print 'You picked an apple!'
        global apples
        apples += 1
        print apples
        begin()
    elif pick == 'n':
        if_sell = raw_input('Would you like to sell your apples? Y/N:')
        if if_sell == 'y':
            sell()

start = raw_input('Would you like to begin? Y/N:')
if start == 'y':
    begin()
elif start == 'n':
    print 'You suck...'
    begin()
