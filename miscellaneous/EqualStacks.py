# You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height.
# You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

# Find the maximum possible height of the stacks such that all of the stacks are exactly the same height.
# This means you must remove zero or more cylinders from the top of zero or more of the three stacks
# until they're all the same height, then print the height.
# The removals must be performed in such a way as to maximize the height.

# Note: An empty stack is still a stack.

# Print a single integer denoting the maximum height at which all stacks will be of equal height.

# https://www.hackerrank.com/challenges/equal-stacks/problem

def reverseTheList(arr, length_of_arr):
	mid_index = (length_of_arr//2)
	if(length_of_arr % 2 == 0):
		for i in range(mid_index):
			tmp = arr[i]
			arr[i] = arr[-(i+1)]
			arr[-(i+1)] = tmp
		## END
	else:
		for i in range(mid_index):
			tmp = arr[i]
			arr[i] = arr[-(i+1)]
			arr[-(i+1)] = tmp
		## END
	## END
	return arr
## END


def alterTheListElements(arr, length_of_arr):
	sum_till_ith_idx = 0
	for i in range(length_of_arr):
		sum_till_ith_idx += arr[i]
		arr[i] = sum_till_ith_idx
	## END
	return arr
## END


def getSmallestList(list1, list2, list3):
	smallest_size = min(list1[1], list2[1], list3[1])

	if(smallest_size == list1[1]):
		return (list1, list2, list3)
	elif(smallest_size == list2[1]):
		return (list2, list1, list3)
	else:
		return (list3, list2, list1)
	## END
## END


def checkIfValueExistsInOtherLists(value, arr_one, arr_two):
	if(value in arr_one and value in arr_two):
		return True
	else:
		return False
	## END
## END


def getTheMaxHeightForAllStack(arr1, arr2, arr3):
	length_of_arr1 = len(arr1)
	length_of_arr2 = len(arr2)
	length_of_arr3 = len(arr3)

	((smallest_arr, length_of_smallest_arr),(arr_one, length_of_arr_one),(arr_two, length_of_arr_two)) = getSmallestList((arr1, length_of_arr1), (arr2, length_of_arr2), (arr3, length_of_arr3))	
	# () = getOtherTwoLists((arr1, length_of_arr1), (arr2, length_of_arr2), (arr3, length_of_arr3), (smallest_arr, length_of_smallest_arr))

	reverseTheList(smallest_arr, length_of_smallest_arr)
	reverseTheList(arr_one, len(arr_one))
	reverseTheList(arr_two, len(arr_two))

	smallest_arr = alterTheListElements(smallest_arr, length_of_smallest_arr)
	arr_one = alterTheListElements(arr_one, length_of_arr_one)
	arr_two = alterTheListElements(arr_two, length_of_arr_two)

	smallest_arr = reverseTheList(smallest_arr, length_of_smallest_arr)

	for value in smallest_arr:
		if(checkIfValueExistsInOtherLists(value, arr_one, arr_two)):
			return value
		## END
	## END
	return 0
## END


if __name__ == '__main__':
	arr1 = [3,2,1,1,1]
	arr2 = [4,3,2]
	arr3 = [1,1,4,1]
	result = getTheMaxHeightForAllStack(arr1, arr2, arr3)
	print(result)
## END


# 99968