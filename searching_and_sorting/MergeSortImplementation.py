#Merge Sort Implementation

def MergeSort(array):
     length = len(array)
     if (length < 2):
          return

     mid = length//2
     left = array[:mid]
     right = array[mid:]

##     for i in range(mid):
##          left[i] = array[i]
##          
##     for i in range(mid,length):
##          right[i] = array[i]

     MergeSort(left)
     MergeSort(right)

     Merge(array,left,right)
     

def Merge(array,left,right):
     nL = len(left)
     nR = len(right)

##     i=j=k=0

     i,j,k = 0,0,0
     
     while(i<nL and j<nR):
          if(left[i] <= right[j]):
               array[k] = left[i]
               i += 1
          else:
               array[k] = right[j]
               j += 1
          k += 1

     while(i<nL):
          array[k] = left[i]
          i += 1
          k += 1

     while(j<nR):
          array[k] = right[j]
          j += 1
          k += 1

##     if(i<nL):
##          array.extend(left[i:])
##          i = len(left)
##          k = len(array)
##
##     if(j<nR):
##          array.extend(right[j:])
##          j = len(right)
##          k = len(array)


if __name__ == "__main__":
     array = [2,4,1,6,8,5,3,7]
     
     print("Unsorted Array :",array[:])
     MergeSort(array)
     print("Sorted Array :",array[:])
