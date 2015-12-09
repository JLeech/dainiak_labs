import numpy as np

class Edge:

  weight = 0.0

  def __init__(self, start,stop):
    self.start = start
    self.stop = stop


def read_data(file_name):
  edges = []
  f = open(file_name,'r') 
  nodes_count = 0
  for line in f : 
    positions = [ int(position) for position in line.strip().split(" ")]
    nodes_count = max(positions + [nodes_count] )
    edges.append( Edge( positions[0], positions[1] ) )

  return [edges,nodes_count+1]

def save_to_file(file_name, data):
  print(data)
  out_file = open(file_name,"w")
  for index, number in enumerate(data) :
    out_file.write(str(index) + " " + str(number) + "\n" )
  out_file.write("\n")

edges,nodes_count = read_data("input.txt")
connections = np.zeros(shape=(nodes_count,nodes_count))

# заполняем матрицу связей
for edge in edges:
  connections[edge.start][edge.stop] = 1.0

# нормируем строки
for row in range(nodes_count):
  connections[row] = connections[row]/sum(connections[row])

# транспонируем для удобства
connections = connections.transpose()

# вектор дефолтных значений весов 
dafault_values = [1.0/nodes_count] * nodes_count 

step = connections.dot(dafault_values)
step_2 = connections.dot(step)

# итеративно сходимся
while (sum(abs(step - step_2)) > 0.001 ):
  
  step = step_2
  step_2 = connections.dot(step)

save_to_file("output.txt",step_2)