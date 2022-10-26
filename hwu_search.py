# -*- coding: utf-8 -*-
"""
Core functions for the A* search problem.
Please see Java source for documentation.
"""

class State:
    def isGoal(self):
        pass
    
    def getHeuristic(self):
        pass

class SearchOrder:
    def addToFringe(self, frontier, parent, children):
        pass
    
class ChildWithCost:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost
        
    def __str__(self):
        return "ChildWithCost [node=" + str(self.node) + ", cost=" + str(self.cost) + "]"
    
class Node:
    def __init__(self, value):
        self.value = value
        self.children = set()
    
    def addChild(self, child, cost):
        if not (child in self.children):
            self.children.add(ChildWithCost(child, cost))
            return True
        else:
            return False
        
    def isGoal(self):
        return self.value.isGoal()
    
    def __str__(self):
        return "Node [value=" + str(self.value) + "]"
    
class FringeNode:
    def __init__(self, node, parent, cost):
        self.node = node
        self.parent = parent
        self.gValue = cost
        
        if (parent != None):
            self.gValue += parent.gValue
        
    def getFValue(self):        
        return self.gValue + self.node.value.getHeuristic()
    
    def __str__(self):
        return "FringeNode [node=" + str(self.node) + ", parent=" + str(self.parent) + ", gValue=" + str(self.gValue) + "]"
    

class SearchProblem:
    def __init__(self, searchOrder):
        self.searchOrder = searchOrder
        
    def doSearch(self, root):
        fringe = list()
        fringe.append(FringeNode(root, None, 0))
        visitedStates = set()
        goalNode = None
        
        while (True):
            if (not(fringe)):
                break
            
            searchNode = fringe.pop()
            
            if (searchNode.node in visitedStates):
                continue
            
            if (searchNode.node.isGoal()):
                goalNode = searchNode
                break
            
            self.searchOrder.addToFringe(fringe, searchNode, searchNode.node.children)
            visitedStates.add(searchNode.node)
        
        if (goalNode is None):
            print ("No goal found")
            return False
        else:
            print ("Found goal node: " + str(goalNode.node))
            print ("Cost: " + str(goalNode.gValue))
            print ("Nodes expanded: " + str(len(visitedStates)))
            print ("Path to root:")
            fNode = goalNode
            while (not(fNode is None)):
                print("- node:" + str(fNode.node.value))
                fNode = fNode.parent
            return True