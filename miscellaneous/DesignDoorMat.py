# Mr. Vincent works in a door mat manufacturing company.
# One day, he designed a new door mat with the following specifications:

# Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

#    Size: 7 x 21 
#    ---------.|.---------
#    ------.|..|..|.------
#    ---.|..|..|..|..|.---
#    -------WELCOME-------
#    ---.|..|..|..|..|.---
#    ------.|..|..|.------
#    ---------.|.---------
    
#    Size: 11 x 33
#    ---------------.|.---------------
#    ------------.|..|..|.------------
#   ---------.|..|..|..|..|.---------
#    ------.|..|..|..|..|..|..|.------
#    ---.|..|..|..|..|..|..|..|..|.---
#    -------------WELCOME-------------
#    ---.|..|..|..|..|..|..|..|..|.---
#    ------.|..|..|..|..|..|..|.------
#    ---------.|..|..|..|..|.---------
#    ------------.|..|..|.------------
#    ---------------.|.---------------


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    nm = input().split(' ')
    N,M = int(nm[0]),int(nm[1])
    i = 0

    for n in range(0,N):
        if(n > N//2):
            i -= 2
        else:
            i = 2*n+1
        ##END

        if(n==(N//2)):
            m = (M-7)//2
            print('-'*m + 'WELCOME' +'-'*m)
        else:
            m = (M-3*i)//2
            print('-'*m + '.|.'*i +'-'*m)            
        ##END
    ##END
