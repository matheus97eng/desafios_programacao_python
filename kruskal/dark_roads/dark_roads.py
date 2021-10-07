class Street:
    def __init__(self, edge, vertex):
        self.v = vertex
        self.e = edge
        self.graphs = []

    def add_street(self,u,v,w):
      self.graphs.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xfind = self.find(parent, x)
        yfind = self.find(parent, y)
        if (rank[xfind] < rank[yfind]):
            parent[xfind] = yfind
        elif (rank[xfind] > rank[yfind]):
            parent[yfind] = xfind
        else:
            parent[yfind] = xfind
            rank[xfind] += 1

    def kruskal(self):
        parent = []
        rank = []
        amount_save = 0
        self.graphs = sorted(self.graphs, key=lambda item: item[2])
        for node in range(self.e):
            parent.append(node)
            rank.append(0)
        for i in range(self.v):
            u, v, w = self.graphs[i]
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                self.apply_union(parent, rank, x, y)
            else:
                amount_save += w
        return amount_save

def test_case(m,n):

    execute = Street(m,n)     # instancia classe

    for i in range(n):              # lendo cada grafo
        u, v, w = [int(i) for i in sys.stdin.readline().split()]
        #u, v, w = int(u), int(v), int(w)
        execute.add_street(u,v,w)

    amount_save = execute.kruskal()
    print(amount_save)

# main program

import sys

m, n = [int(i) for i in sys.stdin.readline().split()]
#m, n = int(m), int(n)

while (m > 0 and n > 0):
    test_case(m,n)
    m, n = [int(i) for i in sys.stdin.readline().split()]
    #m, n = int(m), int(n)
