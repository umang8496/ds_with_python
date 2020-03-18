#The Interpolation Search is an improvement over Binary Search
#where the values in a sorted array are uniformly distributed.

#Binary Search always goes to middle element to check.
#On the other hand interpolation search may go to different locations according the value of key
#being searched.
#For example if the value of key is closer to the last element, interpolation search is likely
#to start search toward the end side.


##     To find the position to be searched:
##     pos = lo + [(x-arr[lo])*(hi-lo)/(arr[hi]-arr[Lo])]
##
##     arr[] ==> Array where elements need to be searched
##     x     ==> Element to be searched
##     lo    ==> Starting index in arr[]
##     hi    ==> Ending index in arr[]

##     array = [1, 10, 29, 34, 37, 38, 38, 39, 39, 46, 47, 51, 52, 60, 69, 78, 82, 93, 97, 99]
##     x = 60

##     for i=1: lo=1 x=60 hi=19 pos=11 array[pos]=47 array[lo]=1 array[hi]=99  array[pos]<x
##     lo=pos+1  else hi=pos-1
##
##     for i=2: lo=12 x=60 hi=19 pos=13 array[pos]=60 array[lo]=51 array[hi]=99 array[pos]=x

def InterpolationSearch(array,element):
    lo = 0
    length = len(array)
    hi = length - 1
  
    while lo <= hi and element >= array[lo] and element <= array[hi]:
        pos  = lo + int(((float(hi - lo) / ( array[hi] - array[lo])) * ( element - array[lo])))
 
        # Condition of target found
        if array[pos] == element:
            return pos
  
        # If element is larger, element is in upper part
        if array[pos] < element:
            lo = pos + 1
  
        # If element is smaller, element is in lower part
        else:
            hi = pos - 1
     
    return -1


if __name__ == "__main__":
     #array = [1, 10, 29, 34, 37, 38, 38, 39, 39, 46, 47, 51, 52, 60, 69, 78, 82, 93, 97, 99]
     #element = 60

     index = InterpolationSearch(array,element)

     if index != -1:
          print("Element Found at Index :",index)
     else:
          print("Element Not Found")
