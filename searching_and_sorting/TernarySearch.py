#Ternary Search
#It is quite similar to the Binary Search, except it has two middle values.

def TernarySearch(array,element):
     length = len(array)
     lower = 0
     upper = length - 1

     while(upper >= 1):
          mid1 = int(lower + (upper - lower)/3)
          mid2 = int(upper - (upper - lower)/3)

          if array[mid1] == element:
               return mid1
          if array[mid2] == element:
               return mid2

          if array[mid1] > element:
               upper = mid1 - 1
          elif array[mid2] > element:
               lower = mid2 + 1
          else:
               lower = mid1 + 1
               upper = mid2 - 1
     return -1


if __name__ == "__main__":
     array = [9, 12, 16, 19, 21, 37, 38, 50, 54, 68, 77, 81, 85, 87, 89, 89, 95, 96]
     print("sorted array :",array)
     element = 81

     index = TernarySearch(array,element)

     if index != -1:
          print("Element Found at Index :",index)
     else:
          print("Element Not Found")
