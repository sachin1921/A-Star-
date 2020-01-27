# for parsing XML
import xml.etree.ElementTree as ET
# importing our Graph class
from way import Way
from node import Node
from graph import Graph
from random import randint
from elevation_data import elevations

def create_graph(filename, g):
    tree = ET.parse(filename)
    root = tree.getroot()
    for item in root:
        if item.tag == 'node':
            node = Node(item.get('id'), float(item.get("lat")), float(item.get("lon")), elevations[item.get('id')])
            g.add_node(node)
         
    for item in root:
        if item.tag == 'way':
            id = item.get("id")
            nodes = []
            name = ""
            for subitem in item:
                if subitem.tag == "nd":
                    nodes.append(g.get_node(subitem.get("ref")))
                if subitem.tag == 'tag' and subitem.get('k') == 'name':
                    name = subitem.get('v')
                    break
            way = Way(id, name, nodes)
            g.add_way(way)

def getTrace(trace, curr):
    path = []
    path.append(curr)
    while curr in trace.keys():
        curr = trace[curr]
        path.append(curr)
    return path

def astar(graph, start, end):
    visited = set()
    discovered = set()
    discovered.add(start)
    trace = {}
    g = {}
    for node in graph.nodes():
        g[node] = float("inf")
    g[start] = 0

    f = {}
    for node in graph.nodes():
        f[node] = float("inf")

    f[start] = Graph.calculate_distance(start, end)
    while len(discovered) != 0:
        lowest = None
        for node in discovered:
            if lowest is None:
                lowest = node
            else:
                if f[node] < f[lowest]:
                    lowest = node
        curr = lowest
        if curr == end:
            return getTrace(trace, curr)

        discovered.remove(curr)
        visited.add(curr)
        for way in graph.adjacencyList[curr]:
            for adjacentNode in way.connected_nodes:
                if adjacentNode not in visited:
                    tmp_g = g[curr] + Graph.calculate_distance(curr, adjacentNode)
                    if adjacentNode not in discovered:
                        discovered.add(adjacentNode)
                    elif tmp_g >= g[adjacentNode]:
                        continue
                    trace[adjacentNode] = curr
                    g[adjacentNode] = tmp_g
                    f[adjacentNode] = g[adjacentNode] + Graph.calculate_distance(adjacentNode, end)

def main():
    g = Graph()
    create_graph("map.osm", g)
    trace = astar(g, g.nodes()[50], g.nodes()[230])
    coordinates = []
    for node in trace:
        coordinates.append((node.lat, node.lon))
    print(coordinates)
    print(trace)

if __name__ == '__main__':
    main()


