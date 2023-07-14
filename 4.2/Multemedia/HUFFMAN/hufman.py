import heapq
from collections import Counter


class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""

    def __lt__(self, nxt):
        return self.freq < nxt.freq

xx = open("output.txt", "w")
def printNodes(node, val=""):
    newVal = val + str(node.huff)
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)

    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")
        xx.write(f"{node.symbol} -> {newVal}" + "\n")

with open("input.txt", "r") as f:
    lines = f.readlines()

nodes = []
for key, val in Counter(lines[0]).items():
    heapq.heappush(nodes, node(val, key))


while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    left.huff = 0
    right.huff = 1
    newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    heapq.heappush(nodes, newNode)

printNodes(nodes[0])