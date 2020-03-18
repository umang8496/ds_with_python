##Shellsort, also known as Shell sort or Shell's method, is an in-place comparison sort.
##It can be seen as either a generalization of sorting by exchange (bubble sort) or
##sorting by insertion (insertion sort).
##The method starts by sorting pairs of elements far apart from each other,
##then progressively reducing the gap between elements to be compared.
##Starting with far apart elements, it can move some out-of-place elements into position faster
##than a simple nearest neighbor exchange.
##The running time of Shellsort is heavily dependent on the gap sequence it uses.
##For many practical variants, determining their time complexity remains an open problem

##Shellsort is not stable: it may change the relative order of elements with equal values.
##It is an adaptive sorting algorithm in that it executes faster when the input is partially sorted.

def ShellSort(array):
     gap = len(array)//2
     #k = 0
     #gap = (2*k+1)
     while (gap > 0 and gap < len(array)):
          for i in range(gap,len(array)):
               key = array[i]
               j = i
               while (j >= gap)and(array[j-gap] > key):
                    array[j] = array[j-gap]
                    j = j - gap
               array[j] = key
          gap = gap//2
          #k += 1
          #gap = (2*k+1)
     return array
##END

if __name__ == "__main__":
     array = [20,19,18,17,16,15,14,13,12,11]
     print("given array:",array)
     array = ShellSort(array)
     print("sorted array:",array)
##END
