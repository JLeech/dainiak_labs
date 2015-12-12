import numpy as np

def count_legan_elem(i,j,base):
	# проверки по символу лежандра
	if (i-j) % base == 0 : return 0
	for x in range(base):
		# для квадратичных/неквадратичных вычетов
		if (i-j) % base == x**2 % base:
			return 1
	return -1

def make_legand(base):
	legan = np.zeros((base,base))
	# заполняем матрицу лежандра
	for i in range(base):
		for j in range(base):
			if i != j :
				legan[i,j] = count_legan_elem(i,j,base)
			else:	
				legan[i,j] = -1
	return legan.astype(int)

base = 7
legan = make_legand(base)
# бесплатное увеличение длины кода
codes = np.ones((base+1, base+1))
codes[1:,1:] = legan
codes[codes == -1] = 0


with open('input.txt', 'w') as fout:
	for t in codes.T:
		fout.write(''.join(map(str, t[1:].astype(int)))+'\n')