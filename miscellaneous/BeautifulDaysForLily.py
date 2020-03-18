
def beautifulDays(i, j, k):
    number_of_beautiful_days = 0
    for Num in range(i,j+1):
        reverseNum = getReversedNumber(Num)
        delta = abs(Num - reverseNum)
        if((delta % k) == 0):
            number_of_beautiful_days += 1
        ## END
    ## END
    return number_of_beautiful_days
## END

def getReversedNumber(number):
    reversedNumber = 0
    while(number != 0):
        remainder = number%10
        reversedNumber = reversedNumber*10 + remainder
        number = number//10
    ## END
    return reversedNumber
## END

if __name__ == "__main__":
    result = beautifulDays(20,23,6)
    print(result)
## END
