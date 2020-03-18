# Execution Time : 0.11590051651000977

import time

#lower = int(input("Enter lower bound: "))
#upper = int(input("Enter upper bound: "))

lower, upper = 1, 10000
start_time = time.time()

print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper+1):
    flag = 1
    if num == 1:
        continue
    if num == 2:
        print(num)
    if num % 2 != 0:
        for i in range(2, (int(num**(1/2)+2))):
            if num % i == 0:
                flag = flag+1
        if flag == 1:
            print(num)

print("Execution Time : "+str((time.time()-start_time)))
