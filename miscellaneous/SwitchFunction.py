def switch_func(value, x):
    return {
        'a': lambda x: x+122,
        'b': lambda x: x*2,
        'c': lambda x: x-123,
        'd': lambda x: x/2
    }.get(value)(x)

# take user input
inp = input('input a character out of a, b, c and d: ')

print('The result for inp is : ', switch_func(inp, 2))
