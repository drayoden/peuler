# lattice path
# how many paths are in a square grid (n x n) from upper left
# to lower right only moving right or down from current
# position. For this project n = 20

# n = 13: paths: 2704156   5.668s (obiwan)
# n = 14: paths: 10400600  22.558s (obiwan)
# n = 15: paths: 40116600  1m56.592s (yoda)
# n = 16: paths:

n = 4 # grid is n x n
nodes = []
pathlist = []
source = 1
dest = n**2

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
    # print(f'n-[{node}] -- nlist: {nlist}')
    return nlist

# create the graph dictionary: { node: [neighbor list]... }
graph = {}
for node in nodes:
    nextto = neighbors(node)
    # print(f'g-find neighbors to: {node}: {nextto}')
    graph[str(node)] = nextto

print()
print(f'graph: {graph}')

print()
print(f'graph length: {len(graph)}')
# bv = [False for _ in range(len(graph))]
# print(f'bv: {bv}')


# print('Done...')
# exit()

# use Depth First Search (dfs) to iterate the graph to get all complete paths (source to dest):
def dfs(g,source,dest,bv,cp):
    if source == dest:
        print(cp)
        return
    bv[source] = True
    cp.append(source)
    for i in g[str(source)]:
        if not bv[i]:
            cp.append(i)
            dfs(g,i,dest, bv, cp)
            cp.pop(i)
    bv[source] = False

def getAllPaths(graph,source,dest):
    print('gap...')
    beingVisited = [False for _ in range(len(graph))]
    currentPath = []
    currentPath.append(source)
    dfs(graph, source, dest, beingVisited, currentPath)

getAllPaths(graph,source, dest)






    
         
