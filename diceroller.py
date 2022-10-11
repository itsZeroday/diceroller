import random
while True:
	try:
		sides = int(input('Please enter the number of sides for the die: '))
		rolls = int(input('How many times do you want to roll: '))
		for x in range(rolls):
			print(random.randint(1,int(sides)))
	except ValueError:
		print('Sorry, that is an invalid input. Try again...')
