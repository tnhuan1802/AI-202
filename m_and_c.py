from search import *
from copy import deepcopy
from operator import sub, add

MISSIONARY_IDX = 0
CANNIBAL_IDX = 1
BOAT_IDX = 2

class MissionariesAndCannibalsProblem(SearchProblem):
    def __init__(self, initial):
        self.initial = initial

    def getStartState(self):
        return self.initial

    def isGoalState(self, state):
        return state.isGoal()

    def getSuccessors(self, state):
        succ = []
        for a in state.legalMoves():
            succ.append((state.result(a), a, 1))
        return succ

    def getCostOfActions(self, actions):
        return len(actions)


class State:
    def __init__(self, state = (3,3,1)):
        self.state = state
        self.west = state
        self.available_actions = [
            (1, 0, 1),
            (2, 0, 1),
            (0, 1, 1),
            (0, 2, 1),
            (1, 1, 1)
        ]
    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(self.state))

    def isGoal(self):
        return self.state == (0, 0, 0)

    def __str__(self):
        return str(self.state) + ' || ' + str(self.east)

    def legalMoves(self):
        # Actions are actually a list of new valid state
        actions = list(map(lambda x : self.perform_action(x), self.available_actions))
        actions = list(filter(None, actions))
        return actions
    def perform_action(self, action):
        if self.state[BOAT_IDX] == 1:
            tmp = tuple(map(lambda x ,y : x - y, deepcopy(self.state), action))
        else:
            tmp = tuple(map(lambda x ,y : x + y, deepcopy(self.state), action))
        if State(tmp).is_valid:
            return tmp
        else:
            pass
    @property
    def east(self):
        total = (3, 3, 1)
        return tuple(map(lambda x, y: x - y, total, self.west))

    @property
    def num_missionaries(self):
        return self.west[MISSIONARY_IDX]

    @property
    def num_cannibals(self):
        return self.west[CANNIBAL_IDX]

    @property
    def num_boat(self):
        return self.west[BOAT_IDX]

    @property
    def missionaries_are_safe(self):
        east = State(self.east)

        return (self.num_missionaries == 0 or self.num_missionaries >= self.num_cannibals) and \
               (east.num_missionaries == 0 or east.num_missionaries >= east.num_cannibals)

    @property
    def is_valid(self):
        east = State(self.east)

        num_missionaries_valid = (0 <= self.num_missionaries <= 3) and (0 <= east.num_missionaries <= 3)
        num_cannibals_valid = (0 <= self.num_cannibals <= 3) and (0 <= east.num_cannibals <= 3)
        num_boat_valid = (0 <= self.num_boat <= 1) and (0 <= east.num_boat <= 1)

        return num_missionaries_valid and num_cannibals_valid and num_boat_valid and self.missionaries_are_safe

    def result(self, action):
        return State(action)

if __name__ == '__main__':
    m_and_c = State()
    problem = MissionariesAndCannibalsProblem(m_and_c)

    path = bfs(problem)
    if path:
        print('BFS found a path of %d moves: %s' % (len(path), str(path)))
        curr = m_and_c
        i = 1
        for a in path:
            curr = curr.result(a)
            print('After %d move%s: %s' % (i, ("", "s")[i>1], a))
            print(curr)

            raw_input("Press return for the next state...")   # wait for key stroke
            i += 1
    else:
        print('No solution found.')




