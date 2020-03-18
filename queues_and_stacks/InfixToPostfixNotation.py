# Algorithm :
# Scan from Left to Right and repeat the following if steps:
# TOKEN         OPERATION
# operand       add to the expression
# "("           push to stack
# operator      pop operation
#                   if p(popped) >= p(scanned):
#                       add to expression
#                   push scanned operator to stack
# ")"           pop till "(" and add popped token to expression
#               delete "("
# pop stack elements if any and add to the expression


class InfixToPostfixNotation:
    stack = []
    TopOfStack = -1

    def push(self, operator):
        self.TopOfStack = self.TopOfStack + 1
        self.stack.append(operator)

    def pop(self):
        element = self.stack[self.TopOfStack]
        self.TopOfStack = self.TopOfStack - 1
        # print(element,"popped")
        del self.stack[-1]
        return element

    def priority(self,ch):
        if (ch == "$" or ch == "^"):
            return 4
        elif (ch == "*" or ch == "/" or ch == "%"):
            return 3
        elif (ch == "+" or ch == "-"):
            return 2
        else:
            return -1

if __name__ == "__main__":
    # print("Enter an infix notation")
    # infix = list(input())

    postfix = []
    ip = InfixToPostfixNotation()
    ip.push("#")

    infix = list("a+(b*c-(d/e$f)*g)*h")
    # infix = list("a+b*c-d")     # abc*+d-
    # infix = list("a$b*c-d+e/f/(g+h)")

    for i in range(len(infix)):
        ch = infix[i]
        # print(ch)
        if ch.isalpha():
            postfix.append(ch)
            # print(ch,"sent to postfix")
            # print(postfix)
        else:
            if ch == "(":
                ip.push(ch)

            elif (ch == "+" or ch == "-" or ch == "*" or ch == "/" or ch == "$" or ch == "%"):
                while (ip.priority(ch) <= ip.priority(ip.stack[ip.TopOfStack])):
                    postfix.append(ip.pop())
                ip.push(ch)
                # print(ch,"pushed into stack")

            elif (ch == ")"):
                while True:
                    x = ip.pop()
                    if x == "(":
                        break
                    postfix.append(x)

            else:
                pass

    # print(ip.stack[0:ip.TopOfStack+1])
    while ip.TopOfStack != 0:
        postfix.append(ip.pop())
        # print(postfix[-1])

    print("Infix Notation :","".join(infix))
    print("Postfix Notation :","".join(postfix))