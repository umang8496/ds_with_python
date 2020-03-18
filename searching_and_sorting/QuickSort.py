#Quick sort is based on the divide-and-conquer approach based on the idea of choosing one element as a pivot element and partitioning the array around it such that: Left side of pivot contains all the elements that are less than the pivot element Right side contains all elements greater than the pivot

#It reduces the space complexity and removes the use of the auxiliary array that is used in merge sort. Selecting a random pivot in an array results in an improved time complexity in most of the cases.

#The worst case time complexity of this algorithm is O(n^2)
#but as this is randomized algorithm, its time complexity fluctuates between O(n^2) and O(nlogn)
#and mostly it comes out to be O(nlogn).


def QuickSort(array,lower,upper):
     if(lower < upper):
          pindex = Partition(array,lower,upper)

          QuickSort(array,lower,pindex-1)
          QuickSort(array,pindex+1,upper)

def Partition(array,lower,upper):
     pindex = lower
     pivot = array[upper]

     #Initial Values : [7,0,5,4,3,2,1,6]
     #for i=0 : [0,7,5,4,3,2,1,6]  pindex=0
     #for i=1 : [0,7,5,4,3,2,1,6]  pindex=1
     #for i=2 : [0,5,7,4,3,2,1,6]  pindex=2
     #for i=3 : [0,5,4,7,3,2,1,6]  pindex=3
     #for i=5 : [0,5,4,3,7,2,1,6]  pindex=4
     #for i=6 : [0,5,4,3,2,7,1,6]  pindex=5
     #for i=7 : [0,5,4,3,2,1,7,6]  pindex=6

     for i in range(lower,upper):
          if(array[i] <= pivot):
               array[i],array[pindex] = array[pindex],array[i]
               pindex += 1

     array[pindex],array[upper] = array[upper],array[pindex]

     return pindex


if __name__ == "__main__":
     #array = [7,0,5,4,3,2,1,6]
     array = [7,6,5,4,3,2,1,0]
     lower = 0
     upper = len(array) - 1

     print("The Unsorted array :",array)
     
     QuickSort(array,lower,upper)

     print("The Sorted array :",array)
