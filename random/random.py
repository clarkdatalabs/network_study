#Small code to generate a random graph depending on the density and number of nodes given

import igraph
from igraph import *
from sys import version_info

n = 50
d = 0.56
possible_connections = n*(n-1)/2
connections = int(d*possible_connections)
g = Graph.Erdos_Renyi(n,m=connections)
g.write_gml('pointfiveseven.gml')
