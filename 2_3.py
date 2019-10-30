x = int(input("Enter x: "))
y = int(input("Enter y: "))
xBinStr = bin(x)[2:]
yBinStr = bin(y)[2:]
type(yBinStr)
print(xBinStr)
print(yBinStr)
xBinStr32 = xBinStr.zfill(32)
yBinStr32 = yBinStr.zfill(32)
print(xBinStr32)
print(yBinStr32)
i = 0
hamDist = 0
for i in range(32):
    if xBinStr32[i] != yBinStr32[i]:
        hamDist = hamDist + 1
print(hamDist)
