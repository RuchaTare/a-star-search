# -*- coding: utf-8 -*-
"""
Examples of using the provided search code.
Please see the Java source files for full documentation.
"""

import hwu_search

class BreadthFirstSearchOrder(hwu_search.SearchOrder):
    """
    Implements the breadth-first search order for searching a graph.

    This class inherits from `SearchOrder` and provides the `addToFringe` method
    to add nodes to the frontier in a breadth-first manner.

    Attributes
    ----------
        None

    Methods
    -------
        addToFringe: Adds the children nodes to the frontier in a breadth-first manner.

    """

    def addToFringe(self, frontier, parent, children):
        """
        Adds the children nodes to the frontier in a breadth-first manner.

        Parameters
        ----------
            frontier (list): The frontier to which the nodes will be added.
            parent (Node): The parent node.
            children (list): The list of child nodes.

        Returns
        -------
            None

        """
        for child in children:
            frontier.append(hwu_search.FringeNode(child.node, parent, child.cost))

class DepthFirstSearchOrder(hwu_search.SearchOrder):
    """
    Depth-first search order implementation.
    """

    def addToFringe(self, frontier, parent, children):
        """
        Add nodes to the fringe in a depth-first manner.

        Parameters
        ----------
        frontier (list): The fringe to add nodes to.
        parent (hwu_search.Node): The parent node.
        children (list): The list of child nodes.

        Returns
        -------
        None
        """
        for child in children:
            frontier.insert(0, hwu_search.FringeNode(child.node, parent, child.cost))
            
class IntState(hwu_search.State):
    """
    Represents an integer state for A* search algorithm.

    Parameters
    ----------
        value (int): The value of the state.
        goal (bool): Whether the state is a goal state or not.

    Attributes
    ----------
        value (int): The value of the state.
        goal (bool): Whether the state is a goal state or not.
    """

    def __init__(self, value, goal=False):
        self.value = value
        self.goal = goal 
    
    def isGoal(self):
        """
        Checks if the state is a goal state.

        Returns
        -------
            bool: True if the state is a goal state, False otherwise.
        """
        return self.goal 
    
    def getHeuristic(self):
        """
        Calculates the heuristic value of the state.

        Returns
        -------
            int: The heuristic value of the state.
        """
        return 0
    
    def __str__(self):
        """
        Returns a string representation of the state.

        Returns
        -------
            str: The string representation of the state.
        """
        return "IntegerState [value=" + str(self.value) + ", goal=" + str(self.goal) + "]"
    
    
def addChild(value, goal, parent):
    """
    Add a child node to the parent node.

    Parameters
    ----------
    value (int): The value of the child node.
    goal (int): The goal value.
    parent (Node): The parent node.

    Returns
    -------
    Node: The newly created child node.
    """
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