def check():
    x = int(input("Enter a number to check for prime"))
    count = 0
    for val in range(1, x + 1):
        if x % val == 0:
            count = count + 1

    if count == 2:
        print(str(x) + " is a prime number")
    else:
        print("Number is consonant")


check()
