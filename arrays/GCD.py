def GCD():
     m=int(input("Enter the first number..."))
     n=int(input("Enter the second number..."))
         
     a=max(m,n)
     b=min(m,n)
                    
     divisor=b
     dividend=a
                    
     while divisor!=0:
          remainder=dividend%divisor
          dividend=divisor
          if remainder==0:
               break
          divisor=remainder

     print("the GCD of",a,"and",b,"is",divisor)
