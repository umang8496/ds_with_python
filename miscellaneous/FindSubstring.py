# In this challenge, the user enters a string and a substring.
# You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.

def count_substring(string, sub_string):
    number_of_substrings = 0
    length_of_sub_string = len(sub_string)
    pos = 0

    # another approach should come here.
    while (pos != -1):
        pass
        # pos = string.find(sub_string)
    ##END

    while (pos + length_of_sub_string <= len(string)):
        pos = string.find(sub_string)
        if (pos == -1):
            break
        else:
            number_of_substrings += 1
            string = string[pos + 1:]
            pos = 0

    return number_of_substrings

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
## END
