from search import *

romania_map = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))

if __name__ == "__main__":
    initial = 'Arad'
    goal = 'Bucharest'
    problem = GraphProblem(romania_map, initial, goal)
    path = ucs(problem)
    print(('BFS found a path of %d moves: %s' % (len(path), str(path))))
    curr = initial
    
    i = 1
    for a in path:
        curr = problem.result(curr, a)
        print(('After %d move%s: %s' % (i, ("", "s")[i>1], a)))
        print(curr)

        raw_input("Press return for the next state...")   # wait for key stroke
        i += 1
