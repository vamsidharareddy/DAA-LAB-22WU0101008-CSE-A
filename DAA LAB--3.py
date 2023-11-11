#!/usr/bin/env python
# coding: utf-8

# In[1]:


# REMOVING DUPLICATES(ARRAY)
a=[1,10,11,12,11,1]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print("the array after removing duplicates:")
print(b)       


# In[2]:


# REMOVING DUPLICATES(LIST)
def remove_duplicates(input_list):
    if not input_list:
        return []

    unique_elements = []
    for item in input_list:
        is_duplicate = False
        for unique_item in unique_elements:
            if item == unique_item:
                is_duplicate = True
                break
        if not is_duplicate:
            unique_elements.insert(len(unique_elements), item) 

    return unique_elements

mixed_list = [1, 12, 11, 10, 11, 1]
result = remove_duplicates(mixed_list)
print(result)  


# In[3]:


# TO FIND WHETHER THE LINKED LIST HAS A LOOP OR NOT
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
            
    def detect_loop(self):
        s = set()
        temp = self.head
        while(temp):
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False  # Return False if no loop is found

list = LinkedList()
list.push(10)
list.push(20)
list.push(30)
list.push(40)

list.head.next.next.next = list.head
if list.detect_loop():
    print("Loop found")
else:
    print("No loop")


# In[1]:


#  TIME COMPLEXITY : N log N
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = merge_sort(arr)

print("Sorted array:", sorted_arr)


# In[2]:


# MAXIMUM SUM
def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0

    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
input_array = [1, -2, 3, -1, 2, 4, -2, 6, -1]
result = max_subarray_sum(input_array)
print(result)


# In[ ]:




