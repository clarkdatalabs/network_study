import igraph
import plotly

from igraph import *
from plotly.graph_objs import *
from plotly import tools




g = Graph.Read_GML('../graphs/1/pointseven.gml')

g.write_dot('pointseven.dot')

g1 = Graph.Read_GML('../graphs/1/pointfourfive.gml')

g1.write_dot('pointfourfive.dot')

g2 = Graph.Read_GML('../graphs/2/pointfive.gml')

g2.write_dot('pointfive.dot')

g3 = Graph.Read_GML('../graphs/2/pointsixfive.gml')

g3.write_dot('pointsixfive.dot')

g4 = Graph.Read_GML('../graphs/3/pointfivefive.gml')

g4.write_dot('pointfivefive.dot')

g5 = Graph.Read_GML('../graphs/3/pointsix.gml')

g5.write_dot('pointsix.dot')

g6 = Graph.Read_GML('../graphs/4/pointfiveseven.gml')

g6.write_dot('pointfiveseven.dot')





