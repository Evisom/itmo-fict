storage = {
    "big_box" : ["box1", "box2", "box3"],
    "box1" : ["box11", "box12" , "box13"],
    "box2" : ["box21", "box22"], 
    "box3" : ["key"],
    "key" : [],
    "box11" : ["box111"],
    "box111" : [],
    "box12" : [],
    "box13" : ["box131"],
    "box131" : [],
    "box21" : [],
    "box22" : ["box221"],
    "box221" : []
}

def bfs(graph, nodes):
    if len(nodes) == 0:
        return False 
    print(nodes)
    next_level = []
    for node in nodes:
        for child in graph[node]:
            next_level.append(child)
            if child == 'key':
                return True
    return bfs(graph, next_level)


print(bfs(storage, ['big_box']))
