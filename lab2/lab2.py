import random

# записать данные в файл
def write_to_file(data):
	writing_file = open('input.txt',"a")
	[ writing_file.write(str(current_data)+" ") for current_data in data ]
	writing_file.write("\n")


def get_2_random_numbers(size):
	return [ random.getrandbits(size) for elem in [1,1] ] 

def to_bit_string(number):
	return "{0:b}".format(number)

# получить список сдвинутых чисел
def get_shifted_numbers(fir_number,sec_number):
	shift_positions = 0
	shifted_numbers = []
	for current_bit in reversed(to_bit_string(sec_number)) :
		current_number = ( fir_number * int(current_bit) ) << shift_positions
		shifted_numbers.append(to_bit_string(current_number))
		shift_positions += 1
	return shifted_numbers

def use_trick_for_numbers(numbers):
	xor_string = ""
	overflow_string = "0"
	max_length = max( [ len(current_num) for current_num in numbers ])
	# подравнять количество бит в числах чтобы не заиорачиваться с разной длинной
	aligned_numbers = [ current_num.zfill(max_length) for current_num in numbers ]
	for current_digit_index in reversed(range(0,max_length)):
		current_digit = 0
		for current_number_index in range(0,3):
			current_digit += int(aligned_numbers[current_number_index][current_digit_index])
		# проксорить биты
		xor_string = str(current_digit%2) + xor_string
		# посмотреть на переполнение
		if current_digit > 1 :
			overflow_digit = 1 
		else:
			overflow_digit = 0
		overflow_string = str(overflow_digit) + overflow_string
	return [overflow_string,xor_string]


# обработать строку с числами
def process_numbers(numbers):
	triples_count = int(len(numbers)/3)
	counted_numbers = []
	for iter in range(0,triples_count):
		# взять тройку с начала и провести над ней 3-2 трюк
		counted_numbers += use_trick_for_numbers(numbers[:3])
		numbers = numbers[3:]
	counted_numbers += numbers
	write_to_file(counted_numbers)
	if len(counted_numbers) > 3:
		# рекурсивно вызвать если числел > 3
		process_numbers(counted_numbers)
	else:
		# в противном случае всё сложить
		write_to_file( [to_bit_string( sum ([ int(number,2) for number in counted_numbers ]) ) ] )
		return str( sum ([ int(number,2) for number in counted_numbers ]) )


#fir_number, sec_number = get_2_random_numbers(16)

fir_number = 17
sec_number = 31

write_to_file( [ to_bit_string(current_number) for current_number in [fir_number,sec_number] ])
shifted_numbers =  get_shifted_numbers(fir_number,sec_number)
write_to_file( [ current_number for current_number in shifted_numbers ] )
result = process_numbers(shifted_numbers)

