import copy
import sys 
from random import randint 
map = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
# 07
# 64


for i in range(6):
    map[randint(0,7)][randint(0,7)] = 1


moves = {
    'king' : [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]], 
    # 'queen' : [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]], 
    # 'rook': [[0, 1], [1, 0], [-1, 0], [0, -1]], 
    # 'bishop': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 
    'queen' : [],
    'bishop' : [],
    'rook' : [],
    'knight': [[2,1], [2, -1], [-2, 1], [-2, -1]], 
    'pawn': [[1,0]] 
}

for i in range(-7,8):
    for q in range(-7,8):
        if i == 0 or q == 0:
            moves['rook'].append([i,q])
        if abs(i) == abs(q):
            moves['bishop'].append([i,q])
    
moves['queen'] = moves['rook'] + moves['bishop']

# print(moves)
routes = []
graph = {'00':[]}

def ats(a):
    return str(a[0]) + str(a[1])

def bfs(nodes, path, fig, goal):
    global routes
    global graph 
    # print(nodes)
    fig_move = moves[fig]
    new_nodes = []
    for i in nodes:
        if i == goal:
            return
        for q in fig_move:
            next_move = copy.deepcopy(i)
            next_move[0] += q[0]
            next_move[1] += q[1]
            if next_move not in path and 8 > next_move[0] >= 0 and 8 > next_move[1] >= 0 and map[next_move[0]][next_move[1]] == 0:
                if (ats(i)) not in graph.keys():
                    graph[ats(i)] = []
                graph[ats(i)].append(ats(next_move))
                new_nodes.append(next_move)
                path.append(next_move)
                routes.append([i, next_move])
    if len(new_nodes) != 0:
        bfs(new_nodes, path, fig, goal)
    

def trace(route, end):
    global result
    if route[-1] not in list(graph.keys()) :
        graph[route[-1]] = []
        return False 
    for i in graph[route[-1]]:
        if i == end:
            result = "".join(route)
        if i in route:
            return False
        else:
            nr = copy.deepcopy(route)
            nr.append(i)
            trace(nr, end)


def find(start, end, fig):
    global result
    bfs([start], [], fig, end)
    print(graph)
    trace([ats(start)], ats(end))
    try:
        return result 
    except:
        return False 



route1 = (find([0,7], [5,4], 'king'))
route2 = (find([0,7], [5,4], 'king'))
print(route1, route2)

from BoyerMoore import BoyerMooreSearch

s = ''
for i in range(0, len(route1), 2):
    if len(BoyerMooreSearch(route2, route1[i:i+2])) > 0:
        s+=route1[i:i+2]

print(s)