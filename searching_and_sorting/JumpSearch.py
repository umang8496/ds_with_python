#It is a searching algorithm for sorted arrays.
#The basic idea is to check fewer elements than linear search by jumping ahead by fixed steps.
#Time Complexity O(n^1/2)


import math as m
import random as rd

def BubbleSort(array):
     length = len(array)
     
     for i in range(length):
          for k in range(0,length-1):
               if array[k]>array[k+1]:
                    array[k],array[k+1] = array[k+1],array[k]

     #print("ID value :",id(array))
     return array   

def JumpSearch(array,element):
     length = len(array)
     step = int(m.sqrt(length))
     prev = 0

     for i in range(0,length,4):
          if array[i] == element:
               return i

          elif array[i] < element:
               prev += 1
               #print(prev)

          elif array[i] > element:
               for k in range(i//prev,i):
                    if array[k] == element:
                         return k

          else:
               continue
          
     return -1


#################################################
if __name__ == "__main__":
     #array = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610]
     #element = 55
     array = [rd.randint(1,100) for x in range(20)]

     BubbleSort(array)

     print("The Current Array is :",array)
     element = int(input("enter the element to be searched for : "))
     
     index = JumpSearch(array,element)

     if index != -1:
          print("Element found at index :",index)
     else:
          print("Element Not Found!!")
