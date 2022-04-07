import random

level = 90
A = 205
D = 188
power = 110

target = 1
weath = 1
badge = 1
crit = 1
rand = random.uniform(0.85, 1)
stab = 1.5
type = 0.5
burn = 1
other = 1

modifier = target * weath * badge * crit * rand * stab * type

damage = ((((((2 * level / 5 ) + 2) * power) *(A / D))) / (50 + 2) * modifier)

print('Charizard Damage is : ',round(damage))