from queue import Queue

class Graph:
    def __init__(self, vertexNum):
        self.V = vertexNum
        self.graph = {}

    def add_edge(self, src, dst):
        if src in self.graph:
            self.graph[src].append(dst)
        else:
            self.graph[src] = [dst]

        if dst in self.graph:
            self.graph[dst].append(src)
        else:
            self.graph[dst] = [src]

    def print_graph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end = "")
            print(self.graph[i])


    visited = []
    ans = []       
    def dfs(self, node):
        if node not in self.visited:
            self.ans.append(node)
            self.visited.append(node)
            for neighbor in self.graph[node]:
                self.dfs(neighbor)
        return self.ans

    def bfs_iterative(self, start):
        visited = []
        ans = []

        q = Queue(maxsize = 0)
        visited.append(start)
        q.put(start)
        ans.append(start)

        while (q.empty() == False):
            v = q.get()
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    q.put(neighbor)
                    ans.append(neighbor)

        return ans

    visited_bfs = []
    ans_bfs = []
    def bfs_recursive(self, q):

        if q.empty() == True:
            return 

        v = q.get()
        #self.visited_bfs.append(v)
        #print(v, end = " ")
        #self.ans_bfs.append(v)
        #print(self.ans_bfs)

        for neighbor in self.graph[v]:
            if neighbor not in self.visited_bfs:
                self.visited_bfs.append(neighbor)
                self.ans_bfs.append(neighbor)
                q.put(neighbor)
        
        self.bfs_recursive(q)
        #return self.ans_bfs
        
def main():
    graph = Graph(7)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)

    graph.print_graph()

    print("Following is the depth-first-search")
    print(graph.dfs(0))
    print("Following is the breadth-first-search(iterative)")
    print(graph.bfs_iterative(0))
    print("Following is the breadth-first-search(recursive)")
    q = Queue(maxsize=0)
    q.put(0)
    graph.visited_bfs.append(0)
    graph.ans_bfs.append(0)
    graph.bfs_recursive(q)
    print(graph.ans_bfs)

if __name__ == '__main__':
    main()