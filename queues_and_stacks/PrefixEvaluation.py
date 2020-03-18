# Algorithm :
# Scan from Right to Left and repeat the following steps
# TOKEN           OPERATION
# operand         add to stack
# operator        pop stack into n1
#                 pop stack into n2
#                 perform n3 = n1 operator n2
#                 push n3 into the stack

class PrefixEvaluation:
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
    # print("Enter the prefix notation to be evaluated.")
    # prefix = list(input())

    n1,n2,n3 = 0,0,0
    # prefix = list("42^3*3-84/11+/+")
    prefix = list("632-5*+1$7+")
    # prefix = list("42^")

    pe = PrefixEvaluation()
    for i in range(len(prefix)):
        ch = prefix[i]
        if ch.isnumeric():
            pe.push(ch)
        else:
            n1 = pe.pop()
            n2 = pe.pop()
            n3 = pe.getResult(ch,n1,n2)
            pe.push(n3)
    print("Prefix Notation :","".join(prefix))
    print("Evaluated Result :",pe.pop())