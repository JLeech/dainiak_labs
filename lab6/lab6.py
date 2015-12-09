import string

class Node:

  sub_nodes = []
  weight = 0.0

# этот метод генерирует pulp_script.py, который решает задачу минимизации
def to_pulp_script(nodes):
  # метод для печати результатов
  script = "from pulp import * \n"
  script += "import string \n"
  script += "def print_result(result) : \n"
  script += "  coverage = \"\"\n"
  script += "  for v in result.variables():\n" 
  script += "    if round(v.varValue) == 1.0 : \n"
  script += "      coverage += str(string.ascii_lowercase[::-1].index(v.name)) + \", \"\n"
  script += "  out_file = open(\"output.txt\",\"w\")\n"
  script += "  out_file.write(coverage)\n\n"

  script += "task = LpProblem(\"prob1\", LpMinimize)\n"
  variables = string.ascii_lowercase[::-1]
  # задание переменных в уравнении минимизации
  for index, node in enumerate(nodes) :
    script += str(variables[index]) + " = LpVariable(\"" + str(variables[index]) + "\",0,1)\n"
  
  script += "\ntask += "
  # задание многочлена для минимизации
  for index, node in enumerate(nodes) :
    script += str(node.weight) + "*" + str(variables[index]) + " + "

  script = script[:-2]
  # задание огарничений на минимизацию
  for index, node in enumerate(nodes) :    
    for sub_node in node.sub_nodes :
      script += "\ntask += "
      script += str(variables[index]) + "+" + str(variables[sub_node]) + " >= 1"
  # решение и вывод результата
  script += "\nGLPK().solve(task)\n"
  script += "print_result(task)"


  out_file = open("pulp_script.py","w")
  out_file.write(script)


def read_data(file_name):
  f = open(file_name,'r') 
  nodes_count = 0
  positions = []
  # определение количества нод
  for line in f : 
    positions.append( len( [ int(position) for position in line.strip().split(" ")] ) )
  nodes_count = positions.count(1)

  sub_nodes = []
  nodes = []
  node_position = 0
  for time in  range(nodes_count):
    sub_nodes.append([])
  
  # заполнение массива из нод данными
  f = open(file_name,'r') 
  for line in f :
    positions = [ int(position) for position in line.strip().split(" ")]
    if len(positions) > 1 :
      sub_nodes[positions[0]].append(positions[1])
    else:
      node = Node()
      node.weight = positions[0]
      node.sub_nodes = sub_nodes[node_position]
      nodes.append(node)
      node_position += 1


  return nodes

to_pulp_script( read_data("input.txt") )