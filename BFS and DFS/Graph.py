import csv
import collections

class Graph:
    "Toma un arcivo CSV y lo transforma a un diccionarioo para tratrarlo como grafo"

    def __init__(self, nodes, edges):

        self.NameDictionary = collections.defaultdict(list)
        self.GraphDictionary = collections.defaultdict(list)

        # Creamos un diccionario para poder traducir los IDs de los nodos a sus respectivos nombres (ID, Name)
        with open(nodes) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    self.NameDictionary[row[0]] = row[1]
                    line_count += 1

        # Obtenemos la conexiones de los nodos a parot del archivo de aristas(Source, Target)
        with open(edges) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    self.GraphDictionary[self.NameDictionary[row[0]]].append(self.NameDictionary[row[1]])
                    line_count += 1
        return


    def DFS(self, node, visited=[]):
        if node not in visited:
            visited.append(node)
            for n in self.GraphDictionary[node]:
                self.DFS(n,visited)
        return visited


    def BFS(self, start):
        explored = []
        queue = [start]
        visited = [start]
        while queue:
            node = queue.pop(0)
            explored.append(node)
            neighbours = self.GraphDictionary[node]
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)
        return explored
