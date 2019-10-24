initList = []
i = 1
inputStep = input("Enter steps: ")
stepCount = int(inputStep)
while i <= stepCount:
    i = i + 1
    N = input("Enter command and arguments: ").split()
    if N[0] == 'insert':
        initList.insert(int(N[1]), int(N[2]))
    elif N[0] == 'print':
        print(initList)
    elif N[0] == 'remove':
        initList.remove(int(N[1]))
    elif N[0] == 'append':
        initList.append(int(N[1]))
    elif N[0] == 'sort':
        initList.sort()
    elif N[0] == 'pop':
        initList.pop()
    elif N[0] == 'reverse':
        initList.reverse()
