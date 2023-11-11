#!/usr/bin/env python
# coding: utf-8

# In[1]:


# DIAGONAL INTERCHANGE
#0 1 2 -  2 1 0
#3 4 5 -  3 4 5
#6 7 8 -  8 7 6
a = [[0, 1, 2], [3, 4, 5], [6, 7, 8]] 

for i in range(len(a)):
    if i % 2 == 0:
        a[i].reverse()  
for row in a:
    for element in row:
        print(element, end=" ")
    print()


# In[2]:


# INDEX FINDER
# index = 0 1 2 3 4 5 6 7 8 9
#     a = 2 3 1 0 4 5 7 6 9 8
a = [2,3,1,0,4,5,7,6,9,8]
print(a)
output=list(range(len(a)))
print(output)


# In[ ]:




