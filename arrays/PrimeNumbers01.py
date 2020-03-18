# Execution Time : 5.646524906158447
import time

#lower = int(input("enter the lower bound"))
#upper = int(input("enter the upper bound"))
lower, upper = 1, 10000
start_time = time.time()
count = 1

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    flag = 1
    if num == 1:
        continue
    if num == 2:
        print(num)
    if num % 2 != 0:
        for i in range(2, num):
            if num % i == 0:
                flag = flag + 1
        if flag == 1:
            count += 1
            print(num, end=" ")
print("Execution Time : " + str((time.time() - start_time)))
print("number of primes", count)
