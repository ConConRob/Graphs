

import sys
sys.path.append(sys.path[0]+"\\..\\graph")
# DATA FORMAT
# [(parent1,child1),#[(parent1,child2)]

from util import Queue

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if not vertex in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check if keys exist
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("The vertex does not exist")

    def bft(self, starting_vertex):
        q = Queue()
        explored = []

        first_of_highest_floor = -1 # if start does not have a child this won't change
        current_floor = 0
        q.enqueue([starting_vertex, current_floor  ])
        visited = set()

        while q.size() > 0:
            # dequeue the first node
            item = q.dequeue()
            v = item[0]
            floor = item[1]
            if v not in visited:
                # if floor height is the same check which is lower id number
                if floor == current_floor and first_of_highest_floor > v:
                    first_of_highest_floor = v
                # if higher then current floor set the new floor height 
                if floor > current_floor:
                    current_floor = floor
                    first_of_highest_floor = v
                visited.add(v)
                for next_node in self.vertices[v]:
                    q.enqueue([next_node, floor + 1])
        return first_of_highest_floor  # returns the last value looked at

def find_latest_ancestor(start, family_tree):
    graph = Graph()
    # build the graph
    for parent_child in family_tree:
        child = parent_child[0]
        parent = parent_child[1]
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
    family = [(10, 1), (1, 3), (2, 3), (4, 5), (4, 8),
              (11, 8), (3, 6), (5, 6), (5, 7), (8, 9)]
    find_latest_ancestor(3, family)
