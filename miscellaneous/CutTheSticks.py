
def cutTheSticks(arr):
    result = []

    for _ in range(len(arr)):
        MIN = findMIN(arr)
        ctr = 0
        for i in range(len(arr)):
            if(MIN == None):
                break
            if(arr[i] >= MIN):
                arr[i] = arr[i] - MIN
                ctr += 1
            ## END
        ## END
        if(ctr != 0):
            result.append(ctr)
        else:
            break
        ## END
    ## END
    return result
## END

def findMIN(arr):
    MIN = None
    for val in arr:
        if(val == 0):
            continue
        else:
            if(MIN == None):
                MIN = val
            else:
                if(MIN > val):
                    MIN = val
                ## END
            ## END
        ## END
    ## END
    return MIN
## END

if __name__ == '__main__':
    # arr = list(map(int, input().rstrip().split()))
    # arr = [5,4,4,2,2,8]
    arr = [1,2,3,4,3,3,2,1]
    result = cutTheSticks(arr)
    print(result)
