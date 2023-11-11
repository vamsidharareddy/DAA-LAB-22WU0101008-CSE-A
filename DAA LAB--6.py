#!/usr/bin/env python
# coding: utf-8

# In[1]:


# MATRIX SORTING AND DIAGONAL REPLACEMENT
def print_1(mat, n, m):
    for i in range(n):
        for j in range(m):
            print( mat[i][j], end = " ")
        print()
def makediagonalzero(mat, n, m):
    for i in range(n):
        for j in range(m):
            if (i == j or (i + j + 1) == n):
                mat[i][j] = 0
    print_1(mat, n, m)
if __name__ == "__main__":
    n = 3
    m = 3
    mat = [[ 2, 1, 7 ],
        [ 3, 7, 2 ],
        [ 5, 4, 9 ]]

    makediagonalzero(mat, n, m)


# In[2]:


# INTEGER MULTIPLICATION WITHOUT OPERATORS
def product( x , y ):
    if x < y:
        return 0
    elif y != 0:
        return (x + product(x, y - 1))
    else:
        return product(y, x)
x = 5
y = 2
print( product(x, y))


# In[ ]:




