# Algorithm :
# Scan from Right to Left and repeat the following if steps:
# TOKEN         OPERATION
# operand       add to the expression
# ")"           push to stack
# operator      pop operation
#                   if p(popped) > p(scanned):
#                       add to expression
#                   push scanned operator to stack
# "("           pop till ")" and add popped token to expression
#               delete "("
# pop stack elements if any and add to the expression


class InfixToPrefix:
    stack = []
    TopOfStack = -1

    def push(self,operator):
        self.TopOfStack = self.TopOfStack + 1
        self.stack.append(operator)
        print(operator,"pushed into the stack")
        print("stack status :",self.stack)

    def pop(self):
        element = self.stack[self.TopOfStack]
        self.TopOfStack = self.TopOfStack - 1
        del self.stack[-1]
        print(element,"popped out")
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
    intopre = InfixToPrefix()
    intopre.push("#")

    infix = list("a+(b*c-(d/e$f)*g)*h")
    # prefix  : "+a*-*bc*/d$efgh"
    # postfix : "abc*def$/g*-h*+"

    # infix = list("a+b*c-d")
    # prefix  : "-+a*bcd"
    # postfix : "abc*+d-"

    # infix = list("a+(b*c)-d")
    # prefix  : "-+a*bcd"
    # postfix : "abc*+d+"

    prefix = []

    length = len(infix)
    for i in range(-1,-length-1,-1):        # "a+(b*c-(d/e$f)*g)*h"
        ch = infix[i]
        # print("ch : "+ch)
        if ch.isalpha():
            prefix.append(ch)
            print(ch,"appended","-->",prefix)

        elif ch == ")":
            intopre.push(ch)
            # print(ch, "appended")

        elif (ch == "+" or ch == "-" or ch == "*" or ch == "/" or ch == "$" or ch == "^"):
            while intopre.priority(ch) < intopre.priority(intopre.stack[intopre.TopOfStack]):
                prefix.append(intopre.pop())
            intopre.push(ch)

        elif ch == "(":
            while True:
                x = intopre.pop()
                if x == ")":
                    break
                prefix.append(x)

        else:
            pass

    while intopre.TopOfStack != 0:
        prefix.append(intopre.pop())

    print("Infix Notation :", "".join(infix))

    # We have to reverse the content of prefix in order to get the required prefix value
    prefix.reverse()
    print("Prefix Notation :", "".join(prefix))