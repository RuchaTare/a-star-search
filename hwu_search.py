# -*- coding: utf-8 -*-
"""
Core functions for the A* search problem.
Please see Java source for documentation.
"""

class State:
    """
    Represents a state in the search problem.

    Attributes
    ----------
        None

    Methods
    -------
        isGoal: Checks if the current state is the goal state.
        getHeuristic: Calculates the heuristic value for the current state.
    """

    def isGoal(self):
            """
            Check if the current state is the goal state.

            Returns
            -------
                bool: True if the current state is the goal state, False otherwise.
            """
            pass
    
    def getHeuristic(self):
            """
            Calculates the heuristic value for the current state.

            Returns
            -------
                int: The heuristic value for the current state.
            """
            pass

class SearchOrder:
    """
    Class representing the search order for A* search algorithm.

    Attributes
    ----------
        None

    Methods
    -------
        addToFringe(frontier, parent, children):
            Adds the given parent and children nodes to the frontier.

    """

    def addToFringe(self, frontier, parent, children):
        """
        Adds the given parent and children nodes to the frontier.

        Parameters
        ----------
            frontier (list): 
                The frontier to add the nodes to.
            parent: The parent node.
            children (list): The children nodes.

        Returns
        -------
            None

        """
        pass
    
class ChildWithCost:
    """
    Represents a child node with its associated cost.

    Attributes
    ----------
    node : object
        The child node.
    cost : float
        The cost associated with the child node.

    Methods
    -------
    __str__()
        Returns a string representation of the ChildWithCost object.
    """

    def __init__(self, node, cost):
        self.node = node
        self.cost = cost
        
    def __str__(self):
        return "ChildWithCost [node=" + str(self.node) + ", cost=" + str(self.cost) + "]"
    
class Node:
    """
    Represents a node in a search tree.

    Parameters
    ----------
    value : object
        The value associated with the node.

    Attributes
    ----------
    value : object
        The value associated with the node.
    children : set
        The set of child nodes.
    """

    def __init__(self, value):
        self.value = value
        self.children = set()

    def addChild(self, child, cost):
        """
        Adds a child node to the current node.

        Parameters
        ----------
        child : Node
            The child node to be added.
        cost : float
            The cost associated with the edge from the current node to the child node.

        Returns
        -------
        bool
            True if the child node is added successfully, False otherwise.
        """
        if not (child in self.children):
            self.children.add(ChildWithCost(child, cost))
            return True
        else:
            return False

    def isGoal(self):
        """
        Checks if the current node is a goal node.

        Returns
        -------
        bool
            True if the current node is a goal node, False otherwise.
        """
        return self.value.isGoal()

    def __str__(self):
        """
        Returns a string representation of the node.

        Returns
        -------
        str
            A string representation of the node.
        """
        return "Node [value=" + str(self.value) + "]"
    
class FringeNode:
    """
    Represents a node in the fringe of the A* search algorithm.

    Attributes
    ----------
    node : Node
        The node associated with this fringe node.
    parent : FringeNode 
        The parent fringe node.
    cost : float
        The cost of reaching this node from the start node.

    Methods
    -------
    getFValue()
        Calculates and returns the f-value of the node.
    __str__()
        Returns a string representation of the FringeNode.
    """

    def __init__(self, node, parent, cost):
        self.node = node
        self.parent = parent
        self.gValue = cost
        
        if parent is not None:
            self.gValue += parent.gValue
        
    def getFValue(self):        
        """
        Calculates and returns the f-value of the node.

        Returns
        -------
        float
            The f-value of the node.
        """
        return self.gValue + self.node.value.getHeuristic()
    
    def __str__(self):
        """
        Returns a string representation of the FringeNode.

        Returns
        -------
        str
            A string representation of the FringeNode.
        """
        return "FringeNode [node=" + str(self.node) + ", parent=" + str(self.parent) + ", gValue=" + str(self.gValue) + "]"
    

class SearchProblem:
    """
    Represents a search problem.

    Attributes:
    ----------
    searchOrder : object
        The search order object used to determine the order of nodes in the fringe.

    Methods:
    -------
    doSearch(root)
        Performs a search starting from the given root node.

    """

    def __init__(self, searchOrder):
        """
        Initializes a new instance of the SearchProblem class.

        Parameters:
        ----------
        searchOrder : object
            The search order object used to determine the order of nodes in the fringe.

        """
        self.searchOrder = searchOrder
        
    def doSearch(self, root):
        """
        Performs a search starting from the given root node.

        Parameters:
        ----------
        root : object
            The root node from which the search starts.

        Returns:
        -------
        bool
            True if a goal node is found, False otherwise.

        """
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