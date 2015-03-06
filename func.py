import json

def toJson(G):
    Dis = {'Edges': [], 'Nodes': []}
    for N in G.Nodes():
        Dis['Nodes'].append({'name': N.GetId()})
    for E in G.Edges():
        Dis['Edges'].append({'source': E.GetSrcNId(), 'target': E.GetDstNId()})
    with open('output.json', 'w') as outfile:
        json.dump(Dis, outfile, indent = 2)

def dumpList(L):
    return ', '.join(map(str, L))
