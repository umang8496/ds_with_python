# You are given a string S and width w. 
# Your task is to wrap the string S into a paragraph of width w.

def wrap(string, max_width):
    ls = []
    for i in range(1,len(string)+1):
        if ((i) % max_width == 0):
            ls.append(string[i-1])
            ls.append('\n')
        else:
            ls.append(string[i-1])
        ##END
    ##END

    return ''.join(ls)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)