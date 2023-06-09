"""# import the important module in python
import numpy as np
         
# make matrix with numpy
a = np.matrix('[6, 2,5; 3, 4,8;1,5,2]')
         
# applying matrix.diagonal() method
c= a.diagonal()
print(c)"""

"""def  diagonalmat(mat):
    print("primary diagonal is:",end=" ")
    row=len(mat)
    col=len(mat[0])
    for i in range(row):
        for j in range(col):
            if i==j:
                print(mat[i][j],end=" ")
    print()
mat=[[1,2,3,4],[4,3,2,1],[5,6,7,8],[1,2,3,4]]
diagonalmat(mat)"""


"""def  diagonalmat(mat):
    print("lower diagonal is:",end=" ")
    row=len(mat)
    col=len(mat[0])
    for i in range(row):
        for j in range(col):
            if i>j:
                print(mat[i][j],end=" ")
    print()
mat=[[1,2,3,4],[4,3,2,1],[5,6,7,8],[1,2,3,4]]
diagonalmat(mat)"""

"""def  diagonalmat(mat):
    print("upper diagonal is:",end=" ")
    row=len(mat)
    col=len(mat[0])
    for i in range(row):
        for j in range(col):
            if i<j:
                print(mat[i][j],end=" ")
    print()
mat=[[1,2,3,4],[4,3,2,1],[5,6,7,8],[1,2,3,4]]
diagonalmat(mat)"""


def  diagonalmat(mat):
    print("non diagonal is:",end=" ")
    row=len(mat)
    col=len(mat[0])
    for i in range(row):
        for j in range(col):
            if i!=j:
                print(mat[i][j],end=" ")
    print()
mat=[[1,2,3,4],[4,3,2,1],[5,6,7,8],[1,2,3,4]]
diagonalmat(mat)




