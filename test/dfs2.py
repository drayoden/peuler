n = 5 # grid is n x n
nodes = []
source = 1
destination = n**2

graph = {}

for i in range(source,destination+1):
    alist = []
    if (i % n) != 0:
        alist.append(i + 1)
    if source < (i + n) <= destination:
        alist.append(i + n) 
    graph[i] = alist

print(f'graph: \n{graph}\n')
print(f'len(graph) {len(graph)}\n')

def dfs(g,s,d,bv,cp):

    if s == d:
        print(cp)
        return

    bv[s] = True
    



def getAllPaths(graph,source,destination):
    
    # simple list of bools to keep track of which nodes have been visited
    beenVisited = [False for _ in range(len(graph))]

    # the current path from 1 to destination
    currentpath = []

    # append the source to the current path the remaining path is set
    currentpath.append(source)

    # call dfs function to deterine all paths from source to destination
    dfs(graph,source,destination,beenVisited,currentpath)

