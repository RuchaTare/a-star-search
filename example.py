# -*- coding: utf-8 -*-
"""
Examples of using the provided search code.
Please see the Java source files for full documentation.
"""

import hwu_search

class BreadthFirstSearchOrder(hwu_search.SearchOrder):
    def addToFringe(self, frontier, parent, children):
        for child in children:
            frontier.append(hwu_search.FringeNode(child.node, parent, child.cost))

class DepthFirstSearchOrder(hwu_search.SearchOrder):
    def addToFringe(self, frontier, parent, children):
        for child in children:
            frontier.insert(0, hwu_search.FringeNode(child.node, parent, child.cost))
            
class IntState(hwu_search.State):
    def __init__(self, value, goal=False):
        self.value = value
        self.goal = goal 
    
    def isGoal(self):
        return self.goal 
    
    def getHeuristic(self):
        return 0
    
    def __str__(self):
        return "IntegerState [value=" + str(self.value) + ", goal=" + str(self.goal) + "]"
    
    
def addChild(value, goal, parent):
    child = hwu_search.Node(IntState(value, goal))
    parent.addChild(child, 1)
    return child

root = hwu_search.Node(IntState(0))
print("Root", root)
goal = hwu_search.Node(IntState(5, True))
print("Goal", goal)
child = addChild(1, False, root)
child = addChild(2, False, child)
child = addChild(3, False, child)
addChild(4, False, child)
root.addChild(goal, 1)

order = DepthFirstSearchOrder()
problem = hwu_search.SearchProblem(order)
problem.doSearch(root)