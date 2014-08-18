
global data

def import_data():
	#This is a local variable. 
	data = []
	with open("p11.txt") as f:
		for line in f:
			line = line.split()
			if line:
				line = [int(i) for i in line]
				data.append(line)

	return data
	


data = import_data()

