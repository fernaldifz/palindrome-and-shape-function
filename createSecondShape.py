def createSecondShape():
    for i in range(5):
        for j in range(5):
            if(i >= j):
                print(j+1, end="")
            else:
                print(" ", end="")
        for j in range(4):
            if(5-i-j <= 2):
                print(5-j-1, end="")
            else:
                print(" ", end="")
        print("\n", end="")

    for i in range(4):
        for j in range(5):
            if(5-i-j >= 2):
                print(j+1, end="")
            else:
                print(" ", end="")
        for j in range(4):
            if(i <= j):
                print(5-j-1, end="")
            else:
                print(" ", end="")
        print("\n", end="")


createSecondShape()
