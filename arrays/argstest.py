## argstest

##The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function.
##It is used to pass a non-keyworded, variable length argument list.

def testify(arg1, *argv):
     print("first argument :", arg1)

     for arg in argv:
          print("Next Arguments through *argv :",arg)


if __name__ == "__main__":
     testify("hello","welcome","to","geeksforgeeks")
