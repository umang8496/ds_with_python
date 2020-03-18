
# A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
# By this logic, we say a sequence of brackets is balanced if the following conditions are met:

# It contains no unmatched brackets.
# The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
# Given N strings of brackets, determine whether each sequence of brackets is balanced.
# If a string is balanced, return YES. Otherwise, return NO.


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

	def isEmpty(self):
		return self.top == -1
	## END

	def getSize(self):
		return (self.top + 1)
	## END
## END


def isBalanced(string):
	if(len(string)%2 != 0):
		return 'NO'
	## END

	stack = MyStackImpl()

	for ch in string:
		if(ch == '[' or ch == '{' or ch == '('):
			stack.push(ch)
		else:
			if(stack.getSize() > 0):
				if(ch == ')'):
					if(stack.peek() != '('):
						return 'NO'
					else:
						stack.removeTheTop()
					## END
				## END
				if(ch == '}'):
					if(stack.peek() != '{'):
						return 'NO'
					else:
						stack.removeTheTop()
					## END
				## END
				if(ch == ']'):
					if(stack.peek() != '['):
						return 'NO'
					else:
						stack.removeTheTop()
					## END
				## END
			## END
		## END
	## END
	if(stack.isEmpty()):
		return 'YES'
	else:
		return 'NO'
	## END
## END


if __name__ == '__main__':

	# test_cases = int(input())
	test_cases = 1
	for _ in range(test_cases):
		# string = input()
		# string = '{[()]}'
		string = '{[(])}'
		result = isBalanced(string)
		print(result)
	## END
## END

