from snap import *
import json
import sys

def toJson(UGraph, Json):
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

    with open(Json, 'w') as outfile:
        json.dump(Data, outfile, sort_keys=True, indent=4, separators=(',', ': '))

    return None

File = 'data/facebook/698.edges'
UGraph = LoadEdgeList(PUNGraph, File, 0, 1, ' ')

toJson(UGraph, sys.argv[-1])
