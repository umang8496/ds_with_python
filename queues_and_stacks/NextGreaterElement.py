# Provided a set of elements in stack,
# we have to find the next greater element wrt the entered element in the stack
# if the entered element is maximum itself then return -1
# also if the entered element is found at the bottom of the stack then return -1

# if input is [4,5,2,13,8] then
# 4->5
# 5->13
# 2->13
# 13->-1
# 8->-1

# Asked in: Amazon,Informatica,Payu,Samsung,Snapdeal

class NextGreaterElement:
    stack = []
    TopOfStack = -1

    def push(self,number):
        self.stack.append(number)
        self.TopOfStack = self.TopOfStack + 1

    def pop(self):
        if self.TopOfStack == -1:
            print("stack underflow")
        else:
            return self.stack[self.TopOfStack]

    def display(self):
        print(self.stack)

    def findNGE(self,num):
        top = self.TopOfStack
        i = 0
        while i != top + 1:
            stackValue = self.pop()
            self.TopOfStack = self.TopOfStack - 1
            if num < stackValue:
                print(stackValue,"is the next greater element.")
                break

    def size(self):
        return self.TopOfStack + 1

if __name__ == "__main__":
    nge = NextGreaterElement()

    print("Enter a set of numbers")
    while True:
        number = input()
        if number == "":
            break
        else:
            nge.push(int(number))

    print(nge.display())

    print("Enter a number from available in the stack.")
    num = int(input())

    nge.findNGE(num)
    