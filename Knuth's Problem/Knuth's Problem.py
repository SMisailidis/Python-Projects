from __future__ import annotations
import sys
import math


# BigInteger usage

class Node:

    def __init__(self, value: float, operation, previous: int):
        self.value = value
        self.prev = previous
        self.type = operation

    def expand(self, parentKey: int) -> list[Node]:
        nodes: list[Node] = []

        curValue = float(self.value)

        sqrtV = math.sqrt(self.value)
        child: Node = Node(sqrtV, "root", parentKey)
        nodes.append(child)

        if abs(self.value - int(self.value) < 0.00000001):
            curValue = int(self.value)

        floorV = math.floor(curValue)

        if self.value == floorV:
            factV = math.factorial(curValue)

            if factV < 620448401733239439360000:
                child: Node = Node(float(factV), "Factorial", parentKey)
                nodes.append(child)
        else:
            child: Node = Node(floorV, "Floor", parentKey)
            nodes.append(child)

        return nodes


class MyHashMap:

    def __init__(self):
        self.previous = None
        self.hashMap: dict = dict()
        self.lPath: list[Node] = []
        self.key = 0

    def add(self, key: int, value: Node) -> None:
        self.hashMap[key] = value

    def getIndex(self, goal: float) -> int or None:

        if len(self.hashMap) == 0:
            print("The number you've tried to search, is your initial number!")
            exit(0)

        for dictKey, dictValue in self.hashMap.items():
            if goal == dictValue.value:
                return int(dictKey)

    def getPath(self, key: int, initV: float) -> None:

        if key == -1:
            return

        self.lPath.append(self.hashMap.get(key))

        for dictKey, dictValue in self.hashMap.items():
            if key == dictKey:
                self.previous = dictValue.prev

        self.getPath(self.previous, initV)

        return

    def setId(self) -> int:
        self.key += 1
        return self.key

    def printSolution(self) -> None:
        self.lPath.pop(len(self.lPath) - 1)
        self.lPath.reverse()

        for value in self.lPath:
            print(value.type)


class Graph:

    def __init__(self, initialValue: float, goal: float):
        self.initV: float = initialValue
        self.goalV: float = goal

    def isGoal(self, value: float) -> bool:
        return value == self.goalV


class Queue:

    def __init__(self, nodeList: list[Node]) -> None:
        self.queue: nodeList[Node] = nodeList
        self.left: int = 0
        self.right: int = len(self.queue)

    def add(self, n: Node) -> None:
        self.queue.insert(self.right, n)
        self.right += 1

    def remove(self) -> Node or None:
        if not self.isEmpty():
            self.right -= 1
            return self.queue.pop(self.left)
        return None

    def isEmpty(self) -> bool:
        return self.right == self.left

    def size(self) -> int:
        return self.right


def algoInput():
    number = input("Give me the number you want to find:  ")

    while True:
        print("Which Algorithm do you want to use?")
        algorithm = input("1: BFS \n2: Iterative deepening\n")

        if algorithm != 1 and algorithm != 2:
            break

    return number, algorithm


def BreadthFirstSearch(G: Graph, hashM: MyHashMap) -> Node or None:
    parentNode: Node = Node(G.initV, None, -1)

    hashM.add(0, parentNode)

    if G.isGoal(parentNode.value):
        return parentNode

    frontier = Queue([parentNode])
    visited = [parentNode]

    while not frontier.isEmpty():

        removedNode = frontier.remove()

        for child in removedNode.expand(hashM.getIndex(removedNode.value)):
            curChildValue = child.value
            hashM.add(hashM.setId(), child)
            if G.isGoal(curChildValue):
                return child
            if curChildValue not in visited:
                visited.append(curChildValue)
                frontier.add(child)
    return None


def IterativeDeepeningSearch(G: Graph, hashM: MyHashMap, limit: int) -> bool:
    hashmap.add(0, Node(G.initV, None, -1))

    for i in range(limit):
        if DepthLimitedSearch(G.initV, G.goalV, hashM, i):
            return True
    return False


def DepthLimitedSearch(value: float, goal: float, hashM: MyHashMap, limit: int) -> bool:
    if value == goal:
        return True

    if limit <= 0:
        return False

    children: list[Node]

    tempParent: Node = Node(value, None, -1)

    children = tempParent.expand(hashM.getIndex(tempParent.value))

    for child in children:
        hashM.add(hashM.setId(), child)
        if DepthLimitedSearch(child.value, goal, hashM, limit - 1):
            return True
    return False


if __name__ == '__main__':

    target, algo = algoInput()
    initialNumber = 4.0

    hashmap: MyHashMap = MyHashMap()
    graph: Graph = Graph(initialNumber, float(target))

    if float(algo) == 1:
        node: Node = BreadthFirstSearch(graph, hashmap)
        if node:
            index: int = hashmap.getIndex(node.value)

            if index != 0:
                hashmap.getPath(index, initialNumber)
                hashmap.printSolution()
                print("The time to find the target with Breadth First Search algorithm was: ")
            else:
                print("Number not Found!")
    elif float(algo) == 2:

        flag = IterativeDeepeningSearch(graph, hashmap, 10000)
        if flag:
            index = hashmap.getIndex(int(target))
            hashmap.getPath(index, initialNumber)
            hashmap.printSolution()
            print("The time to find the target with Iterative Deepening Search algorithm was: ")

    sys.setrecursionlimit(1500)
