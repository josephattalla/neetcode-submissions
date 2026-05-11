class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        # make sure src & dst are vertices
        if src not in self.graph:
            self.graph[src] = set()
        if dst not in self.graph:
            self.graph[dst] = set()
        # add dst to src neighbors
        self.graph[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        # make sure src & dst are vertices
        if src not in self.graph:
            self.graph[src] = set()
        if dst not in self.graph:
            self.graph[dst] = set()
        # remove dst from src
        if dst in self.graph[src]:
            self.graph[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        # initiate queue and visited
        q = deque([src])
        visited = set([src])

        while q:
            cur = q.popleft()
            if cur == dst:
                return True
            
            for neighbor in self.graph[cur]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        
        return False
