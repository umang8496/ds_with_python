class InToPost:
    stack = []
    TopOfStack = -1

    def push(self, operator):
        self.TopOfStack = self.TopOfStack + 1
        self.stack.append(operator)

    def pop(self):
        element = self.stack[self.TopOfStack]
        self.TopOfStack = self.TopOfStack - 1
        del self.stack[-1]
        return element

    def priority(self, ch):
        if (ch == "$" or ch == "^"):
            return 4
        elif (ch == "*" or ch == "/" or ch == "%"):
            return 3
        elif (ch == "+" or ch == "-"):
            return 2
        else:
            return -1

class PostEvaluation:
    stack = []
    TopOfStack = -1

    def push(self, ch):
        self.stack.append(ch)
        self.TopOfStack = self.TopOfStack + 1

    def pop(self):
        element = self.stack[self.TopOfStack]
        self.TopOfStack = self.TopOfStack - 1
        del self.stack[-1]
        return element

    def getResult(self, ch, n1, n2):
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
    # print("Enter the Infix Expression")
    # infix = list(input())
    # infix = list("a$b*c-d+e/f/(g+h)")

    infix = list("4$2*3-4+49/7/(3+4)")
    postfix = []
    n1, n2, n3 = 0, 0, 0

    intopost = InToPost()
    postevaluation = PostEvaluation()

##############################################################################

    for i in range(len(infix)):
        ch = infix[i]

        if ch.isalpha() or ch.isnumeric():
            postfix.append(ch)
        else:
            if ch == "(":
                intopost.push(ch)

            elif (ch == "+" or ch == "-" or ch == "*" or ch == "/" or ch == "$" or ch == "%"):
                while (intopost.priority(ch) <= intopost.priority(intopost.stack[intopost.TopOfStack])):
                    postfix.append(intopost.pop())
                    intopost.push(ch)

            elif (ch == ")"):
                while True:
                    x = intopost.pop()
                    if x == "(":
                        break
                    postfix.append(x)

    while intopost.TopOfStack != 0:
        postfix.append(intopost.pop())

    # So far, infix expression has been converted into postfix expression
##############################################################################

    for i in range(len(postfix)):
        ch = postfix[i]
        if ch.isnumeric():
            postevaluation.push(ch)
        else:
            n1 = postevaluation.pop()
            n2 = postevaluation.pop()
            n3 = postevaluation.getResult(ch,n1,n2)
            postevaluation.push(n3)
##############################################################################

    print("Infix Expression :","".join(infix))
    print("Postfix Expression :","".join(postfix))
    print("Evaluated Postfix Expression :",postevaluation.pop())