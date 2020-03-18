#LinearSearch
#It searches for a value stored in an array or list.
#It does so by going through each value in the array until it gets the required one.
#The array need not to be sorted for implementing this searching algorithm.
#Worst Case Time Complexity is O(n)
#Best Case Time Complexity is O(1)

#array=[1,4,9,16,25,36,49,64,81,100]

def LinearSearch(array, entity):
     for i in range(len(array)):
          if array[i]==entity:
               #print("item found at position",i+1)
               return i
     return -1

###############################################

if __name__ == "__main__":
     array=[4,64,1,16,25,36,9,49,81,100]
     print("the array has following values stored in it...")
     print(array[:])

     entity = int(input("enter the item to be searched for..."))

     pos = LinearSearch(array, entity)

     if pos != -1:
          print("Element found at position",pos)
     else:
          print("Element Not Found")
