from search import *
from copy import deepcopy
class VacuumCleanerProblem(SearchProblem):
    def __init__(self, initial):
        self.initial = initial

    def getStartState(self):
        return self.initial

    def isGoalState(self, state):
        return state.isGoal()

    def getSuccessors(self,state):
        succ = []
        for a in state.legalMoves():
            succ.append((state.result(a), a, 1))
        return succ

    def getCostOfActions(self, actions):
        return len(actions)

#state = (vac_pos, list of room with dirty state)

class VacuumCleanerState:
    def __init__(self, state ):
        self.state = state
    
    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(self.state))

    def isGoal(self):
        _, rooms = self.state
        temp = tuple([True] * len(rooms))
        return True if temp == rooms else False

    def legalMoves(self):
        vac_pos, rooms = self.state
        n_rooms = len(rooms)
        action = []
        if n_rooms == 1:
            pass
        else:
            if vac_pos == 0:
                action.append('right')
            elif vac_pos == n_rooms - 1:
                action.append('left')
            else:
                action.append('left')
                action.append('right')

        if rooms[vac_pos] == False:
            action.append('suck')
        return action

    def result(self, action):
        vac_pos, rooms = deepcopy(self.state)
        n_rooms = len(rooms)
        list_rooms = list(rooms)
        if action == 'left': return VacuumCleanerState((vac_pos - 1, rooms))
        if action == 'right':
            
            return VacuumCleanerState((vac_pos + 1, rooms))
        if action == 'suck':
            list_rooms[vac_pos] = True
            return VacuumCleanerState((vac_pos, tuple(list_rooms)))

    def __str__(self):
        return str(self.state)
if __name__ == '__main__':
    rooms = tuple([False] * 4)
    vacuum = VacuumCleanerState((2, rooms))
    problem = VacuumCleanerProblem(vacuum)

    path = bfs(problem)
    print('BFS found a path of %d moves: %s' % (len(path), str(path)))
    curr = vacuum
    i = 1
    for a in path:
        curr = curr.result(a)
        print('After %d move%s: %s' % (i, ("", "s")[i>1], a))
        print(curr)

        raw_input("Press return for the next state...")   # wait for key stroke
        i += 1