
def saveThePrisoner(prisoners, candies, seat):
    # return ((seat - 1) + (candies % prisoners))
    return (((seat+candies-2) % prisoners) + 1)
## END

if __name__ == '__main__':
    nms = input().split()
    n = int(nms[0])
    m = int(nms[1])
    s = int(nms[2])
    result = saveThePrisoner(n, m, s)
    print(result)
## END
