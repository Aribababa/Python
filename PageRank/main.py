from Graph import Graph
import operator
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def main():
    grafo = Graph("StanLee_nodes.csv", "StanLee_edges.csv")
    AdjMat_grafo = grafo.GetAdjacencyMatrix()

    PageRank =  grafo.PageRank(AdjMat_grafo, d=0.85 ,iterations=100)
    PageRank = PageRank.tolist()

    i = 0
    PageRank_Dict = {}
    for key in grafo.GraphDictionary.keys():
        PageRank_Dict[key] = PageRank[0][i]
        i+=1

    sorted_x = sorted(PageRank_Dict.items(), key=operator.itemgetter(1), reverse=True)
    top10 = sorted_x[:10]
    x, b = map(list, zip(*top10))
    print top10

    # Visualisamos el top5 de los nodos

    x_pos = [i for i, _ in enumerate(x)]

    plt.barh(x_pos, b, color='green')
    plt.ylabel("Facebook Page")
    plt.xlabel("PageRank")
    plt.title("los 5 nodos menos influyentes")

    plt.yticks(x_pos, x)
    plt.gca().invert_yaxis()

    plt.show()

    return

if __name__ == '__main__':
    main()