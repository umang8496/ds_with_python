# 5 5
# aabaa	

# 1 1  --> 1
# 1 4  --> 8
# 1 1  --> 1
# 1 4  --> 8
# 0 2  --> 5

def countSubstrings(string, queries):
	for query in queries:
		q1 = query[0]
		q2 = query[1]	
		getSubstrigs(string, q0, q1)
	## END
## END


if __name__ == '__main__':
	nq = input().split()
	n = int(nq[0])
	q = int(nq[1])
	string = input()
	queries = []

	for _ in range(q):
		queries.append(list(map(int, input().rstrip().split())))
    ## END

	result = countSubstrings(string, queries)
	print('\n'.join(map(str, result)))
## END
