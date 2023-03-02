graph={               #taken values in the form of dictionary as it has unique keys which satisfies our bfs condition
 '5':['3','7'],       #that is avoid duplicates in a graph
 '3':['2','4'],
 '7':['8'],
 '2':[],
 '4':['8'],
 '8':[]
 }
#bfs-we use queue
visited=[] #list for visited nodes
queue=[]  #initialize a queue we use becoz FIFO

def bfs(visited,graph,node):
    visited.append(node) #the visited node should be appended
    queue.append(node)  #and that node should be added in the queue

    while queue: #creating loop to visit
        m=queue.pop(0)  #and that visited should be popped
        print(m,end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)  #now add the non-visited nodes
                queue.append(neighbour)
bfs(visited,graph,'5')  #function call
                        #the order should be followed suppose if we place 8 there then no other nodes are get visited
                        #as its a index based
