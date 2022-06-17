#!/usr/bin/env python3
def is_prime(n):
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def get_l_of_primes(stop):
    l = 2
    i = 0
    while i < stop:
        if is_prime(l):
            i += 1
        l += 1
    return l-1


def main():
    print('welcome to T.P.N.C')
    print('please enter a number')
    number = int(input())
    print('calculating...')
    print(get_l_of_primes(number))


if __name__ == '__main__':
    main()
