# Alexa has two stacks of non-negative integers, stackA  and stackB  where index 0 denotes the top of the stack.
# Alexa challenges Nick to play the following game:

# In each move, Nick can remove one integer from the top of either stack  or stack .
# Nick keeps a running sum of the integers he removes from the two stacks.
# Nick is disqualified from the game if, at any point, his running sum becomes greater than
# some integer N given at the beginning of the game.
# Nick's final score is the total number of integers he has removed from the two stacks.
# Find the maximum possible score Nick can achieve (maximum number of integers he can remove without being disqualified)
# during each game and print it on a new line.

# 1
# 5 4 10
# 4 2 4 6 1
# 2 1 8 5

#!/bin/python3

import os
import sys

def twoStacks(element_sum, stackA, stackB):
    element_sum_counter,score = 0,0
    if(element_sum == 0):
        return 0
    else:
        top_in_A,top_in_B = 0,0
        len_A,len_B = len(stackA),len(stackB)

        while(True):
            if(top_in_A == len_A or top_in_B == len_B):
            	return score
        	## END
            if(stackA[top_in_A] > stackB[top_in_B]):
                element_sum_counter += stackB[top_in_B]
                if(element_sum_counter > element_sum):
                    break
                else:
                    top_in_B += 1
                    score += 1
                ## END
            elif(stackA[top_in_A] < stackB[top_in_B]):
                element_sum_counter += stackA[top_in_A]
                if(element_sum_counter > element_sum):
                    break
                else:
                    top_in_A += 1
                    score += 1
                ## END
            else:
                if((len_B - top_in_B) > (len_A - top_in_A)):
                    element_sum_counter += stackB[top_in_B]
                    if(element_sum_counter > element_sum):
                        break
                    else:
                        top_in_B += 1
                        score += 1
                    ## END
                else:
                    element_sum_counter += stackA[top_in_A]
                    if(element_sum_counter > element_sum):
                        break
                    else:
                        top_in_A += 1
                        score += 1
                    ## END
                ## END
            ## END
        ## END
        return score
    ## END
## END


if __name__ == '__main__':
    # g = int(input())
    g = 1

    for g_itr in range(g):
        x = int(input('Enter threshold : '))

        a = list(map(int, str("1 1 0 1 1 1 0 1 0 1 0 0 1 1 1 1 1 0 1 0 1 1 1 0 1 1 1 0 0 0 1 0 1 1 1 0 1 0 1 1 1 0 0 0 1 1 1 1 1 0").rstrip().split()))
        b = list(map(int, str("1 1 0 1 1 0 0 1 1 0 0 1 1 0 1 1 1 0 1 1 1 0 0 0 0 0 1 0 1 1 0 0 0 0 1 1 1").rstrip().split()))

        result = twoStacks(x, a, b)
        print(str(result) + '\n')
## END



# static int twoStacks(int x, int[] a, int[] b) {
#    int maxStep = 0;
#    int sum = 0;
#    int i = 0; 
#    int j = 0;
#    while (i < a.length && sum + a[i] <= x) {
#        sum += a[i++];
#    }

#    maxStep = Math.max(maxStep, i);
#    while (j < b.length) {
#        sum += b[j++];
#         while (sum > x && i > 0) {
#             sum -= a[--i];
#         }
        
#         if (sum <= x)
#             maxStep = Math.max(maxStep, i + j);
#    } 

#    return maxStep;
# }
