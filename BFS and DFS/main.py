from Graph import Graph
import random

import matplotlib.pyplot as plt
plt.style.use('ggplot')

def Calculate_Avg_Path_BFS(Graph, iterations, node):
    BFS_Path_Avg = []
    counter = 0
    while counter < iterations:
        try:
            BFS_Output = Graph.BFS(random.choice(Graph.GraphDictionary.keys()))
            Step_Counter = 0

            while not (BFS_Output[Step_Counter] == node):
                Step_Counter += 1
            BFS_Path_Avg.append(Step_Counter)
            counter += 1
        except:
            None

    # Calculamos el promedio de los pasos
    return sum(BFS_Path_Avg)/iterations


def Calculate_Avg_Path_DFS(Graph, iterations, node):
    DFS_Path_Avg = []
    counter = 0
    while counter < iterations:
        try:
            DFS_Output = Graph.DFS(random.choice(Graph.GraphDictionary.keys()))
            Step_Counter = 0

            while not (DFS_Output[Step_Counter] == node):
                Step_Counter += 1
            DFS_Path_Avg.append(Step_Counter)
            counter += 1
        except:
            None

    # Calculamos el promedio de los pasos
    return sum(DFS_Path_Avg)/ iterations



def main():
    g = Graph("JamieOliver_nodes.csv", "JamieOliver_edges.csv")

    Avg_Path_BFS = Calculate_Avg_Path_BFS(g, 100, "Owl's Brew")
    Avg_Path_DFS = Calculate_Avg_Path_DFS(g, 100, "Owl's Brew")

    print "Avg. Steps to James Gunn using BFS: ", Avg_Path_BFS
    print "Avg. Steps to James Gunn using DFS: ", Avg_Path_DFS


    # Le damos formato a la salida para la visualizacion
    x = ['Breadth First Search', 'Depth First Search']
    energy = [Avg_Path_BFS, Avg_Path_DFS]

    x_pos = [i for i, _ in enumerate(x)]

    plt.barh(x_pos, energy, color='green')
    plt.xlabel("Number of visits")
    plt.title("Average number of visits")
    plt.yticks(x_pos, x)
    plt.show()

    return

if __name__ == '__main__':
    main()