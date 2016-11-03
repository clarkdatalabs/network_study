import igraph
import plotly

from igraph import *
from plotly.graph_objs import *
from plotly import tools




g = Graph.Read_GML('gml/50_49.gml')
N = g.vcount()
Edges = g.get_edgelist()
layt = g.layout('kk')


Xn=[layt[k][0] for k in range(N)]# x-coordinates of nodes
Yn=[layt[k][1] for k in range(N)]# y-coordinates
nodes = [k for k in range(N)]
Xe=[]
Ye=[]


for e in Edges:
    Xe+=[layt[e[0]][0],layt[e[1]][0], None]# x-coordinates of edge ends
    Ye+=[layt[e[0]][1],layt[e[1]][1], None]
    


trace1=Scatter(x=Xe,
               y=Ye,
               mode='lines',
               line=Line(color='rgb(188,231,132)', width=0.8),
               hoverinfo='none'
               )
trace2=Scatter(x=Xn,
               y=Yn,
               mode='markers',
               marker=Marker(symbol='dot',
                             size=10,
                             color='rgb(15,163,177)',
                             line=Line(color='rgb(15,163,177)', width=0.5)
                             ),
               text= nodes,
               hoverinfo='text',
               
               )

axis=dict(showbackground=False,
          showline=False,
          zeroline=False,
          showgrid=False,
          showticklabels=False,
          title=''
          )

scene = Scene(
         xaxis=XAxis(axis),
         yaxis=YAxis(axis)
        )





layout = Layout(
         width=800,
         height=800,
         showlegend=False,
         scene= scene,
         hovermode= 'closest'   )




data=Data([trace1, trace2])
fig=Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='50_49')


