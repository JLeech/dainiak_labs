import random
import string
import numpy as np
import sympy as sp

from sympy import *
from sympy.matrices import Matrix

def make_computations(matrix,values):
	#letters = list(string.ascii_lowercase)
	#combined_letters = letters
	#symbols = []
	#[ [ symbols.append(sub_lettter+letter) for sub_lettter in combined_letters ]  for letter in letters ]
	#symbols = ",".join(symbols[:len(values)])
	#symbol_variables = np.array([ sp.symbols( symbols )])
	#symbol_matrix = sp.Matrix( symbol_variables * matrix)
	#symbol_det = symbol_matrix.det()
	#print ( sp.Matrix(values*matrix).det() )
	#print (symbol_det)
	return (sp.Matrix(values*matrix).det())

def count_probability():
	matrix = read_data("input.txt")
	values = generate_values(len(matrix))
	probability = 1
	for iterator in range(0,100) :
		result = make_computations(matrix,values)
		if result == 0.0:
			probability *= (1/len(matrix))
	if probability != 1 :
		print (0)
	else :
		print (1)
	print ( probability )

def generate_values(size):
	return [ random.randrange(1,size) for value in range(size) ]

def read_data(file_name):
	f = open(file_name,'r')
	all_nodes = []
	for line in f :	
		all_nodes += [ int(node) for node in line.strip().split(" ") ]	
	
	matrix_size = max(all_nodes)

	matrix = np.zeros([matrix_size,matrix_size])

	f = open(file_name,'r')
	all_nodes = []
	for line in f :		
		values = [ int(node) -1 for node in line.strip().split(" ") ]
		matrix[values[0]][values[1]] = 1
		matrix[values[1]][values[0]] = 1

	return matrix

count_probability()

