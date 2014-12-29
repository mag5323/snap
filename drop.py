from snap import *
import json

File = "data/facebook/698.edges"
UGraph = LoadEdgeList(PUNGraph, File, 0, 1, " ")

Nodes = []
Edges = []

for NI in UGraph.Nodes():
    Node = {}
    Node['name'] = NI.GetId()
    Nodes.append(Node)

    for i in range(NI.GetDeg()):
        Edge = {}
        Edge['source'] = NI.GetId()
        Edge['target'] = NI.GetNbrNId(i)
        Edges.append(Edge)

Data = {'Nodes': Nodes, 'Edges': Edges}

with open('data.json', 'w') as outfile:
    json.dump(Data, outfile, sort_keys=True, indent=4, separators=(',', ': '))
