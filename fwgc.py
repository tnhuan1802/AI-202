from search import *
from copy import deepcopy

WEST = 0
EAST = 1

class RiverCrossingProblem(SearchProblem):
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

class RiverCrossingState():
    def __init__(self, state = (WEST, WEST, WEST, WEST)):
        self.state = state

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(self.state))
    
    def legalMoves(self):
        f, w , g ,c = deepcopy(self.state)
        # The actions can be west or east
        actions = []
        
        if f == WEST:
            current_side = WEST
            other_side = EAST
        else:
            current_side = EAST
            other_side = WEST

        for idx, thing in enumerate([w, g, c]):
            if thing == f:
                tmp = [f ,w , g ,c]
                tmp[0] = other_side
                tmp[idx + 1] = other_side
                actions.append(tuple(tmp))
        actions.append((other_side, w , g ,c))
        actions = filter(self.is_valid, actions)
        return actions

    def is_valid(self, action):
        f, w ,g, c = action

        goat_eats_cabbage = g == c and f != g
        wolf_eats_goat = w == g and f != w
        invalid = goat_eats_cabbage or wolf_eats_goat
        return not invalid

    def result(self, action):
        return RiverCrossingState(action)

    def isGoal(self):
        return self.state == (EAST, EAST, EAST, EAST)

    def __str__(self):
        return str(self.state)

if __name__ == '__main__':
    fwgc = RiverCrossingState()
    problem = RiverCrossingProblem(fwgc)

    path = bfs(problem)
    if path:
        print('BFS found a path of %d moves: %s' % (len(path), str(path)))
        curr = fwgc
        i = 1
        for a in path:
            curr = curr.result(a)
            print('After %d move%s: %s' % (i, ("", "s")[i>1], a))
            print(curr)

            raw_input("Press return for the next state...")   # wait for key stroke
            i += 1
    else:
        print('No solution found.')
        
        
