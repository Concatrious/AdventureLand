#a walk in the woods
#by Coleman Moore
#an interactive game

import random
import sys
#the begging / finding things out
begin = input('hello young adventurer shall we begin your adventure')

#making up #'s

numb1 = random.randint(1,3)
numb2 = random.randint(1,3)



#tutorial
print('OK lets go over a couple of things',
      '\n all answers should be lowercase',
      ' unless i tell you otherwise',
      '\nno cheating it ruins the game',
      '\nto continue from text press enter')
print('\n\nNow on to the adventure!!!')

#first steps
direction = input('which way do you want to go')


if numb1 == 1:
        y='left'
        
elif numb1 == 2:
        y='right'
        
elif numb1 == 3:
        y='straight'
        
while direction != y:
    direction = input('you cant go that way try a diffrent direction!!')

print('yay! you found an old sword on the ground!!')
sword = 1

print('there is a zombie running towards you')
print('do you',
      '\n1. Hit it with the sword',
      '\n2. Run Run Run!!!',
      '\n3. Play dead')
hit = int(input())

#hit it with a sword
if hit == 1:
    print('You plunge your blade deep into the zombies chest',
          'and it crumples to the ground')

    loot = input('do you want to loot the body of the Shia LeZombie?')
    if loot=='yes':
        print('you found a ring')
        input('the ring makes you invalnarable against un dead')
        ring4undead=1

    turn = input('which way do you want to go now?')
    numb = random.randint(1,3)
    if numb == 1:
        x='left'
        
    elif numb == 2:
        x='right'
        
    elif numb == 3:
        x='straight'

    #if num1
    while turn != x:
        turn = input('you cant go that way try a diffrent direction!!')



#Run Run away
if hit == 2:
    print('you start running hes about thirty feet back he breaks into a sprint',
          'but his arm falls off\nyou continue to run but suddenly your leg \
its caught in a bear trap')
    naw = input('\n your think about knawing it off but will you\
\n(yes or no to this type of questions please)')

    if naw == 'yes':
        print('you escape but you have dropped your sword')
    else:
        print('Shia catches up to you and eats you\n\n\nACTUAL CANIBAL \
SHIA LEZOMBIE')
    input('you have died press enter and retry\n\n \t\t\t\tGAME OVER')

    sys.exit(0)
    
          
#play dead
if hit == 3:
    print('you lay down in a neer by ditch hoping the Zombie will not notice\
you\n but its actual caniban shia leZombie and he rips in to your chest ripping\
you apart you have no time to reach for your sword\n You are dead')
    input('press enter and retry for a better fate')

    sys.exit(0)


          
print('yay you lived')
input('press enter to exit the game')
