from search import *

random.seed("aima-python")

ex8_graph = Graph({'1': {'2': 1, '3': 1}})
ex8_graph.connect('2', '4', 1)
ex8_graph.connect('2', '5', 1)
ex8_graph.connect('3', '6', 1)
ex8_graph.connect('3', '7', 1)
ex8_graph.connect('4', '8', 1)
ex8_graph.connect('4', '9', 1)
ex8_graph.connect('5', '10', 1)
ex8_graph.connect('5', '11', 1)
ex8_graph.connect('6', '12', 1)
ex8_graph.connect('6', '13', 1)
ex8_graph.connect('7', '14', 1)
ex8_graph.connect('7', '15', 1)

ex8_problem = GraphProblem('1', '11', ex8_graph)

#print(ex8_graph.nodes())

#BFS
print('solution')
print(breadth_first_graph_search(ex8_problem).solution())
print('depth')
print(breadth_first_graph_search(ex8_problem).depth)
print('path')
print(breadth_first_graph_search(ex8_problem).path())

#DFS
print('\nsolution')
print(depth_limited_search(ex8_problem, 3).solution())
print('depth')
print(depth_limited_search(ex8_problem, 3).depth)
print('path')
print(depth_limited_search(ex8_problem, 3).path())

#IDS
print('\nsolution')
print(iterative_deepening_search(ex8_problem).solution())
print('depth')
print(iterative_deepening_search(ex8_problem).depth)
print('path')
print(iterative_deepening_search(ex8_problem).path())

'''
solution
['2', '5', '11']
depth
3
path
[<Node 1>, <Node 2>, <Node 5>, <Node 11>]
'''