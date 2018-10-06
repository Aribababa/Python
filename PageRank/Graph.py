
class Graph:

    def __init__(self, nodes, edges):
        """
            Crea un grafo direccionado a partir de dos entradas tipoo .CSV. Este al final se queda con
            diccionario el cual representa al grafo.

            Args:
                nodes: Archivo .CSV con los nodos del grafo.
                edges: Archivo .CSV con las aristas del grafo y su metrica.

            Returns:
                None

            Raises:
                KeyError: Raises an exception.
            """
        import csv
        import collections

        NameDictionary = collections.defaultdict(list)
        self.GraphDictionary = collections.defaultdict(list)

        # Creamos un diccionario para poder traducir los IDs de los nodos a sus respectivos nombres (ID, Name)
        with open(nodes) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    NameDictionary[row[0]] = row[1]
                    line_count += 1

        # Obtenemos la conexiones de los nodos a parot del archivo de aristas(Source, Target)
        with open(edges) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    self.GraphDictionary[NameDictionary[row[0]]].append(NameDictionary[row[1]])
                    line_count += 1

        # Verificamos que todos lo nodos esten presenten en el grafo.  Como los pueden ser
        # los que no apuntan a nadie, pero todos apuntan hacia ellos.

        for _, val in NameDictionary.items():
            if  not(val in self.GraphDictionary):
                self.GraphDictionary[val] = []

        return

    def GetAdjacencyMatrix(self):
        """
            Toma el diccionario que representa al grafo y lo pasa a una matriz de adyacencia
            para poder trabajarla con otros metodos

            Args:
                None

            Return:
                La matriz de adyacencia correspondiente.
        """

        keys = self.GraphDictionary.keys()
        size = len(keys)

        adjacencyMatrix = [[0] * size for i in range(size)]

        for a, b in [(keys.index(a), keys.index(b)) for a, row in self.GraphDictionary.items() for b in row]:
            adjacencyMatrix[a][b] = 2 if (a == b) else 1
        return adjacencyMatrix

    def PageRank(self, M, d=0.85, iterations=1):
        """

        :param M: Matriz de adyacencia donde las columnas son los padres y las filas los hijos
        :param d: Factor de amortiguamiento del algoritmo(Por default 0.85)
        :param iterations: Numero de iteraciones que realizara el algoritmo.

        :return: Vector con el valor de cada PageRank

        """
        import numpy as np

        d = 1 - d   # complementamos el valor ya que en el algorimto son complementados
        PageRank = np.full((1, len(M)), 0.25, dtype=float)  # valor inicial del Pagerank
        I = np.full((len(M), len(M)), 1.0/len(M), dtype=float)  # Matriz estocastica

        # Obtenemos la matriz de transportacion, donde se dividen los elementos con el
        # numero de conexiones que hay hacia los nodos.
        for k in range (0, len(M)):
            counter = 1
            for i in range (0, len(M)):
                if M[i][k] :
                    counter+=1
            for j in range (0, len(M)):
                M[j][k] = float(M[j][k])/counter


        # Comenzamos a realizar la parte iterativa del algoritmo
        # Calculmos la parte constante, la cual es la matriz con los factores de amortiguiamiento

        M = np.matrix(M, dtype=float)
        matrix = np.add(d*I, (1.0-d)*M)
        matrix = np.transpose(matrix)

        # Calculamos el algoritmo cierto numero de veces para que los valores converjan
        while iterations:
            # Utilizando el metodo de Power Iteration
            b_k1 = np.dot(PageRank, matrix)
            b_k1_norm = np.linalg.norm(b_k1)
            PageRank = b_k1 / b_k1_norm

            iterations-=1

        return PageRank