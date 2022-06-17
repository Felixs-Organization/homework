import math


def do_calc(n):
    times = 0
    numbers_encountered = []
    for i in range(n):
        if n % (i+1) == 0:
            times += 1
            numbers_encountered.append(i+1)
    return "Times: {0} \nNumbers encountered: {1}".format(str(times), numbers_encountered)
            


def main():
    num = int(input("number please: "))
    print(do_calc(num))


if __name__ == "__main__":
    main()
