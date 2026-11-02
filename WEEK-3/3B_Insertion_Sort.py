
def insertion_sort (arr):
      for i in range(1, len(arr)):
          key = arr[i]
     while j >= 0 and arr[j] > key:
          arr[j + ] = arr[j]
           j-=1
arr[j + 1] = key
return arr
n = int(input ("Enter number of elements: "))
arr = []
for i in range(n):
     arr.append(int (input ("Enter element: ")))
result = insertion_sort (arr)
print ("Sorted array:", result)|
