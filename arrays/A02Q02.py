largest=0
second_largest=0

n=int(input("enter the numbers"))
while(n!=-1):
     if(largest<n):
          second_largest=largest
          largest=n
     elif(second_largest<n & n<largest):
          second_largest=n
     n=int(input())

print("largest value is",largest)
print("second largest value is",second_largest)
