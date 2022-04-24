def reverse(num):
    num = int(input("Enter a number"))
    st = str(num)
    revst = st[::-1]  # start:stop-1
    ans = int(revst)
    return ans


print(reverse(123))
