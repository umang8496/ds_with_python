def CountingSort(aux,exp):
    length = len(array)
    output = [0] * length
    count = [0] * 10

    #array = [10, 21, 17, 34, 44, 11, 654, 123]
    #print("exp",exp)
    for i in range(length):
        index = (array[i] // exp)
        count[(index) % 10] += 1

    print("count",count)

    for i in range(1, 10):
        count[i] += count[i - 1]

    print("count", count)

    i = length - 1
    while i >= 0:
        index = (array[i] // exp)
        output[count[(index) % 10] - 1] = array[i]
        count[(index) % 10] -= 1
        i -= 1

    i = 0
    for i in range(length):
        array[i] = output[i]
##END

def RadixSort(array):
    length = len(array)
    maxx = 0

    #this will determine the maximum value in the array
    for i in range(length):
        if (maxx < array[i]):
            maxx = array[i]
    #maxx = 654

    exp = 1
    while(maxx // exp) > 0:
        CountingSort(array,exp)
        exp *= 10
        print(array)
    ##END

    #while(maxx):
        #print("maxx", maxx)
        #CountingSort(array, exp)
        #maxx = maxx // exp
        #exp *= 10
        #print(array)
    ##END

    return array
##END


if __name__ == "__main__":
    array = [10,21,17,34,44,11,654,123]
    print("Given Array", array)
    output = RadixSort(array)
    #print("Sorted Array", output)
##END