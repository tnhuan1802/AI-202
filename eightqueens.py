from search import *

class NQueensState:
    def __init__(self, N):
        self.state = tuple([-1] * N)
        self.N = N

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(self.state))

    def isGoal(self):
        if self.state[-1] == -1:
            return False
        return not any(self.conflicted(self.state[col], col)
                       for col in range(self.N))

    def legalMoves(self):
        if self.state[-1] != -1:
            return [] #All squares filled
        
        else:
            col = self.state.index(-1)
            return [row for row in range(self.N)
                    if not self.conflicted(row, col)]

    def conflicted(self, row, col):
        return any(self.conflict(row, col, self.state[c], c)
                    for c in range(col))

    def conflict(self, row1, col1, row2, col2):
        return (row1 == row2 or
                col1 == col2 or
                row1 - col1 == row2 - col2 or
                row1 + col1 == row2 + col2)
    def result(self, row):
        col = self.state.index(-1)
        new = list(self.state[:])
        new[col] = row
        new_state = NQueensState(self.N)
        new_state.state = new
        return new_state

    def __str__(self):
        return str(self.state)

class NQueensProblem(SearchProblem):
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


if __name__ == '__main__':
    eight_queens = NQueensState(8)
    problem = NQueensProblem(eight_queens)

    path = bfs(problem)
    print('BFS found a path of %d moves: %s' % (len(path), str(path)))
    curr = eight_queens
    i = 1
    for a in path:
        curr = curr.result(a)
        print('After %d move%s: %s' % (i, ("", "s")[i>1], a))
        print(curr)

        raw_input("Press return for the next state...")   # wait for key stroke
        i += 1