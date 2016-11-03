import igraph
import plotly

from igraph import *
from plotly.graph_objs import *
from plotly import tools




g = Graph.Read_GML('../graphs/4/pointfiveseven.gml')
N = g.vcount()
Edges = g.get_edgelist()
layt = g.layout('kk',dim = 3)

g2 = Graph.Read_GML('../graphs/4/pointfivefive.gml')
N2 = g2.vcount()
Edges2 = g2.get_edgelist()
layt2 = g2.layout('kk',dim = 3)


Xn=[layt[k][0] for k in range(N)]# x-coordinates of nodes
Yn=[layt[k][1] for k in range(N)]# y-coordinates
Zn=[layt[k][2] for k in range(N)]# z-coordinates
nodes = [k for k in  range(N)]


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
               line=Line(color='rgb(188,231,132)', width=1),
               hoverinfo='none'
               )
trace2=Scatter3d(x=Xn,
               y=Yn,
               z=Zn,
               mode='markers',
               marker=Marker(symbol='dot',
                             size=6,
                             color='rgb(15,163,177)',
                             line=Line(color='rgb(188,231,132)', width=0.5)
                             ),
               text=nodes,
               hoverinfo='text'
               )


Xn2=[layt2[k][0] for k in range(N2)]# x-coordinates of nodes
Yn2=[layt2[k][1] for k in range(N2)]# y-coordinates
Zn2=[layt2[k][2] for k in range(N2)]# z-coordinates
nodes2 = [k for k in  range(N2)]


Xe2=[]
Ye2=[]
Ze2=[]

for e in Edges2:
    Xe2+=[layt2[e[0]][0],layt2[e[1]][0], None]# x-coordinates of edge ends
    Ye2+=[layt2[e[0]][1],layt2[e[1]][1], None]
    Ze2+=[layt2[e[0]][2],layt2[e[1]][2], None]


trace3=Scatter3d(x=Xe2,
               y=Ye2,
               z=Ze2,
               mode='lines',
               line=Line(color='rgb(188,231,132)', width=1),
               hoverinfo='none'
               )
trace4=Scatter3d(x=Xn2,
               y=Yn2,
               z=Zn2,
               mode='markers',
               marker=Marker(symbol='dot',
                             size=6,
                             color='rgb(15,163,177)',
                             line=Line(color='rgb(188,231,132)', width=0.5)
                             ),
               text=nodes2,
               hoverinfo='text'
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
         yaxis=YAxis(axis),
         zaxis=ZAxis(axis),
        )






layout = Layout(
     
         width=1300,
         height=800,
         showlegend=False,
         hovermode='closest',    )




fig = tools.make_subplots(rows=1, cols=2,
                          specs=[[{'is_3d': True}, {'is_3d': True}]],horizontal_spacing = 0.0)
fig.append_trace(trace1, 1,1)
fig.append_trace(trace2, 1,1)
fig.append_trace(trace3, 1,2)
fig.append_trace(trace4, 1,2)

fig['layout'].update(layout)
fig['layout']['scene1'].update(scene)
fig['layout']['scene2'].update(scene)


plotly.offline.plot(fig, filename='density3d_4.html')


