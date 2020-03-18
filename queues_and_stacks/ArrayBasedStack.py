class MyStack():
    stack = []
    top = -1

    def push(self,element):
        self.stack.append(element)
        self.top += 1
        print(element,"pushed to stack")

    def pop(self):
        if(self.top == -1):
            print("Stack is Empty")
            return
        else:
            element = self.stack[self.top]
            del self.stack[self.top]
            self.top -= 1
            print(element,"is popped out of stack")

    def size(self):
        print("Current Size of the Stack is :",self.top+1)

    def display(self):
        print("Current Stack Status")
        print(self.stack)

    def peek(self):
        '''it returns the topmost element of the stack'''
        print("Peek Element is :",self.stack[self.top])

if __name__ == "__main__":
    stk = MyStack()
    print("Put elements into Stack.")
    while True:
        element = input()
        if element == "":
            break;
        else:
            stk.push(element)

    print()
    stk.display()
    stk.peek()
    print()
    stk.pop()
    stk.peek()
    stk.pop()
    print()
    stk.peek()
    stk.display()
    stk.peek()
    stk.size()