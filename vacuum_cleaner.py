from search import *

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
    
    def isGoal(self):
        _, rooms = self.state
        for dirt in rooms:
            if dirt == False:
                return False
        return True

    def legalMoves(self):
        vac_pos, rooms = self.state
        n_rooms = len(rooms)
        action = []
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
        vac_pos, rooms = self.state
        n_rooms = len(rooms)
        if action == 'left': return VacuumCleanerState((vac_pos - 1, rooms))
        if action == 'right': return VacuumCleanerState((vac_pos + 1, rooms))
        if action == 'suck':
            rooms[vac_pos] = True
            print(vac_pos)
            print(rooms)
            return VacuumCleanerState((vac_pos, rooms))

    def __str__(self):
        return str(self.state[0]) + ' , ' + str(self.state[1])
if __name__ == '__main__':
    rooms = [False] * 3
    vacuum = VacuumCleanerState((0, rooms))
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