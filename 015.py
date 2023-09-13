# lattice path
# how many paths are in a square grid (n x n) from upper left
# to lower right only moveing right and down from current
# position. For this project n = 20

n = 5 # grid is n x n
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
    print(f'find neighbors to: {node}: {nextto}')
    graph[str(node)] = nextto

print(graph)

# iterate the graph and get all paths:

pathlist = []

def allpaths(g,node,path):
    path.append(node)
    for n in g[str(node)]:
        if n not in path:
            allpaths(g,n,path.copy())
    if path[0] == 1 and path[len(path)-1] == n**2:      
        pathlist.append(path)

allpaths(graph,1,[])

for path in pathlist:
    print(path)








    
         
