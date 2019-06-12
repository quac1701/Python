from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = [False]*(len(self.graph))


    def addEdge(self, u,v):
        self.graph[u].append(v)

    def dfsInit(self, s,visited,stack):
        count = int(not stack==[]) 
        visited[s] = True
        stack.append(s)
        print(s)
        while(stack):
            for i in self.graph[s]:
                if (visited[i] == False):
                    count += 1
                    self.dfsInit(i,visited,stack)
            
            
            if(count == 1):
                stack.pop(len(stack)-1)


    def dfs(self,s):
        visited = [False]*(len(self.graph))
        stack = []
        self.dfsInit(s,visited,stack)



    
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 4)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 5)
 
g.dfs(0)

                

        

