# 2dPeakFinder.py

# TEST CASE : 01
# [10  21  34  19]
# [12  20  34  19]
# [24  21  30  19]
# [36  25  34  40]
# [[10,21,34,19],[12,20,34,19],[24,21,30,19],[36,25,34,40]]

# TEST CASE : 02
# [10   8  10  10]
# [14  13  12  11]
# [15   9  11  21]
# [16  17  19  20]
# [[10,8,10,10],[14,13,12,11],[15,9,11,21],[16,17,19,20]]
# OUTPUT : 21


def TwoDimensionalPeakFinder(array_2D, rows, cols):
	mid_col = cols//2
	print('Finding 2D peak')
	return find_two_dimensional_peak(array_2D, rows, cols, mid_col)
## END


def findMax(array_2D, mid_col):
	j = mid_col
	maxval = array_2D[0][j]
	
	for i in range(0,4):
		if (maxval < array_2D[i][j]):
			maxval = array_2D[i][j]
		## END
	## END
	print('maxval :', maxval)
	return (i, j, maxval)
## END


def find_two_dimensional_peak(array_2D, rows, cols, mid_col):
	(i, j, maxval) = findMax(array_2D, mid_col)

	if (j == cols-1):
		if (maxval >= array_2D[i][j-1]):
			return maxval
	elif (j == 0):
		if (maxval >= array_2D[i][j+1]):
			return maxval
	else:
		if (maxval >= array_2D[i][j+1] and maxval >= array_2D[i][j-1]):
			return maxval
		## END
	## END

	# if (j+1 < cols and j >= 0):
	if (maxval < array_2D[i][j+1]):
		return find_two_dimensional_peak(array_2D, rows, cols, j+1)
	else:
		return find_two_dimensional_peak(array_2D, rows, cols, j-1)
	## END
## END


if __name__ == '__main__':
	# array_2D = [[10,8,10,10],[14,13,12,11],[15,9,11,21],[16,17,19,20]]
	array_2D = [[10,21,34,19],[12,20,34,19],[24,21,30,19],[36,25,34,40]]
	rows,cols = 4,4
	peakValue = TwoDimensionalPeakFinder(array_2D, rows, cols)
	print('Peak Value :',peakValue)
## END
