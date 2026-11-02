# Extracted from the program screenshot in the DSA manual.
# Please check indentation/symbols before running.

indices
3E. Aim. Write a python program to sort the elements using a quick sort technique . take an
input elements from the user
def quick_sort (arr):
if len(arr) <= 1:
return arr
pivot = arr[-1]
left = []
right = []
for i in range(len(arr) - 1):
if arr[i] < pivot:
left.append(arr[i])
oa
