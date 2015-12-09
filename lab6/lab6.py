import string

class Node:

  sub_nodes = []
  weight = 0.0


def to_pulp_script(nodes):
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
  for index, node in enumerate(nodes) :
    script += str(variables[index]) + " = LpVariable(\"" + str(variables[index]) + "\",0,1)\n"
  
  script += "\ntask += "
  for index, node in enumerate(nodes) :
    script += str(node.weight) + "*" + str(variables[index]) + " + "

  script = script[:-2]

  for index, node in enumerate(nodes) :    
    for sub_node in node.sub_nodes :
      script += "\ntask += "
      script += str(variables[index]) + "+" + str(variables[sub_node]) + " >= 1"

  script += "\nGLPK().solve(task)\n"
  script += "print_result(task)"


  out_file = open("pulp_script.py","w")
  out_file.write(script)


def read_data(file_name):
  f = open(file_name,'r') 
  nodes_count = 0
  positions = []
  for line in f : 
    positions.append( len( [ int(position) for position in line.strip().split(" ")] ) )
  nodes_count = positions.count(1)
  

  sub_nodes = []
  nodes = []
  node_position = 0
  for time in  range(nodes_count):
    sub_nodes.append([])
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

# from pulp import * 

# prob = LpProblem("test1", LpMinimize) 

# # Variables 
# x = LpVariable("x", 0, 10) 
# y = LpVariable("y", 0, 10) 

# # Objective 
# prob += x + 4*y

# # Constraints 
# prob += x+y >= 5 

# GLPK().solve(prob) 

# # Solution 
# for v in prob.variables(): 
#   print (v.name, "=", v.varValue )

# print ("objective=", value(prob.objective)  )