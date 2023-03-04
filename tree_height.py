# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    tree = [[] for _ in range(n)]
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)

    def height(node):
        if not tree[node]:
            return 0
        return max(height(child) for child in tree[node]) + 1

    max_height = height(root) + 1
    return max_height

def main():
    text = str(input())
    if "I" in text:
        n = int(input())
        parents = [int(x) for x in input().split()]
        height = compute_height(n, parents)
        print(height)
        sys.exit()
    elif "F" in text:
        filename = str(input())
        if 'a' in filename.lower():
            print("Invalid filename")
            sys.exit()
        with open(filename, 'r') as file:
            n = int(file.readline().strip())
            parents = [int(x) for x in file.readline().strip().split()]
        height = compute_height(n, parents)
        print(height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
#print(numpy.array([1,2,3]))
