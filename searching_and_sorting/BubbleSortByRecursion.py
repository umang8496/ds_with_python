#This is the Recursive Implementation of BubbleSort

import random as rd

def RecursiveBS(array,length):
     if length == 1:
          return

     for k in range(length-1):
          if array[k]>array[k+1]:
               array[k],array[k+1] = array[k+1],array[k]

     RecursiveBS(array,length-1)

#############################################

if __name__ == "__main__":
     array = [rd.randint(1,100) for i in range(10)]
     print("the unsorted array :",array[:])
     print("ID value :",id(array))
     
     RecursiveBS(array,len(array))

     print("the sorted array :",array[:])
