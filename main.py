import hwu_search
import numpy as np

class grid_State(hwu_search.State):
    def __init__(self, value, position, goal=False):
        """ Initialializing state for the cell position
        """
        self.value = value
        self.position = position
        self.grid = grid
        self.goal = goal

    def __eq__(self, current_cell):
        return self.position == current_cell.position

    def isGoal(self):
        return self.goal
    
    def __str__(self):
        return "[value=" + str(self.value) + ", goal=" + str(self.goal) + ", Position=" + str(self.position) + "]"

    def getHeuristic(self):
        """ Returns Manhattan distance between position1 and position2 
        """
        heuristic = abs(self.position[0] - goal[0]) + abs(self.position[1] - goal[1])
        return heuristic


class a_Star_Search(hwu_search.SearchOrder):
    def addToFringe(self, frontier, parent, children):

        for child in children:
            temp_child_fringe = hwu_search.FringeNode(child.node, parent, child.cost)
            
            if child == parent and temp_child_fringe.node.value.getHeuristic() > parent.node.value.getHeuristic():
                continue
            
            frontier.append(temp_child_fringe)


def add_child(value, parent, grid):
        children_coords = [
            (-1, 0),
            (0, -1),
            (0, 1),
            (1, 0),
        ]

        parent_x = parent.position[0]
        parent_y = parent.position[1]

        if grid[parent_x][parent_y] != 4:
            grid_limit_x, grid_limit_y = get_grid_limits(grid)
            for child_coords in children_coords:
                x = parent_x + child_coords[0]
                y = parent_y + child_coords[1]

                if 0 <= x < grid_limit_x and 0 <= y < grid_limit_y:
                    cost = grid[x][y]
                    if cost !=0:
                        if cost ==4:
                            child = hwu_search.Node(grid_State(value, (x, y), True))
                            cost = 1
                        else: 
                            child = hwu_search.Node(grid_State(value, (x, y)))
                        child.position=(x, y)
                        # parent.addChild(child, cost)
                        if child.position not in traversed_cells:
                            parent.addChild(child, cost)
                            traversed_cells.append(child.position)
                            add_child("V", child, grid)
                        
                    else: continue
                else: continue
        

def get_grid_limits(grid):
    grid_shape = np.shape(grid)

    return grid_shape[0], grid_shape[1]


if __name__ == '__main__':
    grid = [[1, 1, 1, 1, 1, 1],
            [3, 0, 0, 0, 3, 1],
            [1, 3, 0, 1, 1, 3],
            [1, 3, 3, 4, 1, 1]]

    global traversed_cells
    traversed_cells = []

    grid = np.asarray(grid)
    goal = (3, 3)

    root = hwu_search.Node(grid_State("V", (0,0)))
    root.position = (0, 0)
    traversed_cells.append(root.position)
    add_child("V", root, grid)

    order = a_Star_Search()
    problem = hwu_search.SearchProblem(order)
    problem.doSearch(root)