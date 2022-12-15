import sys
import os
import math as m


class Coeiff:
    def __init__(self,a4,a3,a2,a1,a0):
        self.a0 = a0
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4

def solve_4degree(a4,a3,a2,a1,a0,method=2,iteration=200):
    CF=Coeiff(a4,a3,a2,a1,a0)
    x1,x2=my_choose(method,CF,iteration)
    return x1,x2

def my_choose(opt, CF, n):
    if opt == 1:
        my_bisection(CF, n)
    elif opt == 2:
        my_newton(CF, n)
    elif opt == 3:
        my_secant(CF, n)
        return -1,-1

def my_secant(CF, n):
    print("Secant:")
    print("a0 = {0:d}".format(CF.a0))
    print("a1 = {0:d}".format(CF.a1))
    print("a2 = {0:d}".format(CF.a2))
    print("a3 = {0:d}".format(CF.a3))
    print("a4 = {0:d}".format(CF.a4))
    print("n = {0:d}".format(n))

def my_bisection(CF, n):
    p1 = 0.0
    p2 = 1.0
    x1 = float
    x2 = float
    x = float

    for i in range(1, 300):
        x = (p1 + p2) / 2
        if i <= n:
            print("x = {0:.{1:d}f}".format(x, i))
        else:
            print("x = {0:.{1:d}f}".format(x, n))
        x1 = (CF.a4 * pow(x, 4)) + (CF.a3 * pow(x, 3)) + (CF.a2 * pow(x, 2)) + (CF.a1 * x) + CF.a0
        x2 = (CF.a4 * pow(p1, 4)) + (CF.a3 * pow(p1, 3)) + (CF.a2 * pow(p1, 2)) + (CF.a1 * p1) + CF.a0
        if x2 * x1 < 0:
            p2 = x
        else:
            p1 = x
        if round(p1 * pow(10, n)) == round(p2 * pow(10, n)):
            return x1,x2
    return x1, x2

def my_newton(CF, n):
    p1 = 0.0
    p2 = 1.0
    x1 = float
    x2 = float
    x = float

    for i in range(1, 300):
        x = (p1 + p2) / 2
        if i <= n:
            print("x = {0:.{1:d}f}".format(x, i))
        else:
            print("x = {0:.{1:d}f}".format(x, n))
        x1 = (CF.a4 * pow(x, 4)) + (CF.a3 * pow(x, 3)) + (CF.a2 * pow(x, 2)) + (CF.a1 * x) + CF.a0
        x2 = (CF.a4 * pow(p1, 4)) + (CF.a3 * pow(p1, 3)) + (CF.a2 * pow(p1, 2)) + (CF.a1 * p1) + CF.a0
        if x2 * x1 < 0:
            p2 = x
        else:
            p1 = x
        if round(p1 * pow(10, n)) == round(p2 * pow(10, n)):
            return x1,x2

    return x1,x2


# def main():
#     my_check_arg()
#     CF = Coeiff
#     opt = int(sys.argv[1])
#     CF.a0 = int(sys.argv[2])
#     CF.a1 = int(sys.argv[3])
#     CF.a2 = int(sys.argv[4])
#     CF.a3 = int(sys.argv[5])
#     CF.a4 = int(sys.argv[6])
#     n = int(sys.argv[7])
#     my_choose(opt, CF, n)
#     sys.exit(0)
# main()