#FindingDuplicates

def findDuplicates(array):
     length = len(array)
     dt = {}
     
     for i in range(length):
          tmp = array[i]
          for j in range(length):
               if(i==j):
                    continue
               else:
                    if(tmp ^ array[j] == 0):
                         if(dt.get(tmp) != 0):
                              dt[tmp] = 0
                    ##END
               ##END
          ##END
     ##END
     duplicate = dt.keys()
     return(list(duplicate))
##END

          
if __name__ == "__main__":
     #array = [1,2,3,1,3,6,6]
     array = [2,4,5,2,4]
     duplicates = findDuplicates(array)
     print(duplicates)
##END
