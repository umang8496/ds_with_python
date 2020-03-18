
def isPrime(number):
	if(number == 2 or number == 3 or number == 5 or number == 7):
		return True
	elif((number % 2) == 0):
		return False
	else:
		upper_limit = abs(int(number**(1/2)))
		for i in range(3,upper_limit+1):
			if(number%i == 0):
				return False
			## END
		## END
		return True
	## END
## END


def getLastPrime(number):
	if(number > 2):
		for i in range(number-1,2,-1):
			if(isPrime(i)):
				return i
			else:
				continue
			## END
		## END
	else:
		return 2
	## END
## END


def getNextPrime(number):
	if(number > 2):
		i = number
		while(True):
			if(isPrime(i)):
				return i
			else:
				i += 1
			## END
		## END
	else:
		return 2
	## END
## END


def getNearestPrime(ascii_ch, last_prime, next_prime):
	if((ascii_ch - last_prime) < (next_prime - ascii_ch)):
		return last_prime
	elif((ascii_ch - int(last_prime)) > (int(next_prime) - ascii_ch)):
		if(next_prime <= 122):
			return next_prime
		else:
			return last_prime
	else:
		return last_prime
	## END
# END


def getMagicalEquivalent(word):
	magical_word = []
	for ch in word:
		ascii_ch = ord(ch)
		if(ascii_ch < 65):
			magical_word.append('C')
		elif(isPrime(ascii_ch)):
			magical_word.append(chr(ascii_ch))
		else:
			last_prime = getLastPrime(ascii_ch)
			next_prime = getNextPrime(ascii_ch)
			# print(ascii_ch, last_prime, next_prime)
			required_prime = getNearestPrime(ascii_ch, last_prime, next_prime)
			# print(chr(required_prime))
			magical_word.append(chr(required_prime))
		## END
	## END
	return("".join(magical_word))
## END


if __name__ == '__main__':
	# word = input('Enter the word : ')
	word = 'j4eZamQY0SQgM9cX7dcb'
	magical_equivalent = getMagicalEquivalent(word)
	print(magical_equivalent)
	
	# print(isPrime(121))
	# print(isPrime(13))
	# print(isPrime(63))
	# print(isPrime(65))
	
	# print(getLastPrime(121))
	# print(getLastPrime(30))
	# print(getLastPrime(27))
	# print(getLastPrime(10))

	# print(getNextPrime(121))
	# print(getNextPrime(30))
	# print(getNextPrime(27))
	# print(getNextPrime(10))
	# print(getNearestPrime(121, getLastPrime(121), getNextPrime(121)))
## END

# j4eZamQY0SQgM9cX7dcb
# kCeYamOYCSOgOCaYCeaa


