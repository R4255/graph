def addedge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)
def printgraph(adj):
    for u,l in enumerate(adj):
        print(u,"->",l)
v=4
adj=[[] for i in range(v)]
addedge(adj,0,1)
addedge(adj,0,2)
addedge(adj,1,2)
addedge(adj,1,3)
printgraph(adj)