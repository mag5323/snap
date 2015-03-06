from snap import *
from func import *
from operator import itemgetter

G = TUNGraph.New()

for N in range(1, 7):
    G.AddNode(N)

G.AddEdge(1, 2)
G.AddEdge(1, 3)
G.AddEdge(2, 3)
G.AddEdge(2, 4)
G.AddEdge(3, 5)
G.AddEdge(4, 5)
G.AddEdge(5, 6)

Centr = []
Neighbors = {}
for NI in G.Nodes():
    NId = NI.GetId()
    Centr.append({'id': NId, 'centr': GetDegreeCentr(G, NId)})

    TempNeighbor = []
    for Id in NI.GetOutEdges():
        TempNeighbor.append(Id)
    Neighbors[NId] = TempNeighbor

Centr.sort(key=lambda x: x['centr'])

Max = Centr.pop()['id']
NIdV = TIntV()
NIdV.Add(Max)
for N in Neighbors[Max]:
    NIdV.Add(N)

SubGraph = GetSubGraph(G, NIdV)
G.Dump()
SubGraph.Dump()

toJson(G)
