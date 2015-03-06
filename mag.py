from snap import *
from func import *
from operator import itemgetter

G = TUNGraph.New()

for N in range(0, 6):
    G.AddNode(N)

G.AddEdge(0, 1)
G.AddEdge(0, 2)
G.AddEdge(1, 2)
G.AddEdge(1, 3)
G.AddEdge(2, 4)
G.AddEdge(3, 4)
G.AddEdge(4, 5)

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

toJson(toObj(G, SubGraph, 1))
