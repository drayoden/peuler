# lattice path
# how many paths are in a square grid (n x n) from upper left
# to lower right only moving right or down from current
# position. For this project n = 20

# n = 13: paths: 2704156   5.668s
# n = 14: paths: 10400600  22.558s
# n = 15: paths:

n = 14 # grid is n x n
nodes = []

# create list of nodes:
i = 1
for x in range(n):
    for y in range(n):
        nodes.append(i)
        i += 1

print(f'nodes: {nodes}')


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
    graph[str(node)] = nextto

# print(graph)

# iterate the graph and get all paths:

pathlist = []

def allpaths(g,node,path):
    path.append(node)
    for neighbor in g[str(node)]:
        if neighbor not in path:
            allpaths(g,neighbor,path.copy())
    if path[len(path)-1] == n**2:
        pathlist.append(path)

allpaths(graph,1,[])

print(f'Number of paths: {len(pathlist)}')







    
         
