# Extracted from the program screenshot in the DSA manual.
# Please check indentation/symbols before running.

def merge_sort (arr):
if len(arr) <= 1:
return arr
mid = len(arr) // 2
left = arr[:mid]
right = arr[mid:]
left = merge_sort (left)
right = merge_sort (right)
return merge(left, right)
def merge(left, right):
result = []
i-=0
“9
while i < len(left) and j < len(right):
if left{i] < right[j]:
result. append (left [i])
i¢=1
else:
result.append (right [j])
2 a
