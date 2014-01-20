# -*- coding: utf-8 -*-

def fibo(n):
    if n == 1 or n == 2:
        return 1

    return fibo(n-1) + fibo(n-2)

def main():
    for i in range(1,10):
        print fibo(i)

if __name__ = '__main__':
    main()