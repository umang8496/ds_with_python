# BinaryInsertionSort.py

#Insertion Sort
#Time Complexity is O(n^2)

import random as rd
import profile as prf

def InsertionSort(array):
	for i in range(1,len(array)):
		k = i-1
		key = array[i]

		while(k >= 0 and key < array[k]):
			array[k+1] = array[k]
			k = k - 1
		array[k+1] = key
	## END
## END

def main():
	# array = [9,8,7,6,5,4,3,2,1,0]
	array = [57, 33, 30, 62, 56, 30, 95, 23, 46, 60, 84, 53, 86, 72, 86, 87, 77, 74, 80, 17]
	# array = [26, 34, 79, 89, 47, 24, 60, 14, 84, 21, 1, 97, 78, 54, 47, 18, 2, 84, 15, 70]
	# array = [62, 83, 8, 19, 85, 94, 26, 9, 55, 92, 46, 82, 83, 9, 22, 2, 94, 39, 96, 27]
	print("Unsorted Array :",array)
	InsertionSort(array)
	print("Sorted Array :",array)
## END


if __name__ == "__main__":
    print()
    main()
    # print(prf.run("main()"))
## END

#21160



