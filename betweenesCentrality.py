import networkx as nx
from random import choice

n = int(input("Please enter number of vertices:"))
m = int(input("Please enter the random edges to be added for each node:"))
p = float(input("Please enter the probability of adding a traingle after adding a random edge:"))
inc = int(input("Please enter the number of edges to increment it with:"))


g = nx.powerlaw_cluster_graph(n,m,p)

nx.write_graphml(g,"plc_"+str(n)+".graphml")

for i in range(4,0,-1):
	for x in range(0,inc*i):
		v1 = choice(g.nodes())
		v2 = choice(g.nodes())
		while (v1==v2 or g.has_edge(v1,v2)):
			v2 = choice(g.nodes())
			v1 = choice(g.nodes())
		g.add_edge(v1,v2)
	nx.write_graphml(g,"plc_"+str(n)+"_"+str(i)+".graphml")



