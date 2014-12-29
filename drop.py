from snap import *

UGraph = PUNGraph.New()
UGraph.AddNode(1)
UGraph.AddNode(2)
UGraph.AddNode(5)
UGraph.AddNode(6)

UGraph.AddEdge(1, 2)
UGraph.AddEdge(1, 5)
UGraph.AddEdge(1, 6)
UGraph.AddEdge(2, 6)

NIdToDistH = TIntH()
shortestPaths = []

UGraph.Dump()

for NI in UGraph.Nodes():
    shortestPaths.append(GetShortPath(UGraph, NI.GetId(), NIdToDistH))
print shortestPaths
