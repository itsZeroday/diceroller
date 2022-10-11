import random

print('Enter the number of sides for the die')
sides = int(input(''))
print('How many times do you want to roll?')
rolls = int(input(''))

for x in range(rolls):
	print('You rolled a...')
	print(random.randint(1,sides))
