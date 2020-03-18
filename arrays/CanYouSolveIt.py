# Raman loves Mathematics a lot. One day his maths teacher gave him an interesting problem.
#
# He was given an array 'A' consisting of 'n' integers,
# he was needed to find the maximum value of the following expression:
#
# |Ai - Aj| + |i - j|
#
# where, 0<= i,j <n and Ai, Aj are the Array elements.

import sys

def getMaxOfExpr(num):
    max1, max2 = -(sys.maxsize+1), -(sys.maxsize+1)
    min1, min2 = (sys.maxsize), (sys.maxsize)

    for i in range(len(array)):
        if((num[i] + i) > max1):
            max1 = (num[i] + i)
        if((num[i] + i) < min1):
            min1 = (num[i] + i)
        if((num[i] - i) > max2):
            max2 = (num[i] - i)
        if((num[i] - i) < min2):
            min2 = (num[i] - i)
    print(max(max1-min1, max2-min2))

if __name__ == "__main__":
    # array = [13, 58, 31, 80, 48, 4, 51, 92, 67, 6, 2, 67, 94, 97, 76, 57, 55, 19, 98, 63]  # 107
    array = [1,2,3,4,5]
    getMaxOfExpr(array)
# END
