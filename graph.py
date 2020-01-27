import geopy.distance
from way import Way 
from node import Node
from math import sqrt

class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def __repr__(self):
        return f"Graph()"

    def __str__(self):
        return str(self.adjacencyList)

    def nodes(self):
        return list(self.adjacencyList.keys())

    def get_node(self, id):
        for node in self.nodes():
            if node.id == id:
                return node

    def ways(self):
        return list(self.adjacencyList.values())

    def add_node(self, node):
        if node not in self.adjacencyList:
            self.adjacencyList[node] = []
    
    def add_way(self, way):
        for node in way.connected_nodes:
            if way not in self.adjacencyList[node]:
                self.adjacencyList[node].append(way)
    
    @staticmethod
    def calculate_distance(start_node, end_node):
        coords_1 = (start_node.lat, start_node.lon)
        coords_2 = (end_node.lat, end_node.lon)
        height_diff = abs(start_node.elevation - end_node.elevation)
        straight_distance = geopy.distance.vincenty(coords_1, coords_2).km
        return sqrt((height_diff)**2+(straight_distance)**2)

if __name__ == "__main__":
    g = Graph()
    node1 = Node("82815113", 43.9007573, -78.8542211, 6000)
    node2 = Node("6195225242", 43.9036566, -78.8847820, 4000)
    way = Way("10885233", "William Street East", [node1, node2])
    g.add_node(node1)
    g.add_node(node2)
    g.add_way(way)
    print(g)
