#BubbleSort
#It is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
#Time Complexity O(n^2)

import random as rd

def BubbleSort(array):
     length = len(array)
     
     for i in range(length):
          for k in range(0,length-1):
               if array[k]>array[k+1]:
                    array[k],array[k+1] = array[k+1],array[k]
                    #print("for k =",k,array)
                    #print()
          print("for i =",i,array)

     #print("ID value :",id(array))
     return array           

###########################################

if __name__ == "__main__":
     #array = [rd.randint(1,100) for i in range(10)]
     array = [8,7,6,5,4,3,2,1]
     print("the unsorted array :",array[:])
     #print("ID value :",id(array))
     
     BubbleSort(array)

     print("the sorted array :",array[:])
##END
