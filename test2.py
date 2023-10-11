#
for num in range(2, 996+2):
    # check if num is prime
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num)