# filter function will filter out the result based on function and sequence (Range)

def prime(x):
    for n in range(2, x):
        if x % n == 0:
            return False
        else:
            return True


filtered = filter(prime, range(10))
print(list(filtered))  # Make a list and print
