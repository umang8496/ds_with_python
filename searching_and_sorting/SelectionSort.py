#Selection Sort
# This algorithm sorts an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning.
#This maintains two subarrays in a given array
#(a) The subarray which is already sorted
#(b) Remaining subarray which is unsorted

#In every iteration of selection sort, the minimum element from the unsorted subarray is picked and moved to the sorted subarray.

#Time Complexity is O(n^2)
#Auxiliary Space O(1)

import random as rd

def SelectionSort(array):
     length = len(array)
     
     for i in range(length):
          pos = i
          for k in range(i+1,length):
               if array[pos] > array[k]:
                    pos = k
          array[i],array[pos] = array[pos],array[i]
               

if __name__ == "__main__":
     array = [87, 54, 89, 21, 68, 19, 96, 38, 37, 50, 12, 77, 81, 85, 16, 9, 19, 95, 77, 89]
     #array = [rd.randint(1,100) for i in range(20)]
     
     print("The unsorted array :",array)

     SelectionSort(array)

     print("The Sorted array :",array)
