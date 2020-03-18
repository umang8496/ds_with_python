# size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# import string
# alpha = string.ascii_lowercase

# print("Enter size : ",end='')
# n = int(input())
# L = []

# for i in range(n):
#     s = "-".join(alpha[i:n])
#     L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
# print('\n'.join(L[:0:-1]+L))


N = int(input("Enter the size : "))

if (N <= 0 or N >=27):
	exit()
## END

#N = 5
width = ((4*N)-3)
rows = ((2*N)-1)
counter = ((2*N)-1)

for i in range(1,rows+1):
	if (i == N):
		alpha = 97 + N
		for k in range(1,width+1):
			if(k % 2 != 0):
				if (k > (2*N-1)):
					alpha = (alpha+1)
				else:
					alpha = (alpha-1)
				## END
				print(chr(alpha),end='')
			else:
				print('-',end='')
			## END
		## END
	else:
		alpha = 97 + N
		for k in range(1,width+1):
			if (k == 1 or (k%2 == 0) or k == width):
				print('-',end='')
			else:
				if (k < counter):
					print('-',end='')
				else:
					if (k > (2*N-1)):
						if ((width-k+1) < counter):
							print('-',end='')
							continue
						## END
						alpha = (alpha+1)
						print(chr(alpha),end='')
					else:
						alpha = (alpha-1)
						print(chr(alpha),end='')
					## END
				## END
			## END
		## END
	## END
	if (i < N):
		counter -= 2
	else:
		counter += 2
	print()
## END



