

def kmpSearch(text, pattern):
	text_length = len(text)
	pattern_length = len(pattern)
	t = 0	# for text
	p = 1	# for pattern (must always be +ve)
	lsp = computeLspTable(pattern)

	for t in range(0, text_length):
		while (p > 0 and text[t] != pattern[p]):
			p = lsp[p - 1]
		## END
		if (text[t] == pattern[p]):
			p += 1
			if (p == pattern_length):
				return (t - p + 1)
			## END
		## END
	## END
	return t 	# index of first match
## END


# LSP-Table for the pattern "onions" is as follows:
# o  n  i  o  n  s
# 0  0  0  1  2  0
def computeLspTable(pattern):
	pattern_length = len(pattern)
	lsp = [0] * pattern_length
	length = 0
	f = 1
	
	while (f < pattern_length):
		if (pattern[f] == pattern[length]):
			lsp[f] = length + 1
			length += 1
			f += 1
		else:
			if (length != 0):
				length = lsp[length - 1]
			else:
				lsp[f] = 0
				f += 1
			## END
		## END
	## END
	return lsp
## END


if __name__ == '__main__':
	text = "onionionsone";
	pattern = "onions";

	# text = "trailtrain"
	# pattern = "train"

	# text = "abazacabababac"
	# pattern = "ababac"

	print("text: " + text)
	print("pattern: " + pattern)
	index = kmpSearch(text, pattern)
	if (index != -1):
		print("Match Found at: " + str(index))
	else:
		print("Match Not Found!!")
	## END
## END


# Test Case (1):
# text = "onionionsone";
# pattern = "onions";
# index ==> 3

# Test Case (2):
# text = "trailtrain"
# pattern = "train"
# index ==> 5

# Test Case (3):
# text = "abazacabababac"
# pattern = "ababac"
# index ==> 8
