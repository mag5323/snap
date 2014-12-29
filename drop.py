from snap import *

File = "data/facebook/698.edges"
UGraph = LoadEdgeList(PUNGraph, File, 0, 1, " ")

Nodes = []
Edges = []

NIdToDistH = TIntH()
shortestPaths = []

UGraph.Dump()

for NI in UGraph.Nodes():
    shortestPaths.append(GetShortPath(UGraph, NI.GetId(), NIdToDistH))
print shortestPaths
