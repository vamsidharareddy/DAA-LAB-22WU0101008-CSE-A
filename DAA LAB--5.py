#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ROWS WITH MOST NO OF ONE'S
array = [[1,0,1,1],[1,1,1,1],[1,0,1,0],[1,0,0,1]]
max_count = 0
max_row = 0
for i in range(len(array)):
    count = 0
    for j in range(len(array[0])):
        if array[i][j] == 1:
            count += 1
    if count > max_count:
        max_count = count
        max_row = i
print(max_row + 1)


# In[2]:


# MIDDLE ROW AND COLUMN SUM
def middlesum(mat, n):
    row_sum = 0
    col_sum = 0

    for i in range(n):
        row_sum += mat[5 // 2][i]

    print("Sum of middle row = ", row_sum)

    for i in range(n):
        col_sum += mat[i][5 // 2]

    print("Sum of middle column = ", col_sum)

    return row_sum, col_sum

mat = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 12],
       [10, 11, 13, 14, 15]]

row_sum, col_sum = middlesum(mat, 3)
s = row_sum + col_sum 
print(s)


# In[ ]:




