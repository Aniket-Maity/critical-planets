from collections import defaultdict 
   
#This class represents a directed graph using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        self.graph[v].append(u) 
    
    def deleteEdge(self, u,v):
        # print("before delete==>",self.graph)

        self.graph[u].remove(v)
        self.graph[v].remove(u) 
        #     else:
        #         graph2[key] = value
        # print("after delete==>",self.graph)
       
     # Use BFS to check path between s and d 
    def isReachable(self, s, d): 
        # Mark all the vertices as not visited 
        visited =[False]*(self.V) 
   
        # Create a queue for BFS 
        queue=[] 
   
        # Mark the source node as visited and enqueue it 
        queue.append(s) 
        visited[s] = True
   
        while queue: 
  
            #Dequeue a vertex from queue  
            n = queue.pop(0) 
              
            # If this adjacent node is the destination node, 
            # then return true 
            if n == d: 
                return True
  
            #  Else, continue to do BFS 
            for i in self.graph[n]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
        # If BFS is complete without visited d 
        return False
   
# # Create a graph given in the above diagram 
# g = Graph(4) 
# g.addEdge(0, 1) 
# g.addEdge(0, 2) 
# g.addEdge(1, 2) 
# g.addEdge(2, 0) 
# g.addEdge(2, 3) 
# g.addEdge(3, 3) 
  
# u =1; v = 3
  
# if g.isReachable(u, v): 
#     print("There is a path from %d to %d" % (u,v)) 
# else : 
#     print("There is no path from %d to %d" % (u,v)) 
  
# u = 3; v = 1
# if g.isReachable(u, v) : 
#     print("There is a path from %d to %d" % (u,v)) 
# else : 
#     print("There is no path from %d to %d" % (u,v)) 

M, N = map(int, input().split())
g = Graph(N)

edges = []
for _ in range(M):
    a,b = map(int, input().split())
    g.addEdge(a,b)
    edges.append((a,b))

check = []
# print(g.graph)
for i,e in enumerate(edges):
    g.deleteEdge(e[0],e[1])
    # print("after delete==>",e,g.graph)
    if not g.isReachable(e[0],e[1]):
        check.append(e)
    g.addEdge(e[0],e[1])

print({u for v in check for u in v})

  
