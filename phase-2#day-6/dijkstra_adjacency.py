"""Dijkstra's algorithm is an iterative algorithm that provides us with the shortest path from one particular starting node
(a in our cases)to all other nodes in the graph"""
#python program for dijkstra's single
#source shortest path algorithm.The program is for adjacency matrix representation of the graph
#library for INT_MAX
import sys
class Graph():
    def __init__(self,vertices):
        self.v=vertices
        self.Graph=[[0 for column in range(vertices)] for row in range(vertices)]
    def printsolution(self,dist):
        print("vertex distance from source")
        for node in range(self.v):
            print(node,"t",dist[node])
#a utility function to find the vertex with minimum distance value,from the set of vertex not yet
#included in shortestpath tree
    def  mindistance(self,dist,sptset):
        #initialize minimum distance for next node
        min=sys.maxsize
        #search not nearest vertex not in the shortest path tree
        for v in range(self.v):
            if dist[v]<min and sptset[v]==False:
                min=dist[v]
                min_index=v
        return min_index
#function that implements dijkstra's single shortest path algorithm for a graph represntation using
#adjacency matrix representation
    def dijkstra(self,src):
         dist=[sys.maxsize]*self.v
         dist[src]=0
         sptset=[False]*self.v
         for cout in range(self.v):
             u=self.mindistance(dist,sptset)
             sptset[u]=True
             for v in range(self.v):
                 if(self.Graph[u][v]>0) and (sptset[v]==False) and (dist[v]>dist[u] +self.Graph[u][v]):
                     dist[v]=(dist[u]+self.Graph[u][v])
         self.printsolution(dist)
g=Graph(9)
g.Graph=[ [0,4,0,0,0,0,0,8,0],
               [4,0,8,0,0,0,0,11,0],
               [0,8,0,7,0,4,0,0,2],
               [0,0,7,0,9,14,0,0,0],
               [0,0,0,9,0,10,0,0,0],
               [0,0,4,14,10,0,2,0,0],
               [0,0,0,0,0,2,0,1,6],
               [8,11,0,0,0,0,1,0,7],
               [0,0,2,0,0,0,6,7,0]]
g.dijkstra(0)
          

    
                    
