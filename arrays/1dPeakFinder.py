# 1dPeakFinder.py

# This program finds the number of peaks and peaks themselves for a list.

# example(1)
# arr1=[61,62,24,28,32,14,36,61,6,12]
# peaks=[62,32,61,12]
# numberofpeaks=4

# example(2)
# arr2=[10,20,15,2,23,90,67]
# peaks=[20,90]
# numberofpeaks=2

# array=[10,20,15,2,23,90,67]
# array=[61,62,24,28,32,14,36,61,6,12]

def PeakFinder():
	array=[61,62,24,28,32,14,36,61,6,12]
	print("Given Array is",array)
	peaks=[]

	if array[0]>array[1]:
			peaks.append(array[0])

	for i in range(1,len(array)-1):
			if array[i]>array[i+1] and array[i]>array[i-1]:
					peaks.append(array[i])

	if array[-1]>array[-2]:
			peaks.append(array[-1])
			
	print("Peaks are",peaks)
	print("Number of peaks",len(peaks))

if __name__ == "__main__":
	#PeakFinder()
	import profile
	profile.run("PeakFinder()")