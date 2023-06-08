"""source vertex to all other vertices(considering all other vertices
one by one to all other vertices-dynamic"""
nv=4
inf=999
#algorithm implementation
def floyd_warshall(g):
    distance=list(map(lambda i:list(map(lambda j:j,i)),g))
    #adding vertices individually
    for k in range(nv):
        for i in range(nv):
            for j in range(nv):
                distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])
    print_solution(distance)
    #printing the solution
def print_solution(distance):
    for i in range(nv):
        for j in range(nv):
            if(distance[i][j]==inf):
                print("inf",end=" ")
            else:
                print(distance[i][j],end=" ")
        print(" ")
g=[[0,3,inf,5],[2,0,inf,4],[inf,1,0,inf],[inf,inf,2,0]]
floyd_warshall(g)
                
