from __future__ import annotations
import sys

import math


class Node:

    def __init__(self, value: float, operation):
        self.value = value
        self.type = operation

    def expand(self) -> list[Node]:
        nodes: list[Node] = []

        curValue = float(self.value)

        if abs(self.value - int(self.value) < 0.00000001):
            curValue = int(self.value)

        floorV = math.floor(curValue)

        if self.value == floorV:
            factV = math.factorial(curValue)
            if factV <= 2147483647:
                child: Node = Node(float(factV), "Factorial")
                nodes.append(child)
        else:
            child: Node = Node(floorV, "Floor")
            nodes.append(child)

        sqrtV = math.sqrt(self.value)
        child: Node = Node(sqrtV, "root")
        nodes.append(child)

        return nodes


class MyHashMap:

    def __init__(self):
        self.hashMap: dict = dict()
        self.lPath: list[Node] = []

    def getTargetIndex(self, goal: float) -> float or None:
        if len(self.hashMap) == 0:
            print("The number you've tried to search, is your initial number!")
            exit(0)

        for dictKey, dictValue in self.hashMap.items():
            if goal == dictValue.value:
                return float(dictKey)

    def getPath(self, i: float, initV: float) -> None:
        key = i
        if i == 0:
            return

        if len(self.hashMap) == 0:
            return None

        if i != initV:
            value = i
            for dictKey, dictValue in self.hashMap.items():
                if value == dictValue.value:
                    key = dictKey

            self.getPath(key, initV)

        return

    def printSolution(self) -> None:
        pass


class MyList:

    def __init__(self):
        self.list: list[list[Node]] = []
        self.lPath: list[Node] = []

    def addNode(self, n: Node, x) -> None:
        self.list[x].append(n)

    def getTargetIndex(self, goal: Node):

        if len(self.list) == 0:
            print("The number you've tried to search, is your initial number!")
            exit(0)

        if goal is None:
            return None

        for r in self.list:
            if r.index(goal):
                return r.index(goal)

    def getPath(self, i) -> None:

        if i is None:
            return

        previous: Node = self.list[i][0]

        self.lPath.append(previous)

        for i in range(i - 1, 0, -1):
            for j in range(len(self.list[i])):
                curr: Node = self.list[i][j]
                if curr.value is previous.value:
                    self.getPath(i)

    def printSolution(self) -> None:
        pass


class Graph:

    def __init__(self, initialValue: float, goal: float):
        self.initV: float = initialValue
        self.goalV: float = goal
        self.mList: MyList = MyList()
        self.mHashMap: MyHashMap() = MyHashMap()

    def isGoal(self, value: float) -> bool:
        return value is self.goalV


class Queue:
    def __init__(self) -> None:
        self.queue: list[Node] = []
        self.left: int = 0
        self.right: int = 0

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


def BreadthFirstSearch(G: Graph) -> Node or None:
    x = 0
    firstNode: Node = Node(G.initV)
    if G.isGoal(firstNode.value):
        return firstNode
    frontier = Queue([firstNode])
    visited = [firstNode]

    while not frontier.isEmpty():
        removedNode = frontier.remove()
        G.mList.addNode(removedNode, x)
        for child in removedNode.expand():
            curChildValue = child.value
            G.mList.addNode(child, x)
            if G.isGoal(curChildValue):
                return child
            if curChildValue not in visited:
                visited.append(curChildValue)
                frontier.add(child)
        x += 1


def IterativeDeepeningSearch(G: Graph, limit) -> bool:
    for i in range(limit):
        if DepthLimitedSearch(G.initV, G.goalV, G.mHashMap.hashMap, i):
            return True
    return False


def DepthLimitedSearch(value, goal, hashMap, limit) -> bool:
    if value == goal:
        return True

    if limit <= 0:
        return False

    children: list[Node]

    children = Node(value, 0).expand()

    for child in children:
        hashMap[value] = child
        if DepthLimitedSearch(child.value, goal, hashMap, limit - 1):
            return True
    return False


if __name__ == '__main__':

    target, algo = algoInput()
    initialNumber = 4.0

    graph: Graph = Graph(initialNumber, float(target))

    if float(algo) == 1:
        node: Node = BreadthFirstSearch(graph)
        index = graph.mList.getTargetIndex(node)
        if index:
            graph.mList.getPath(index)
            graph.mList.printSolution()
            print("The time to find the target with Breadth First Search algorithm was: ")
        else:
            print("Number not Found!")
    elif float(algo) == 2:

        flag = IterativeDeepeningSearch(graph, 10)
        if flag:
            index = graph.mHashMap.getTargetIndex(float(target))
            graph.mHashMap.getPath(index, initialNumber)
            graph.mHashMap.printSolution()
            print("The time to find the target with Iterative Deepening Search algorithm was: ")

    sys.setrecursionlimit(1500)
