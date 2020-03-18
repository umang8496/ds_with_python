
#!/bin/python3

# Complete the largestRectangle function below.
def largestRectangle(array):
    length_of_array = len(array)
    i = 1
    array.sort()
    largest_rectangle = 0
    for k in range(-1, -(length_of_array+1), -1):
        current_largest = (array[k] * i)
        # print(current_largest)
        i += 1
        if(largest_rectangle < current_largest):
            largest_rectangle = current_largest
        ## END
    ## END
    return largest_rectangle
## END

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input())
    # h = list(map(int, input().rstrip().split()))
    h = list(map(int, "8979 4570 6436 5083 7780 3269 5400 7579 2324 2116".rstrip().split()))
    result = largestRectangle(h)
    print(str(result) + '\n')
