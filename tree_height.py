# python3

import sys
import threading


def compute_height(n, parents):
    tree = [[] for _ in range(n)]
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)
    
    # Define a recursive function to compute the height of a node
    def height(node):
        if not tree[node]:
            return 0
        return max(height(child) for child in tree[node]) + 1
    
    max_height = height(root)
    return max_height


def main():
    while True:
        input_type = input().split()[0]
        break
    #a = input_type.split()[0]
    if input_type == "I":
        while True:
            n = input()
            n = int(n)
            break
        parents = []
        while True:
            parents = [int(x) for x in input().split()]
            break
        height = compute_height(n, parents)
        print(height)
    elif input_type == "F":
        while True:
            filename = input()
            if 'a' in filename.lower():
                print("Invalid filename")    
            break
        
        with open(filename, 'r') as file:
            n = int(file.readline().strip())
            parents = [int(x) for x in file.readline().strip().split()]
        height = compute_height(n, parents)
        print(height)
    else:
        pass
    
    


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
