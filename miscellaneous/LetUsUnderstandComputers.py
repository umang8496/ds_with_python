
import math

def getMinimumNumberOfBitsFor(number):
	i = 0
	max_range = 0
	while(True):
		max_range = max_range + 2**i
		if(number <= max_range):
			return (i+1)
		else:
			i += 1
		## END
	## END
## END


if __name__ == '__main__':
    test_cases = 1
    
    for _ in range(test_cases):
        number = int(input())
        
        b = int(math.log(number,2)) + 1
        
        if(b%2 == 0):
            print(number - (number//2**math.ceil(b//2.0)))
        else:
            print(number - int(2**(b//2)) + 1)
	    ## END
    ## END
## END

