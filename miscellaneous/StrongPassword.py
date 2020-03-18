#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(length, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = list("!@#$%^&*()-+")

    isNumberAvailable = 0
    isUppercaseLetterAvailable = 0
    isLowercaseLetterAvailable = 0
    isSpecialCharacterAvailable = 0

    for ch in password:
        if((ord(ch) >= 48) and (ord(ch) <= 57)):
            isNumberAvailable = 1
        elif((ord(ch) >= 65) and (ord(ch) <= 90)):
            isUppercaseLetterAvailable = 1
        elif((ord(ch) >= 97) and (ord(ch) <= 122)):
            isLowercaseLetterAvailable = 1
        elif(ch in special_characters):
            isSpecialCharacterAvailable = 1
        else:
            pass
        ## END
    ## END
    
    types_not_satisfied = (4 - (isNumberAvailable + isUppercaseLetterAvailable + isLowercaseLetterAvailable + isSpecialCharacterAvailable))

    if((length + types_not_satisfied) < 6):
        return 6 - length
    else:
        return types_not_satisfied
    ## END
## END


if __name__ == '__main__':
    password = input('enter the password : ')
    answer = minimumNumber(len(password), password)
    print(answer)
## END
