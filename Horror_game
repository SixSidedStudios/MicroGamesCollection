#house explorer
from time import sleep

#This is a horror game that i started on vacation... and got kinda cool!!!
#from this point to the controls section is into, the rest is game
print '"Welcome to Mr. Dibs house, or what used to be his house."'
sleep(2)
print '.'
sleep(1)
print '.'
sleep(1)
print '.'
sleep(1.5)
print '"Well, um, this is the outside as you can see its a vary nice and bright house."'
sleep(3)
print 'Vines climb up and down the dark wooden boards of the house.'
sleep(2.5)
print '"Um i guess we should take a look inside."'
sleep(2.5)
print 'You and the supposed realtor walk up the crumbling concrete stairs.'
sleep(3)
print 'A locked keybox hangs from the doorknob.'
sleep(3)
print 'Its cracked.'
sleep(1.5)
print '"Ehem, um... dont worry."'
sleep(1.5)
print 'He opens the keybox.'
sleep(2.5)
print 'The key is gone...'
sleep(1.5)
print '"Um, heh... dont worry i... well i have another one, one, another key..."'
sleep(3.5)
print 'He pulls out a new key... inserts it into the door, and turns.'
sleep(3)
print '"So... um, Mr. Dibs had owned this, this vary lovely house for um seven years. As you can see he took not the best care of it... but um."'
sleep(5)
print 'Broken beer bottles litter the floor, the shelves are full of pictures, there are two doorways to diffrent rooms.'
sleep(5)
print '"Well i guess ill let you walk around for a bit, um make sure you visit the attic..."'
sleep(4.5)
print '"its um really well made, ya\' know... so yah, ill be right back i um just gotta check on the temp, of the, the house... so yah ill be right with you..."'
sleep(6)
print 'Use these commands to run the play the game:'
sleep(2)
print 'move <area> ;to move to another room'
print 'see ;to get a discription of what you see'
print 'use <object> ;to activate an object'
print 'behind ;to see if someones behind you'
print 'light ;to turn on the rooms light'

#def first act cmnds
def see1():
    print 'Broken beer bottles litter the floor, the shelves are full of pictures, there are two doorways to diffrent rooms.'
    action()
def behind1():
    print 'The door is behind you...'
    action()
def light1():
    print 'You turn the light on. You can now see that the dining room is beside you.'

#def main cmnds    
def move(area):
    movearea = area[4:]
    if movearea == 'dining room':
        room = 'dining'
        action()
    elif movearea == 'living room':
        room = 'living'
        action()
    elif movearea == 'kitchen':
        room = 'kitchen'
        action()
    elif movearea == 'kids bedroom':
        room = 'kids'
        action()
    elif movearea == 'adult bedroom':
        room = 'bed'
        action()
    else:
        print 'Invalid area or command!'
        action()
        
def see():
    if room == 'dining':
        print 'There is a single table in the dining room. It has some plates with rotted food on them. Its cold.'
        print 'There is a shelf in the room, it is bent to the right and is missing a shelf board at the bottom.'
        print 'It ha several games on it, including the board game clue.'
        print 'the kitchen is in front of you and next to you is the living room.'
        action()
    elif room == 'living':
        print 'In the living room there is a couch against the northern wall.'
        print 'It has many scratches on it and there is some fluff coming out the side pillow.'
        print 'Oppisite the couch there sits an old 80\s television. The glass is shatterd.'
        print 'There are some old movies sitting on top of it, including williwonka.'
        print 'In front of you is the kids bedroom, and to your right is the kitchen.'
        action()
    elif room == 'kitchen':
        print 'The kitchen is a small space. It is one hallway with the adult bedroom and dining room at either end and counter on either side of you.'
        print 'The sink is vary rusty and has a large dent in the side of it. The tap of the sink has been snapped off.'
        print 'The oven is sitting idle behind you.'
        print 'A single kitchen knife lies next to cutting board.'
        action()
    elif room == 'kids':
        print 'The kids bedroom is small. It has a desk with A computer sitting on it. The desk also has many pencils and dice in contaniers.'
        print 'There is a one bed to your right. It has no sheets on it.'
        action()
    elif room == 'bed':
        print 'There is one twin sized bed in the middle of the room. A bedstand sits next to the bed with a single glass of water.'
        print 'There is a window in the left wall.'
        sleep(3.5)
        print 'Its open'

#variable incharge of what room ur in
room = 'door'

def use():
    if room == 'living':
        usetv()
    elif room == 'dining':
        print 'Sorry there is nothing to use in this room!'
        action()
    elif room == 'kids':
        usecpu()
    elif room == 'kitchen':
        usestov()
    elif room == 'bed':
        usewin()

#def the main usr inpt
def action():
    useract = raw_input('What do you do now?')
    if useract[0:4] == 'move':
        move(action)
    elif useract[0:3] == 'see':
        see()
    elif useract[0:3] == 'use':
        use()
    elif useract[0:6] == 'behind':
        behind()
    elif useract[0:6] == 'light':
        light()
#edirty easteregg
    elif useract == 'use bathroom':
        print 'You walk into the elegant bathroom with heated floors and a shining mirror.'
        sleep(2)
        print 'You sit on the toilet and take a HUGE dump'
        sleep(1.5)
        print 'You take the crap out of the toilet and stuff it in your pocket'

#frst usr act
useract = raw_input('What is your first action:')
if useract[0:4] == 'move':
    move(useract[4:])
elif useract[0:3] == 'see':
    see1()
elif useract[0:3] == 'use':
    print 'There is nothing to use!'
elif useract[0:6] == 'behind':
    behind1()
elif useract[0:6] == 'light':
    light1()

#have fun
