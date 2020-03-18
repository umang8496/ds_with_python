# Given a string , which is the company name in lowercase letters, 
# your task is to find the top three most common characters in the string.

# Print the three most common characters along with their occurrence count.
# Sort in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.

# INPUT
# 	aabbbccde
# OUTPUT
# 	b 3
# 	a 2
# 	c 2

import collections

if __name__ == '__main__':
    company_name = list(sorted(input()))
    # company_name = 'aabbbccde'
    char_dictionary = collections.OrderedDict()

    ctr = collections.Counter(company_name)
    print(ctr)

    for each in ctr:
    	print(*each)


