#adventure Stuffs
#coleman Moore

import random

wep = random.randint(1,5)
prot = random.randint(1,5)

inventory = ()



if wep == 1:
    inventory += 'sword'

elif wep == 2:
    inventory +='knife'

elif wep == 3:
    inventory += 'spear'

elif wep == 4:
    inventory += 'bow'

elif wep == 5:
    inventory += 'fire rune'
    
if prot == 1:
    inventory += 'shield'

elif prot == 2:
    inventory += 'chestplate'

elif prot == 3:
    inventory += 'helmet'

elif prot == 4:
    inventory += 'magical shield'

elif prot == 5:
    inventory += 'golem'



input('you found a weapon and a peice of protection')
print('here is your inventory',inventory)

