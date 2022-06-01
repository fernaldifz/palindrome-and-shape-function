def createShape(N):
    for i in range(N):
        for j in range(N):
            if(j < i):
                print(" ", end="")
            else:
                print("* ", end="")
        print("\n", end="")
    for i in range(N-1):
        for j in range(N):
            if(N-i-2 > j):
                print(" ", end="")
            else:
                print("* ", end="")
        print("\n", end="")


createShape(4)
