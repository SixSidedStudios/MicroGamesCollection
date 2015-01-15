#Apple picker game
print 'Welcome to the Apple Picker game.'
gold = 0
apples = 0

def crash():
    print 'ADUHA*UYg&GAD&ga^d8ady68fsd8*&AdadbA'
    print 'NFIh8aGd79adA^Yd78789Adtg7A674dgd^*A'
    print 'JUADYh7a*dbg&A(dbUAd8a79dhA*Z)bdna*('
    crash()

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
    if pick.lower() == 'y':
        print 'You picked an apple!'
        global apples
        apples += 1
        if apples > 1:
            print 'You have',apples,'apples!'
            begin()
        else:
            print 'You have',apples,'apple!'
            begin()
    elif pick.lower() == 'n':
        if_sell = raw_input('Would you like to sell your apples? Y/N:')
        if if_sell.lower() == 'y':
            sell()
        elif if_sell.lower() == 'n':
            begin()
        else:
            print 'You speak gibberish, eh?'
            begin()
    elif pick.lower() == 'crash':
        print 'Apple_picker.py has stopped working'
        crash()
    else:
        print "I suppose that means something..."
        begin()
start = raw_input('Would you like to begin? Y/N:')
if start.lower() == 'y':
    begin()
elif start.lower() == 'n':
    print 'You suck...'
    begin()
else:
    print 'I don\'t understand gibberish...'
    begin()
