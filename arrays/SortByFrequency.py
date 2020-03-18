# Given an array of integers, sort the array according to frequency of elements.
# For example, if the input array is {2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12},
# then modify the array to {3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5}.

# Asked in: Oracle,Zycus

def SortByFrequency(arr):
    aux = {}
    for num in arr:
        if(num in list(aux.keys())):
            aux[num] += 1
        else:
            aux[num] = 1

    output = []
    while(len(aux.keys())):
        max_freq = max(aux.values())
        for k in list(aux.keys()):
            #print("k :",k)
            if(aux[k] == max_freq):
                tmp = [k]*max_freq
                output.extend(tmp)
                del(aux[k])

    return output
##END

if __name__ == "__main__":
    arr = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
    frequency_sorted = SortByFrequency(arr)
    print(frequency_sorted)
##END
