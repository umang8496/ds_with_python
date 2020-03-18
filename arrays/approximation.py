#cube=27
cube = int(input("Enter a value for determing its cube root..."))
guess = float(input("What's your estimation? "))
epsilon = 0.01
increment = 0.0001
decrement = -0.0001
num_guesses = 0

if(abs(guess**3-cube) >= epsilon):
	while abs(guess**3-cube) >= epsilon:
		guess += increment
		num_guesses += 1
else:
	while abs(guess**3-cube) < epsilon:
		guess += increment
		num_guesses += 1
		
print("num_guesses:",num_guesses)
print(guess,"is close to the cube root of",cube)

##if (guess**3-cube)>=epsilon:
##     print("failed on cube root of",cube)
##else:
##     print(guess,"is close to the cube root of",cube)
