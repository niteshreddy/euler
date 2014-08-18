
'''
	This is a solution to problem 9 of project euler. 

	There exists a pythagorean triplet for which 

	a + b + c = 1000

	find the product abc. 
'''

#Brute forco approach

def brute_force ():
	 a = b = c = 0
	 s = 1000
	 found = False;

	 for a in range(1,s/3):
	 	for b in range(a,s/2):
	 		c = s - a - b

	 		if(a * a + b * b == c * c):
	 			found = True;
	 			print a * b * c
	 			break;


	 	if(found == True):
	 		break;
brute_force()




