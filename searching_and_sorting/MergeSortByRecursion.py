#Merge Sort
#It is a divide and conquer algorithm.
#It divides the array into two halves, and calls itself for the two halves and then merges them.
#In all 3 cases, its Time Complexity is O(nlogn)

import random as rd
import profile as prf

def MergeSort(array,lower,upper):
     if lower < upper:
          mid = (lower + upper)//2

          MergeSort(array,lower,mid)
          MergeSort(array,mid+1,upper)
          Merge(array,lower,mid,upper)
     

def Merge(array, lower, mid, upper):
     n1 = mid - lower + 1
     n2 = upper - mid

     L = [0]*n1
     R = [0]*n2

     for i in range(n1):
          L[i] = array[lower + i]

     for j in range(n2):
          R[j] = array[mid + 1 + j]

     i,j,k = 0,0,lower
     
     while(i<n1 and j<n2):
          if L[i] <= R[j]:
               array[k] = L[i]
               i += 1
          else:
               array[k] = R[j]
               j += 1
          k += 1

     while i < n1:
          array[k] = L[i]
          i += 1
          k += 1

     while j < n2:
          array[k] = R[j]
          j += 1
          k += 1


if __name__ == "__main__":
     #array = [rd.randint(1,100) for i in range(10)]
     array = [26, 34, 79, 89, 47, 24, 60, 14, 84, 21, 1, 97]#, 78, 54, 47, 18, 2, 84, 15, 70]

     print("unsorted array :",array)
     lower = 0
     upper = len(array)-1
     MergeSort(array,lower,upper)
     print("sorted array :",array)
     
##     print("\n")
##     print(prf.run("__name__"))
