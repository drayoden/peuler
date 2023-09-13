# create square graph/grid in memory with added neighbor info:

n = 3
nodes = []
directions = [[1,0],[0,1]] # right or down only

# n x n graph:
for x in range(n):
    for y in range(n):
        nodes.append([x,y])

print(nodes)
print(f'adding neighbor info for right and down directions only:')

def neighbors(n):
    result = []
    for dir in directions:
        newn = [n[0] + dir[0], n[1] + dir[1]]
        if newn in nodes:
            result.append(newn)
    return result

# create the graph dictionary:
nodes_with_neighbors = {}
for node in nodes:
    nodeneighbors = neighbors(node)
    nodes_with_neighbors[str(node)] = nodeneighbors

print(nodes_with_neighbors)



