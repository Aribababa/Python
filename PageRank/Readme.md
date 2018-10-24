# PageRank Approximation
*Implementation of an algorithm to approximate the PageRank value of a node using numerical methods to calculate the egienvectors of the graph.*

## Background

In simple terms, Pagerank calculates the influence of the nodes given their links to him. The way in which the influence value or PageRank is defined is by the following formula.

<p align="center">
  <img src="https://qph.fs.quoracdn.net/main-qimg-a9fb139f045563fdf31da58c06666db3">
</p>

Where PR is the value of PageRank and C are the connections that have the nodes that point towards the node that you want to calculate.

For the implementation of the algorithm we must first see how to represent the graph. For ease in the way that the algorithm is planned to be implemented, an adjacency matrix will be used in which a zero matrix is created, whose columns and rows represent the nodes of the graph and for each edge that joins two nodes, one adds to the value that is currently in the corresponding location of the matrix.

<p align="center">
  <img src="https://i.stack.imgur.com/Ucg3W.png">
</p>

The way in which this algorithm is implemented will be algebraically, that is to say matrix calculations. Because this probem has a certain mathematical proof of how to see this as eigenvalues problem, I am not gonig to explain it here, but yu can consult it from this link:
[Understanding PageRank as an eigenvalue problem](https://math.stackexchange.com/questions/1935927/understanding-pagerank-as-an-eigenvalue-problem)



Because this method is iterative, that is, it must be done a certain number of times to obtain a more reliable result. For the iterative part we can use a Power Iteration method which, starting from an initial value of PageRank, approximates the eigenvalues of the pages. The way this algorithm works is to multiply the matrices and then normalize them. The final result will be an eigenvector representing the PageRank. Depending on the number of iterations is the fidelity of the result

## Results

To test the algorithm we will take an example graph with enough nodes as it is Stan Lee which has a little more than 2000 nodes. We will calculate the PageRank with a damping factor of 0.85, as indicated by the same algorithm and with 100 iterations.

```python
grafo = Graph("StanLee_nodes.csv", "StanLee_edges.csv")
AdjMat_grafo = grafo.GetAdjacencyMatrix()
PageRank =  grafo.PageRank(AdjMat_grafo, d=0.85 ,iterations=100)
PageRank = PageRank.tolist()
```

Through the Python Matplotlib library we can visualize a bar graph the influence of each node, for this we take the ten most influential and we see the result.

(Insert useful image here)

By far, the Los Angeles Comic Con node is the most influential node in the entire graph with a PageRank of 0.9071 followed by the Stan Lee Foundation node with a PageRank of 0.2355.

The other part that we can visualize are the 10 least influential nodes. As in the previous, we can visualize using Matplotlib.
 
(Insert another useful image here)

What we can see is that not only is there a less influential node, but there are many nodes that have almost no influence on the graph. This is because the algorithm ponders the pagerank and for each iteration reduces the value until it converges. In this case, what we can conclude is that not only is there a less influential node, but there are many.

## References

[1] Ilse Ipsen (s.f.) The Linear Algebraic Aspects of PageRank [Online]. Available at: http://www4.ncsu.edu/~ipsen/ps/slides_dagstuhl07071.pdf 

[2] Jed Isom (Saturday, April 18, 2015). Simple PageRank Algorithm Description [Online]. Available at: http://simpledatamining.blogspot.com/2015/04/simple-pagerank-algorithm-description.html?m=1 

[3] Wikipedia (October 01, 2018). Power Iteration [Online]. Available at: https://en.wikipedia.org/wiki/Power_iteration 

[4] The University of North Carolina at Chapel Hill (s.f.). The Math Behind Google Student Edition [Online]. Available at: http://www.unc.edu/depts/our/hhmi/hhmi-ft_learning_modules/googlemodule/googlese.html 

[5]Hagen von Eitzen (September 21, 2016) . Understanding PageRank as an eigenvalue problem [Online]. Available at: https://math.stackexchange.com/questions/1935927/understanding-pagerank-as-an-eigenvalue-problem 
