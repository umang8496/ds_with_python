
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(number):
    divisor_counter = 0
    looping_variable = number
    while(looping_variable != 0):
        divisor = (looping_variable % 10)
        looping_variable = (looping_variable // 10)

        if(divisor == 0):
            continue
        else:
            if((number % divisor) == 0):
                divisor_counter += 1
            ## END
        ## END
    ## END
    return divisor_counter
## END

if __name__ == '__main__':
    for t_itr in range(t):
        n = int(input())
        result = findDigits(n)
        print(str(result))