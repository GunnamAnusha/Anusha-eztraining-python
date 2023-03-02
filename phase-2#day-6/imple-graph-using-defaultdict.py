#import dictionary for graph
from collections import defaultdict

#add edge to graph:function
graph=defaultdict(list)
def addedge(graph,u,v):
    graph[u].append(v)
    
#function description
def generate_edges(graph):
    edges=[]
    
#for each node in graph
    for node in graph:
        #for each neighbour node of a single node
        for neighbour in graph[node]:
            #if edge exists then append
            edges.append((node,neighbour))
    return edges

#declaring-graph as dictionary
addedge(graph,'a','c')
addedge(graph,'b','c')
addedge(graph,'b','e')
addedge(graph,'c','d')
addedge(graph,'c','e')
addedge(graph,'c','a')
addedge(graph,'c','b')
addedge(graph,'e','b')
addedge(graph,'d','c')
addedge(graph,'e','c')
#printing graph
print(generate_edges(graph))
            
