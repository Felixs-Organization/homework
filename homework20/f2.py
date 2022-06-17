def is_prime(n):
    if n == 1:
        return "%d is not a prime number." % n
    for i in range(2, n):
        if n % i == 0:
            return "%d is not a prime number." % n
    return "%d is a prime number." % n

num = int(input("number please: "))
print(is_prime(num))


print('yu suck @ mc l')