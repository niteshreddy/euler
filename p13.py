'''
Solution to problem 13 of project euler. 
'''


global data

def import_data():
	#This is a local variable. 
	data = []
	with open("p13.txt") as f:
		for line in f:
			line = line.split()
			if line:
				line = [long(i) for i in line]
				data.append(line)

	return data
	


data = import_data()




global n
n = 0
for i in data:
	for j in i:
	 n = n + j

print str(n)[0:10]