# Reverse a string using stack
class Reverse():
    stack = []
    TopOfStack = -1

    def push(self,data):
        self.stack.append(data)
        self.TopOfStack = self.TopOfStack + 1

    def pop(self):
        return self.stack[self.TopOfStack]

    def StringReverse(self,str):
        # first push all the string characters into the stack
        for i in range(len(str)):
            self.push(str[i])

        # this will contain all the popped up elements of the stack
        mylist = []

        # this will go until stack becomes empty
        while self.TopOfStack != -1:
            data = self.stack.pop()
            mylist.append(data)
            self.TopOfStack = self.TopOfStack - 1

        return "".join(mylist)

# Driver Code
if __name__ == "__main__":
    print("Enter a String to get its reverse String.")
    str = input()

    object = Reverse()
    reverseString = object.StringReverse(str)
    print("Reversed String :", reverseString)