# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

class Node:
    def __init__(self, state = None, parent = None, action = None, path_cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost  = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1


    def solution(self):
        return [node.action for node in self.path()[1:]]

    def path(self):
        node , path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

# def treeSearch(problem, frontier):
#     frontier.push(Node(problem.getStartState()))
#     while frontier:
#         if frontier.isEmpty(): return None
#         node = frontier.pop()
#         if problem.isGoalState(node.state):
#             return node.solution()
#         for state, action, step_cost in problem.getSuccessors(node.state):
#             child = Node(state, node, action, node.path_cost + step_cost)
#             frontier.push(child) 

def graphSearch(problem, frontier):
    frontier.push(Node(problem.getStartState()))
    explored = set()
    while frontier:
        if frontier.isEmpty(): return None
        node = frontier.pop()
        # print(node.state.state)
        if problem.isGoalState(node.state):
            return node.solution()
        explored.add(node.state)
        for state, action, step_cost in problem.getSuccessors(node.state):
            
            child = Node(state, node, action, node.path_cost + step_cost)
            if child.state not in explored and child not in frontier.list:
                frontier.push(child)

def depthFirstSearch(problem):
    fringe = util.Stack()
    return graphSearch(problem, fringe)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    fringe = util.Queue()
    return graphSearch(problem, fringe)

def uniformCostSearch(problem):
    frontier = util.PriorityQueue()
    initial = Node(problem.getStartState())
    frontier.push(initial, initial.path_cost)
    explored = set()
    while frontier:
        if frontier.isEmpty(): return None
        node = frontier.pop()
        if problem.isGoalState(node.state):
            return node.solution()
        explored.add(node)
        for state, action, step_cost in problem.getSuccessors(node.state):
            child = Node(state, node, action, node.path_cost + step_cost)
            frontier.update(child, child.path_cost)

def depth_limited_search(problem, limit):
    def recursive_dls(node, problem, limit):
        if problem.isGoalState(node.state):
            return node.solution()
        elif limit == 0:
            return 'cutoff'
        else:
            cutoff_occurred = False
            for state, action, step_cost in problem.getSuccessors(node.state):
                child = Node(state, node, action, node.path_cost + step_cost)
                result = recursive_dls(child, problem, limit - 1)

                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return 'cutoff' if cutoff_occurred else None
        
    return recursive_dls(Node(problem.getStartState()), problem, limit)

def iterative_deepening_search(problem):
    depth = 0
    while(True):
        result = dls(problem, depth)
        if result != 'cutoff':
            return result
        depth += 1

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
dls = depth_limited_search
ids = iterative_deepening_search
astar = aStarSearch
ucs = uniformCostSearch
