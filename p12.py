#!/usr/bin/python

import math
'''
	This solves problem 12 of project euler. 
	Brute force. 
'''

def nth_triangle_number(n):
	return (n * (n + 1)) /2
	

def number_of_divisors(num):
	nod = 0
	sqrt = int(math.sqrt(num));

	for i in range(1,sqrt + 1):
		if(num % i == 0):
			nod += 2

	if(sqrt * sqrt == num):
		nod -= 1

	return nod;


global keep_running
keep_running = True;

global n 
n = 1
while (keep_running):
	
	number = nth_triangle_number(n)
	if(number_of_divisors(number) >= 500):
		print number
		keep_running = False
		break
	
	n = n + 1


