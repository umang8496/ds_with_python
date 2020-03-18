
# Steve has a string of lowercase characters in range ascii[‘a’..’z’].
# He wants to reduce the string to its shortest length by doing a series of operations.
# In each operation he selects a pair of adjacent lowercase letters that match, and he deletes them.
# For instance, the string aab could be shortened to b in one operation.

# Steve’s task is to delete as many characters as possible using this method and print the resulting string.
# If the final string is empty, print Empty String

class MyStackImpl():
	def __init__(self):
		self.stack = []
		self.top = -1
	## END

	def push(self, ch):
		self.top += 1
		self.stack.append(ch)
	## END

	def pop(self):
		if(self.top == -1):
			return None
		## END
		value = self.stack[self.top]
		del self.stack[self.top]
		self.top -= 1
		return value
	## END

	def peek(self):
		return self.stack[self.top]
	## END

	def removeTheTop(self):
		del self.stack[self.top]
		self.top -= 1
	## END

	def getSize(self):
		return (self.top + 1)
	## END
## END


def getSuperReducedString(string):
	stack = MyStackImpl()
	for ch in string:
		if(stack.getSize() == 0):
			stack.push(ch)
		else:
			if(stack.peek() == ch):
				stack.removeTheTop()
				continue
			else:
				stack.push(ch)
			## END
		## END
	## END
	if(stack.getSize() == 0):
		return 'Empty String'
	else:
		return("".join(stack.stack))
	## END
## END


if __name__ == '__main__':
	string = input('Enter the string : ')
	super_reduced_string = getSuperReducedString(string)
	print(super_reduced_string)
## END
