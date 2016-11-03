import igraph
import plotly

from igraph import *
from plotly.graph_objs import *
from plotly import tools




g = Graph.Read_GML('density/gml/0point1.gml')

g.write_dot('0point1.dot')

g1 = Graph.Read_GML('density/gml/0point2.gml')

g1.write_dot('0point2.dot')

g2 = Graph.Read_GML('density/gml/0point3.gml')

g2.write_dot('0point3.dot')

g3 = Graph.Read_GML('density/gml/0point4.gml')

g3.write_dot('0point4.dot')

g4 = Graph.Read_GML('density/gml/0point5.gml')

g4.write_dot('0point5.dot')

g5 = Graph.Read_GML('density/gml/0point6.gml')

g5.write_dot('0point6.dot')

g6 = Graph.Read_GML('density/gml/0point7.gml')

g6.write_dot('0point7.dot')

g7 = Graph.Read_GML('density/gml/0point75.gml')

g7.write_dot('0point75.dot')

g8 = Graph.Read_GML('density/gml/0point8.gml')

g8.write_dot('0point8.dot')

g9 = Graph.Read_GML('density/gml/0point9.gml')

g9.write_dot('0point9.dot')



