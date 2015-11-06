'''
Created on Nov 8, 2014

@author: Gary
'''

import fileinput
import graph
import matplotlib.pyplot as plt
import math
import BellmanFord

def plotEdge( plot_axis, x0, y0, x1, y1, weight, clr):
    d0 = 4 # This is an offset so the edge is not drawn to the middle of vertex
    d1 = 3 # offset for edges (perpendicular to the edge)
    d2 = 20 # This is an offset to the end of the arrow tails
    dx = x1-x0
    dy = y1-y0
    length = math.sqrt(dx*dx+dy*dy)
    if length > 0:
        vx = dx/length
        vy = dy/length
        plot_axis.plot([x0+vx*d0+vy*d1,x1-vx*d0+vy*d1],[y0+vy*d0-vx*d1,y1-vy*d0-vx*d1], color=clr) # Draw a line

        # Plot arrows
        plot_axis.plot([x1-vx*d2+vy*4+vy*d1,x1-vx*d0+vy*d1],[y1-vy*d2-vx*4-vx*d1,y1-vy*d0-vx*d1], color=clr)
        plot_axis.plot([x1-vx*d2-vy*4+vy*d1,x1-vx*d0+vy*d1],[y1-vy*d2+vx*4-vx*d1,y1-vy*d0-vx*d1], color=clr)

        plot_axis.text( x0+dx/1.5+vy*10-10, y0+dy/1.5-vx*10-8, weight)

# Parse graph.txt and populate mygraph structure.
mygraph = graph.graph()
isVertices = True
for line in fileinput.input("graph.txt"):
    if isVertices:
        if "----------" in line:
            isVertices = False
        else: #read vertices in this part
            split = line.split()
            mygraph.addVertex(split[0],float(split[1]),float(split[2]))
    else:     #read    edges in this part
        split = line.split()
        mygraph.addEdge(split[0], split[1], float(split[2]))
    print line, isVertices

fig = plt.figure()
plt_ax  = fig.add_subplot(111)
bellman = BellmanFord.BellmanFord(mygraph)
mst_edges = mst_edges = [edge for edge in bellman.edge_to if edge is not None]

# Display vertices
minX = minY =  1e1000
maxX = maxY = -1e1000
for iV in range (0, mygraph.vCount()):
    x = mygraph.vX(iV)
    y = mygraph.vY(iV)
    plt_ax.plot(x,y,'wo', ms = 15)
    minX = min(minX,x)
    minY = min(minY,y)
    maxX = max(maxX,x)
    maxY = max(maxY,y)
    plt_ax.text(x, y, mygraph.vName(iV), ha = 'center', va = 'center')
padX = .10*(maxX-minX)+10
padY = .10*(maxY-minY)+10
plt_ax.axis([minX-padX, maxX+padX, minY-padY, maxY+padY])

# Display edges
for iE in range (0, mygraph.eCount()):
    x0 = mygraph.eV0X(iE)
    y0 = mygraph.eV0Y(iE)
    x1 = mygraph.eV1X(iE)
    y1 = mygraph.eV1Y(iE)
    plotEdge(plt_ax, x0, y0, x1, y1, mygraph.eWght(iE), '0.9')

for iTE in mst_edges:
    x0 = mygraph.eVX(iTE[0])
    y0 = mygraph.eVY(iTE[0])
    x1 = mygraph.eVX(iTE[1])
    y1 = mygraph.eVY(iTE[1])
    plt.plot([x0,x1],[y0,y1],'r--')

plt.show()
