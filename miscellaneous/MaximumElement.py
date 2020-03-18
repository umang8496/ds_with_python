
# You have an empty sequence, and you will be given N queries. Each query is one of these three types:

# 1 x  -Push the element x into the stack.
# 2    -Delete the element present at the top of the stack.
# 3    -Print the maximum element in the stack.

import sys

class MyStackImpl():
	def __init__(self):
		self.stack = []
		self.top = -1
		self.current_max = -(sys.maxsize+1)
	## END

	def push(self, ch):
		self.top += 1
		if(self.current_max < ch):
			self.current_max = ch
		## END
		self.stack.append((ch,self.current_max))
	## END

	def getCurrentMax(self):
		return self.stack[self.top][1]
	## END

	def removeTheTop(self):
		del self.stack[self.top]
		self.top -= 1
		if(self.top == -1):
			self.current_max = -(sys.maxsize+1)
		if(self.top > -1):
			self.current_max = self.stack[self.top][1]
		## END
	## END

	def getSize(self):
		return (self.top + 1)
	## END
## END


if __name__ == '__main__':
	test_cases = int(input())
	stack = MyStackImpl()

	for _ in range(test_cases):
		ab = list(map(int,input().split()))
		if(ab[0] == 1):
			stack.push(ab[1])
		## END
		if(ab[0] == 2):
			stack.removeTheTop()
		## END
		if(ab[0] == 3):
			print(stack.getCurrentMax())
		## END
		print(stack.stack)
	## END
## END
