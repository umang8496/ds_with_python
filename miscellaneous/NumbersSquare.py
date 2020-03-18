def numbersSquare(n, s):
     row_element = [x for x in range(1,(2*n-1),2)]
     col_element = [x for x in range(3,(2*n),2)]

     #print("row_element",row_element)
     #print("col_element",col_element)
     
     for i in range(0,n,1):
          tmp = s
          print(tmp,end=" ")

          for j in range(0,(n-1),1):
               tmp = tmp + row_element[j]
               print(tmp,end = " ")

          if i != (n-1):
               row_element[i] = -1
               s = s + col_element[i]

          print()
     
##END


if __name__ == "__main__":
     n = 10 #5
     s = 4  #1
     numbersSquare(n,s)
##END
