import igraph
import plotly

from igraph import *
from plotly.graph_objs import *
from plotly import tools




g = Graph.Read_GraphML('50_49.graphml')
N = g.vcount()
Edges = g.get_edgelist()
layt = g.layout('kk',dim = 3)
print(g.vertex_attributes())

Xn=[layt[k][0] for k in range(N)]# x-coordinates of nodes
Yn=[layt[k][1] for k in range(N)]# y-coordinates
Zn=[layt[k][2] for k in range(N)]# z-coordinates

Xg.nodes()
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
                             color='#0e9aba',
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

scene = Scene(
         xaxis=XAxis(axis),
         yaxis=YAxis(axis),
         zaxis=ZAxis(axis),
        )

scene1 = Scene(
         xaxis=XAxis(axis),
         yaxis=YAxis(axis),
         zaxis=ZAxis(axis),
         camera=dict(
            eye=dict(
                x=1.25,
                y=1.25,
                z=1.3
            )
        )
        )




layout = Layout(
         title="Barabasi",
         width=1300,
         height=800,
         showlegend=False,
         hovermode='closest',    )




fig = tools.make_subplots(rows=1, cols=2,
                          specs=[[{'is_3d': True}, {'is_3d': True}]],horizontal_spacing = 0.0)
fig.append_trace(trace1, 1,1)
fig.append_trace(trace2, 1,1)
fig.append_trace(trace1, 1,2)
fig.append_trace(trace2, 1,2)

fig['layout'].update(layout)
fig['layout']['scene1'].update(scene1)
fig['layout']['scene2'].update(scene)


plotly.offline.plot(fig, filename='Barabasi')


