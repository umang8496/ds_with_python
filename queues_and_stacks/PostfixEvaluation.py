# Algorithm :
# Scan from Left to Right and repeat the following if steps:
# TOKEN         OPERATION
# operand       add to stack
# operator      pop stack into n1
#               pop stack into n2
#               perform n3 = n2 operator n1
#               push n3 into the stack
# pop the stack to get the resultant value

class PostfixEvaluation:
    stack = []
    TopOfStack = -1

    def push(self,ch):
        self.stack.append(ch)
        # print(ch,"is pushed into the stack")
        self.TopOfStack = self.TopOfStack + 1

    def pop(self):
        element = self.stack[self.TopOfStack]
        self.TopOfStack = self.TopOfStack - 1
        del self.stack[-1]
        # print(element,"is popped")
        # print("stack :",self.stack)
        return element

    def getResult(self,ch,n1,n2):
        if ch == "+":
            return int(n2) + int(n1)
        elif ch == "-":
            return int(n2) - int(n1)
        elif ch == "*":
            return int(n2) * int(n1)
        elif ch == "/":
            return int(n2) / int(n1)
        elif ch == "^":
            return int(n2) ** int(n1)
        elif ch == "$":
            return int(n2) ** int(n1)
        else:
            return -1

if __name__ == "__main__":
    # print("Enter the postfix notation to be evaluated.")
    # postfix = list(input())

    n1,n2,n3 = 0,0,0
    # postfix = list("42^3*3-84/11+/+")
    postfix = list("632-5*+1$7+")
    # postfix = list("42^")

    pe = PostfixEvaluation()
    for i in range(len(postfix)):
        ch = postfix[i]
        if ch.isnumeric():
            pe.push(ch)
        else:
            n1 = pe.pop()
            n2 = pe.pop()
            n3 = pe.getResult(ch,n1,n2)
            pe.push(n3)
    print("Postfix Notation :","".join(postfix))
    print("Evaluated Result :",pe.pop())