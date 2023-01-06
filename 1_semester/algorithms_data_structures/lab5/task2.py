network = {
    "switch0" : ["switch1", "switch2", "switch3"],
    "switch1" : ["switch4", "switch5"],
    "switch2" : ["switch6"],
    "switch3" : ["pc1", "pc2", "pc3"],
    "switch4" : ["pc4", "pc5"],
    "switch6" : ["pc6", "pc7", "pc8"],
    "switch5" : ["server"],
    "server" : [],    
    "pc1" : [],
    "pc2" : [],
    "pc3" : [],
    "pc4" : [],
    "pc5" : [],
    "pc6" : [],
    "pc7" : [],
    "pc8" : []
}

global result 
result = []

def dfs(graph, node, visited):
    if not(node in visited):
        visited.append(node)
        for near_node in graph[node]:
            if len(graph[near_node]) == 0:
                result.append(near_node)
            else:
                dfs(graph, near_node, visited)


dfs(network, "switch0", [])
print(result)
