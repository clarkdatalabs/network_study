import igraph
import plotly

from igraph import *
from plotly.graph_objs import *
from plotly import tools



g = Graph.Barabasi(50)
N = g.vcount()
Edges = g.get_edgelist()
layt = g.layout('kk',dim = 3)

Xn=[layt[k][0] for k in range(N)]# x-coordinates of nodes
Yn=[layt[k][1] for k in range(N)]# y-coordinates
Zn=[layt[k][2] for k in range(N)]# z-coordinates

Xe=[]
Ye=[]
Ze=[]

for e in Edges:
    Xe+=[layt[e[0]][0],layt[e[1]][0], None]# x-coordinates of edge ends
    Ye+=[layt[e[0]][1],layt[e[1]][1], None]
    Ze+=[layt[e[0]][2],layt[e[1]][2], None]


trace1=Scatter3d(x=Xe,
               y=Ye,
               z=Ze,
               mode='lines',
               line=Line(color='rgb(125,125,125)', width=1),
               hoverinfo='none'
               )
trace2=Scatter3d(x=Xn,
               y=Yn,
               z=Zn,
               mode='markers',
               marker=Marker(symbol='dot',
                             size=6,
                             colorscale='Viridis',
                             line=Line(color='rgb(50,50,50)', width=0.5)
                             )
               )

axis=dict(showbackground=False,
          showline=False,
          zeroline=False,
          showgrid=False,
          showticklabels=False,
          title=''
          )



layout = Layout(
         title="Barabasi",
         width=1000,
         height=1000,
         showlegend=False,
         scene=Scene(
         xaxis=XAxis(axis),
         yaxis=YAxis(axis),
         zaxis=ZAxis(axis),
        ),
     margin=Margin(
        t=100
    ),
    hovermode='closest',    )

data=Data([trace1, trace2])


fig=Figure(data=data, layout=layout) 


plotly.offline.plot(fig, filename='Barabasi')


