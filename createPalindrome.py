def createPalindrome():
    N = int(input("Jumlah karakter input: "))

    result = ""
    for i in range(N):
        character = str(input("Input karakter ke-" + str(i+1) + ": "))
        result += character

    currLength = len(result)
    for i in range(N-1):
        result += result[currLength-(i+2)]

    return(result)


print(createPalindrome())
