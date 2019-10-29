def ham_dist_func(x, y):
    """Hamming distance function"""
    xBinStr = bin(x)[2:]
    yBinStr = bin(y)[2:]
    xBinStr32 = xBinStr.zfill(32)
    yBinStr32 = yBinStr.zfill(32)
    i = 0
    hamDist = 0
    while i < 32:
        if xBinStr32[i] != yBinStr32[i]:
            hamDist = hamDist + 1
        i = i + 1
    return hamDist


if __name__ == "__main__":
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    ham = ham_dist_func(x, y)
    print(ham)
