#Randomized Quick Sort
#This has the Time Complexity of O(nlogn) for all cases.
#This algorithm is a slight modification over the Recursive Quick Sort.

import random as rd

def RandomizedQuickSort(array,lower,upper):
     if(lower < upper):
          r = rd.randint(lower,upper)
          array[r],array[upper] = array[upper],array[r]
          
          pindex = Partition(array,lower,upper)

          RandomizedQuickSort(array,lower,pindex-1)
          RandomizedQuickSort(array,pindex+1,upper)


def Partition(array,lower,upper):
     pivot = array[upper]
     pindex = lower

     for i in range(lower,upper):
          if(array[i] <= pivot):
               array[i],array[pindex] = array[pindex],array[i]
               pindex += 1

     array[pindex],array[upper] = array[upper],array[pindex]
     return pindex


if __name__ == "__main__":
     #array = [rd.randint(1,100) for x in range(20)]
     array = [91, 51, 100, 96, 90, 45, 34, 71, 24, 90, 82, 67, 71, 19, 2, 59, 13, 94, 19, 24]
     print("Unsorted Array :",array[:])

     RandomizedQuickSort(array,0,len(array)-1)

     print("Sorted Array :",array[:])

