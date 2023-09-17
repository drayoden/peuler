n = 5 # grid is n x n
nodes = []
source = 1
destination = n**2

# create list of nodes:
i = 1
for x in range(n):
    for y in range(n):
        nodes.append(i)
        i += 1

print(f'nodes: {nodes}\n')

def neighbors(node):
    nlist = []
    if (node % n) != 0:         # right
        nlist.append(node+1)
    if (node+n) in nodes:       # down
        nlist.append(node+n)
    # print(f'[{node}] -- nlist: {nlist}')
    return nlist

# create the graph dictionary: { node: [neighbor list]... }
graph = {}
for node in nodes:
    nextto = neighbors(node)
    # print(f'find neighbors to: {node}: {nextto}')
    graph[node] = nextto

print(f'graph: {graph}\n')

print(f'len(graph): {len(graph)}\n')



# def dfs(g, s, d, p, v):
#     v[s] = True
#     p.append(s)

#     if (s == d):
        

#     pass


# def getAllPaths(graph, source, destination): 
    
#     # mark all nodes as not visited
#     visited = [False for _ in range(len(graph))]

#     # path list:
#     path = []

#     # call dfs to get all the paths:
#     dfs(graph, source, destination, path, visited)




