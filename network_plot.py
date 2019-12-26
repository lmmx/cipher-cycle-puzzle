from os import linesep as nl
import networkx as nx
import matplotlib.pyplot as plt
from string import ascii_uppercase

def decipher_alpha_pair(edge):
    deciphered = []
    for number in edge:
        if 0 < number < 27:
            deciphered.append(ascii_uppercase[number - 1])
        else:
            deciphered.append(number)
    return deciphered

with open("network.csv", "r") as f:
    net = [f"{line.rstrip(nl)}".split(',') for line in f.readlines()]
    net = dict([[int(node) for node in edge] for edge in net])

net_entries = list(net.items())
alpha_net_entries = [decipher_alpha_pair(edge) for edge in net_entries]

A = nx.Graph()
A.add_edges_from(net_entries)

plt.figure(1)
nx.draw(A, with_labels=True)

plt.figure(2)
B = nx.Graph()
B.add_edges_from(alpha_net_entries)
nx.draw(B, with_labels=True)

plt.show()
