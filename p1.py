#!/usr/bin/python

def mul3and5():
    print '''Finding the sum all numbers which are 
            multiples of 3 or 5 and are below and including thousand.'''
    sum = 0
    for x in range(1, 1000):
        if x%3 == 0:
            sum = sum + x
        elif x%5 == 0:
            sum = sum + x
        elif x%15 == 0:
            sum = sum - 15

    print "The sum is:%d"%sum


mul3and5()
