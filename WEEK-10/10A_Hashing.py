# Hashing using Separate Chaining, Linear Probing, and Quadratic Probing

# Separate Chaining
def separate_chaining(keys, size):
    table = [[] for _ in range(size)]

    for key in keys:
        index = key % size
        table[index].append(key)

    print("\nSeparate Chaining:")
    for i in range(size):
        print(i, ":", table[i])


# Linear Probing
def linear_probing(keys, size):
    table = [None] * size

    for key in keys:
        index = key % size
        i = 0

        while i < size and table[(index + i) % size] is not None:
            i += 1

        if i < size:
            table[(index + i) % size] = key
        else:
            print("Hash table is full. Cannot insert", key)

    print("\nLinear Probing:")
    for i in range(size):
        print(i, ":", table[i])


# Quadratic Probing
def quadratic_probing(keys, size):
    table = [None] * size

    for key in keys:
        index = key % size
        i = 0

        while i < size and table[(index + i * i) % size] is not None:
            i += 1

        if i < size:
            table[(index + i * i) % size] = key
        else:
            print("Cannot insert", key)

    print("\nQuadratic Probing:")
    for i in range(size):
        print(i, ":", table[i])


# Main Program
size = int(input("Enter hash table size: "))
n = int(input("Enter number of elements: "))

keys = []
for i in range(n):
    key = int(input("Enter element: "))
    keys.append(key)

separate_chaining(keys, size)
linear_probing(keys, size)
quadratic_probing(keys, size)
