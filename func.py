import json

def toJson(G):
    Dis = {'links': [], 'nodes': []}
    for N in G.Nodes():
        Dis['nodes'].append({'name': N.GetId()})
    for E in G.Edges():
        Dis['links'].append({'source': E.GetSrcNId(), 'target': E.GetDstNId()})
    with open('output.json', 'w') as outfile:
        json.dump(Dis, outfile, indent = 2)

def dumpList(L):
    return ', '.join(map(str, L))
