import random as rd

def CountingSort(array):
    length = len(array)
    maximum = max(array)
    auxiliary_array = [0]*(maximum+1)
    sorted_array = [0]*length

    #Store the frequencies of each distinct element of array, by mapping its value as the index of auxiliary_array
    for i in range(length):
        auxiliary_array[array[i]] += 1
    #print(auxiliary_array)

    j = 0
    for i in range(maximum+1):
        count = auxiliary_array[i]
        while(count):
            sorted_array[j] = i
            j += 1
            count -= 1

    return sorted_array
##END

if __name__ == "__main__":
    array = [rd.randint(1, 20) for i in range(10)]
    #array = [13, 6, 12, 19, 18, 2, 16, 9, 9, 8]
    print("unsorted array",array)
    sorted_array = CountingSort(array)
    print("sorted array",sorted_array)
##END