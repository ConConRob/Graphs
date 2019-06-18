



import sys
sys.path.append(sys.path[0]+"\\..\\graph")


from graph import Graph

# DATA FORMAT
#[(parent1,child1),#[(parent1,child2)]


def find_latest_ancestor(start, family_tree):
  graph = Graph()
  # build the graph
  for parent_child in family_tree:
    parent = parent_child[0]
    child = parent_child[1]
    # if parent or child not made yet make the node
    # graph class already handles this
    graph.add_vertex(parent)
    graph.add_vertex(child)
    # add the link between the parent and child
    graph.add_edge(parent, child)
  # get the last item in a bwt
  
  print(graph.bft(start))


if __name__ == '__main__':
  # family is the graph from the read me
  family = [(10,1),(1,3),(2,3),(4,5),(4,8),(11,8),(3,6),(5,6),(5,7),(8,9)]
  find_latest_ancestor(5, family)
  