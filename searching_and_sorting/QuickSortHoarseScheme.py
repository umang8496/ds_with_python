##def quicksort(x):
##    if len(x) == 1 or len(x) == 0:
##        return x
##    else:
##        pivot = x[0]
##        i = 0
##        for j in range(len(x)-1):
##            if x[j+1] < pivot:
##                x[j+1],x[i+1] = x[i+1], x[j+1]
##                i += 1
##        x[0],x[i] = x[i],x[0]
##        first_part = quicksort(x[:i])
##        second_part = quicksort(x[i+1:])
##        first_part.append(x[i])
##        return first_part + second_part

##def quicksort(x):
##    if len(x) == 1 or len(x) == 0:
##        return x
##    else:
##        pivot = x[0]
##        i = 0
##        for j in range(len(x)-1):
##            if x[j+1] < pivot:
##                x[j+1],x[i+1] = x[i+1], x[j+1]
##                i += 1
##        x[0],x[i] = x[i],x[0]
##        first_part = quicksort(x[:i])
##        second_part = quicksort(x[i+1:])
##        first_part.append(x[i])
##        return first_part + second_part

def quicksort(x):
      if len(x) < 2:
          return x
      else:
          pivot = x[0]
          less = [i for i in x[1:] if i <= pivot]
          greater = [i for i in x[1:] if i > pivot]
          return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == "__main__":
    array = [7,6,5,4,3,2,1,0]
    print("unsorted array",array)
    quicksort(array)
    print("sorted array",array)
