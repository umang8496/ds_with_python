#FibonacciSearch

##In computer science, the Fibonacci search technique is a method of searching a sorted array
##using a divide and conquer algorithm that narrows down possible locations with the aid of
##Fibonacci numbers.
##Compared to binary search where the sorted array is divided into two equal-sized parts,
##one of which is examined further, Fibonacci search divides the array into two parts that
##have sizes that are consecutive Fibonacci numbers.
##On average, this leads to about 4% more comparisons to be executed,
##but it has the advantage that one only needs addition and subtraction to calculate the indices of
##the accessed array elements, while classical binary search needs bit-shift, division or
##multiplication, operations that were less common at the time Fibonacci search was first published.
##Fibonacci search has an average- and worst-case complexity of O(log n).
##
##If the elements being searched have non-uniform access memory storage
##(the time needed to access a storage location varies depending on the location accessed),
##the Fibonacci search may have the advantage over binary search in slightly reducing the average time
##needed to access a storage location.


import random as rd

def FibonacciSearch(array, element, length):
     # Initialize fibonacci numbers 
     fib2 = 0 # (m-2)'th Fibonacci No.
     fib1 = 1 # (m-1)'th Fibonacci No.
     fib = fib2 + fib1 # m'th Fibonacci
 
     # fib is going to store the smallest 
     # Fibonacci Number greater than or equal to n 
     while (fib < length):
          fib2 = fib1
          fib1 = fib
          fib = fib2 + fib1
 
     #offset = 0
     offset = -1
 
     while (fib > 1):
          # Check if fibMm2 is a valid location
          #i = min(offset + fib2, length - 1)
          i = (offset + fib2)

          print(fib,"",fib1,"",fib2,"",offset)
          print("array:",array[i])
               
          # If x is greater than the value at index fib2, cut the subarray array from offset to i 
          if (array[i] < element):
               fib = fib1
               fib1 = fib2
               fib2 = fib - fib1
               offset = i
 
          # If x is greater than the value at index fib2, cut the subarray after i+1
          elif (array[i] > element):
               fib = fib2
               fib1 = fib1 - fib2
               fib2 = fib - fib1
               #offset = i this should not be here
               
          # element found. return index 
          else :
               return i

     if(fib1 == 1 and array[offset+1] == element):
          return offset+1
 
     return -1

# Driver Code
#array = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
#array = [rd.randint(1,10000) for i in range(100)]
#array.sort()

#array = [1, 3, 15, 27, 40, 42, 44, 46, 59, 63, 77]
array = [11,12,13,14,15,16,17,18,19,20]
length = len(array)
print("sorted array :",array)
#element = int(input("element : "))
element = 16
index = FibonacciSearch(array, element, length)

if index != -1:
     print("Element Found at Index :",index)
else:
     print("Element Not Found")
