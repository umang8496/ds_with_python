def getNextGap(gap):
     #Shrink gap by Shrink factor
     #gap = int((gap * 10)/13)
     gap = int(gap/1.25)
     if gap < 1:
          return 1
     return gap
##END

# Function to sort arr[] using Comb Sort
def CombSort(array):
     n = len(array)
     gap = n
 
     # Initialize swapped as true to make sure that loop runs
     swapped = True
     #print(int(swapped))

     # Keep running while gap is more than 1 or last iteration caused a swap
     while gap != 1 or swapped == True:
          gap = getNextGap(gap)
          print("gap",gap)
          swapped = False
 
          # Compare all elements with current gap
          for i in range(0, n-gap):
               if array[i] > array[i+gap]:
                    array[i],array[i+gap] = array[i+gap],array[i]
                    print(array)
                    swapped = True
     ##END
##END


if __name__ == "__main__":
     array = [20,19,18,17,16,15,14,13,12,11]
     CombSort(array)
     print("sorted array:",array)
##END