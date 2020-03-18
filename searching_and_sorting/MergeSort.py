#Iterative Implementation of Merge Sort

import random as rd

def MergeSort(array):
     length = len(array)
     if length < 2:
          return array

     middle = length//2
     left = MergeSort(array[:middle])
     right = MergeSort(array[middle:])

     return Merge(left,right)

def Merge(left,right):
     if not len(left) or not len(right):
          return left or right
 
     result = []
     i, j = 0, 0
     while (len(result) < len(left) + len(right)):
          if left[i] < right[j]:
               result.append(left[i])
               i += 1
          else:
               result.append(right[j])
               j += 1

          if i == len(left) or j == len(right):
               result.extend(left[i:] or right[j:])
               break
 
     return result

if __name__ == "__main__":
     #array = [rd.randint(1,100) for i in range(10)]
     array = [26, 34, 79, 89, 47, 24, 60, 14, 84, 21, 1, 97]#, 78, 54, 47, 18, 2, 84, 15, 70]

     print("unsorted array :",array)
     lower = 0
     upper = len(array)-1
     array = MergeSort(array)
     print("sorted array :",array)
