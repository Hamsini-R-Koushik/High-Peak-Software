def sort_tuple_list(tup):
    if tup:
    	tup.sort(key = lambda x: x[1])  
    return tup

def get_data(data):
	result = []
	for item in data:
		d = item.split(':')
		result.append((d[0].strip(),int(d[1].strip())))
	return result

def write_output(sorted_data, min_diff, cs, ce, num_of_emp):
	with open('sample_output.txt','w') as f:
		f.write(f'Number of the employees: {num_of_emp}\n')
		f.write('Here are the goodies that are zselected for dostribution are:\n')
		for item in sorted_data[cs:(ce+1)]:
			f.write(f'{item[0]}: {item[1]}\n')
		f.write(f'And the differece between the chosen goodie with highest price and the lowest price is {min_diff}')

def min_diff():
	num_of_emp = int(input("Number of the employees: "))
	lines = []
	with open('sample_input.txt','r') as f:
		lines = f.read().splitlines()
	sorted_data = sort_tuple_list(get_data(lines))
	s = 0
	e = num_of_emp-1
	min_diff = -1
	cs = s
	ce = e
	if sorted_data:
		while True:
			if e == len(sorted_data):
				break
			else:
				diff = sorted_data[e][1]-sorted_data[s][1]
				if min_diff != -1:
					if diff < min_diff:
						min_diff = diff
						cs = s
						ce = e
				else:
					min_diff = diff
				s += 1
				e += 1
		write_output(sorted_data, min_diff, cs, ce, num_of_emp)
	else:
		print("Input provided is empty")

if __name__ == '__main__':
	min_diff()

