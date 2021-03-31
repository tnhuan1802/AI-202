from search import *

class WaterJugProblem(SearchProblem):
    def __init__(self, waterjug, goal):
        self.waterjug = waterjug
        self.goal = goal

    def getStartState(self):
        return waterjug

    def isGoalState(self, state):
        return state.isGoal(self.goal)

    def getSuccessors(self,state):
        
        succ = []
        for a in state.legalMoves():
            succ.append((state.result(a), a, 1))
        return succ

    def getCostOfActions(self, actions):
        return len(actions)
    
class WaterJugState:
    def __init__(self,capacities, state = (0 , 0)):
        self.state = state
        self.capacities = capacities

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(self.state))
    
    def legalMoves(self):
        c_1, c_2 = self.capacities
        j_1, j_2 = self.state

        action = []

        if j_1 == 0: action.append('fill_1')
        if j_2 == 0: action.append('fill_2')
        if j_1 == c_1: action.append('empty_1')
        if j_2 == c_2: action.append('empty_2')
        if j_1 > 0 and j_1 <= c_1: action.append('pour_1_2')
        if j_2 > 0 and j_1 <= c_2: action.append('pour_2_1')

        return action

    def result(self, action):
        c_1, c_2 = self.capacities
        j_1, j_2 = self.state

        if action == 'fill_1': return WaterJugState((c_1, c_2) ,(c_1, j_2))
        if action == 'fill_2': return WaterJugState((c_1, c_2) ,(j_1, c_2))
        if action == 'empty_1': return WaterJugState((c_1, c_2) ,(0, j_2))
        if action == 'empty_2': return WaterJugState((c_1, c_2) ,(j_1 , 0))
        if action == 'pour_1_2':
            delta = min(j_1, c_2 - j_2)
            return WaterJugState((c_1, c_2) ,(j_1 - delta, j_2 + delta))
        if action == 'pour_2_1':
            delta = min(c_1 - j_1 , j_2)
            return WaterJugState((c_1, c_2) ,(j_1 + delta, j_2 - delta))

    def isGoal(self, state):
        return self.state == state

    def __str__(self):
        return str(self.state)
        
if __name__ == '__main__':
    waterjug = WaterJugState((3,5))
    problem = WaterJugProblem(waterjug, (0,1))

    path = bfs(problem)
    print('BFS found a path of %d moves: %s' % (len(path), str(path)))
    curr = waterjug
    i = 1
    for a in path:
        curr = curr.result(a)
        print('After %d move%s: %s' % (i, ("", "s")[i>1], a))
        print(curr)

        raw_input("Press return for the next state...")   # wait for key stroke
        i += 1