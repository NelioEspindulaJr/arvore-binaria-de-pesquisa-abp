from binaryTree import BinarySearchTree
import re

entries = open('entrada.txt')

processData = re.findall(r"\b(\w+)\b", entries.read())

searchBynaryTree = BinarySearchTree()

# searchBynaryTree.insert(10)
# searchBynaryTree.insert(5)
# searchBynaryTree.insert(15)
# searchBynaryTree.insert(20)

for data in processData:
    print(data)
    searchBynaryTree.insert(data)

print('\n')
searchBynaryTree._print_tree_recursive(searchBynaryTree.root, 0)
