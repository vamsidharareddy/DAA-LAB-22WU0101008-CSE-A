#!/usr/bin/env python
# coding: utf-8

# In[1]:


# LEADER ARRAY
def leader_array(arr):
    n = len(arr)
    
    # The rightmost element is always a leader
    leader = arr[n - 1]
    leaders = [leader]
    
    # Traverse the array from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] >= leader:
            leader = arr[i]
            leaders.insert(0, leader)
    
    return leaders

# Example usage:
arr = [16, 17, 4, 3, 5, 2]
result = leader_array(arr)

print("Leaders in the array:", result)


# In[2]:


# SORTING ARRAY
def alternate_sort(arr):
    arr.sort()
    n = len(arr)
    output = []
    left = 0
    right = n - 1
    
    while left <= right:
        output.append(arr[left])
        if left != right:
            output.append(arr[right])
        
        left += 1
        right -= 1
    
    return output

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = alternate_sort(arr)

print("Output sequence:", result)



# In[ ]:




