def hourglassSum(arr):
     sum = 0
     i_base = [0,0,0,1,2,2,2] 
     j_base = [0,1,2,1,0,1,2]
    
     for a in range(4):
          for b in range(4):
               tmp = 0
               for i,j in list(zip(i_base,j_base)):
                    tmp += arr[i+a][j+b]
                    print(i+a,j+b,end=",  ")
                    if sum < tmp :
                         sum = tmp
               print()
     return sum
##END

if __name__ == "__main__":
     arr = [[-9,-9,-9,1,1,1],
            [0,-9,0,4,3,2],
            [-9,-9,-9,1,2,3],
            [0,0,8,6,6,0],
            [0,0,0,-2,0,0],
            [0,0,1,2,4,0]]

     hg = hourglassSum(arr)

     print(hg)
##END
