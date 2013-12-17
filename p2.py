#!/usr/bin/python

'''
This python file is going to solve problem 2 of project euler. 
It is going to calculate the sum of all even fibonacci numbers
below and including 4 million. 

'''

def sumEvenFibonacci():
    print '''Problem 2 of Project Euler'''

    total = 0

    fib = 1
    n1 = 1 
    n2 = 0
    while fib <= 4000000:
        
        if fib%2 == 0:
            total = total + fib
        fib = n2 + n1 
        n2 = n1
        n1 = fib
    print "%d"%total

sumEvenFibonacci()


