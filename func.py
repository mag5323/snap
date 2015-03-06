import json

def toObj(G, S, Group):
    Dis = {'links': [], 'nodes': []}
    for N in G.Nodes():
        Dis['nodes'].append({'name': N.GetId()})
    for E in G.Edges():
        Dis['links'].append({'source': E.GetSrcNId(), 'target': E.GetDstNId()})
    for S in S.Nodes():
        Dis['nodes'][S.GetId()] = {'name': S.GetId(), 'group': Group}
    return Dis

def toJson(Dis):
    with open('output.json', 'w') as outfile:
        json.dump(Dis, outfile, indent = 2)

def dumpList(L):
    return ', '.join(map(str, L))
