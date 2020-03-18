# Dothraki are planning an attack to usurp King Robert's throne.
# King Robert learns of this conspiracy from Raven and plans to lock the single door through which the enemy can enter his kingdom.
#
# But, to lock the door he needs a key that is an anagram of a palindrome.
# He starts to go through his box of strings, checking to see if they can be rearranged into a palindrome.

# aaabbbb YES
# cdefghmnopqrstuvw NO
# cdcdcdcdeeeef YES
# aaabbb NO

def seeIfItCanCreatePalindrome(string):
	dt = getTheCountOfEachChar(string)
	# print(dt)
	length_of_string = len(string)
	if(length_of_string%2 == 0): 	# if it is EVEN
		if(checkIfAnyCharIsOutOfPair(dt)):
			return 'NO'
		else:
			return 'YES'
		## END
	else: 							# if it is ODD
		if(checkIfOnlyOneCharIsOutOfPair(dt)):
			return 'YES'
		else:
			return 'NO'
		## END
	## END
## END


def getTheCountOfEachChar(string):
	dt = {}
	for ch in string:
		if(dt.get(ch) == None):
			dt[ch] = 1
		else:
			dt[ch] = dt[ch] + 1
		## END
	## END
	return dt
## END


def checkIfAnyCharIsOutOfPair(dt):
	for char_count in dt.values():
		if((char_count%2) != 0):
			return True
		## END
	## END
	return False
## END


def checkIfOnlyOneCharIsOutOfPair(dt):
	chars_out_of_pair = 0
	for char_count in dt.values():
		if((char_count%2) != 0):
			chars_out_of_pair += 1
		## END
		if(chars_out_of_pair > 1):
			return False
		## END
	## END
	return True
## END


if __name__ == '__main__':
	# string = input()
	# string = 'aabbccdd'
	# string = 'aaabbbb'
	# string = 'aaabbb'
	# string = 'cdcdcdcdeeeef'
	string = 'cdefghmnopqrstuvw'
	result = seeIfItCanCreatePalindrome(string)
	print(result)
## END
