#Binary Search Recursive Implementation

import random as rd

def BubbleSort(array):
     length = len(array)
     
     for i in range(length):
          for k in range(0,length-1):
               if array[k]>array[k+1]:
                    array[k],array[k+1] = array[k+1],array[k]

     #print("ID value :",id(array))
     return array          

def BinarySearch(array,element,lower,upper):
     if lower <= upper:
          mid = int((lower+upper)/2)

          if array[mid] == element:
               return mid

          elif array[mid] > element:
               upper = mid - 1
               return BinarySearch(array,element,lower,upper)

          else:
               lower = mid + 1
               return BinarySearch(array,element,lower,upper)
     else:
          #Element Not Found
          return -1
     


if __name__ == "__main__":
     array = [rd.randint(1,100) for i in range(10)]

     array.sort()

     print("the sorted array being searched for :",array)
     entity = int(input("enter the element to be searched for: "))

     lower = 0
     upper = len(array)-1
     
     pos = BinarySearch(array,entity,lower,upper)

     if pos != -1:
          print("Element Found at Index :",pos)
     else:
          print("Element Not Found")
