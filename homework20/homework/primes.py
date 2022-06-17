def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True




def get_l_of_primes(stop):
    l = []
    for i in range(stop):
        if is_prime(i):
            l.append(i)
    return l

f = open('./primes.txt', 'w')
for i in get_l_of_primes(100):
    f.write(str(i) + '\n')
f.close()