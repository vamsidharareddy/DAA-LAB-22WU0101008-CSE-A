#!/usr/bin/env python
# coding: utf-8

# In[1]:


# TRIPLET AND THEIR SUM
def find_triplets_with_sum(arrorder, target_sum):
    arr.sort() 
    n = len(arr)
    triplets = []

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target_sum:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return triplets

arr = [1, 2, 3, 4, 5]

target_sum = 9

result = find_triplets_with_sum(arr, target_sum)

if result:
    print(f"Triplets that sum to {target_sum}:")
    for triplet in result:
        print(triplet)
else:
    print(f"No triplets found that sum up to {target_sum}")


# In[2]:


# SORTING AN ARRAY
def insertionSort(array):

    for step in range(1, len(array)):
        n = array[step]
        j = step - 1     
        while j >= 0 and n < array[j]:
            array[j + 1] = array[j]
            j = j - 1        
            array[j + 1] = n


data = [0, 0, 1, 2, 0, 1, 2, 2, 1] 
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)


# In[ ]:




