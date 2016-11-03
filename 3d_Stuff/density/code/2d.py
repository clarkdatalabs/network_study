import igraph
import plotly

from igraph import *
from plotly.graph_objs import *
from plotly import tools




g = Graph.Read_GML('../1/pointseven.gml')
N = g.vcount()
Edges = g.get_edgelist()
layt = g.layout('kk')

g2 = Graph.Read_GML('../1/pointfourfive.gml')
N2 = g2.vcount()
Edges2 = g2.get_edgelist()
layt2 = g2.layout('kk')


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

Xn2=[layt2[k][0] for k in range(N2)]# x-coordinates of nodes
Yn2=[layt2[k][1] for k in range(N2)]# y-coordinates
nodes2 = [k for k in range(N2)]
Xe2=[]
Ye2=[]


for e in Edges2:
    Xe2+=[layt2[e[0]][0],layt2[e[1]][0], None]# x-coordinates of edge ends
    Ye2+=[layt2[e[0]][1],layt2[e[1]][1], None]
    


trace2=Scatter(x=Xe2,
               y=Ye2,
               mode='lines',
               line=Line(color='rgb(188,231,132)', width=0.8),
               hoverinfo='none'
               )
trace2=Scatter(x=Xn2,
               y=Yn2,
               mode='markers',
               marker=Marker(symbol='dot',
                             size=10,
                             color='rgb(15,163,177)',
                             line=Line(color='rgb(15,163,177)', width=0.5)
                             ),
               text= nodes2,
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
         width=1300,
         height=800,
         showlegend=False,
         hovermode= 'closest'   )




fig = tools.make_subplots(rows=1, cols=2,horizontal_spacing = 0.0)
fig.append_trace(trace1, 1,1)
fig.append_trace(trace2, 1,1)
fig.append_trace(trace3, 1,2)
fig.append_trace(trace4, 1,2)

fig['layout'].update(layout)
fig['layout']['scene1'].update(scene)
fig['layout']['scene2'].update(scene)

plotly.offline.plot(fig, filename='density_1')


