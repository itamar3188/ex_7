# This is a sample Python script.

import math

def mission1a():
    num = int(input("Enter a number: "))
    flag = False
    int n:

    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

        # check if flag is True
        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")

    def mission1b():
        flag = 0
        int s:
        if (n > 1):
            for k in range(2, int(sqrt(s)) + 1):
                if (n % k == 0):
                    flag = 1
                break
            if (flag == 0):
                print(n, " is a Prime Number!")
            else:
                print(n, " is Not a Prime Number!")
        else:
            print(n, " is Not a Prime Number!")


def mission2():
    int
    a,b:
    for i in range(1, min(a, b) + 1):
        if a % i == b % i == 0:
            if i<100:
                print(i)



    def main():
        hello()

    if __name__ == '__main__':
        main()
