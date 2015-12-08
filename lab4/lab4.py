import cmath

def read_data(file_name):
  f = open(file_name,'r')
  coefficients = [ complex(variable) for variable in f.readlines()[0].strip().split(" ") ]
  return coefficients

def save_to_file(file_name, data):
  out_file = open(file_name,"w")
  [ out_file.write(str(number.real)+","+str(number.imag)+" ") for number in data ]
  out_file.write("\n")

def count_fft(coefficients):
  # считаем корень из единицы
  coef_length = int(len(coefficients))
  angle = 2 * cmath.pi / coef_length
  root_of_unity = cmath.cos(angle) + cmath.sin(angle) * 1j

  if coef_length == 1:
    return coefficients

  # применяем рекурсивно для чётных и нечётных (поэтому и log)
  y0 = count_fft(coefficients[::2])
  y1 = count_fft(coefficients[1::2])
  y = [0+0j] * coef_length

  w_coef = 1 + 0j

  for k in range( int( coef_length / 2) ):
      # по формулам "преобразования бабочки"
      y[k] = y0[k] + w_coef * y1[k]
      y[k + int(coef_length / 2)] = y0[k] - w_coef * y1[k]
      w_coef = w_coef * root_of_unity
      
  return y

save_to_file("output.txt", count_fft(read_data("input.txt")) )
