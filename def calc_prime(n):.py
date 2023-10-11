def calc_prime(limit):
    #array 0 .... 1 init and all var as true prime will be false
    prime = [True for i in range(limit+1)]
    p = 2
    while p**2 <= limit:
        if prime[p]:
            for i in range(p**2, limit+1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, limit+1) if prime[p]]

limit = int(input("input the range: "))
prime = calc_prime(limit)
print("Prime numbers up to", limit, "\n", "ARE:\n", prime)

