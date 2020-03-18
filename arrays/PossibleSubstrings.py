def AllPossibleSubstrings(stg):
     N = len(stg)
     substring = []
     
     #for grp in range(1,1+1):
     for i in range(1,N+1):
          for j in range(i):
               #print(stg[j:i])
               substring.append(stg[j:i])
     return substring
##END

########################################################

if __name__ == "__main__":
     stg = input('Enter a string : ')
     substring = AllPossibleSubstrings(stg)

     print(substring)
     print("number of all substrings :",len(substring))
     print("number of all set(substrings) :",len(set(substring)))
##END
