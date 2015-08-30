from visual import *

#cilindro = cylinder(pos=(0,1,-1), axis=(5,0,0),color=color.orange)
from visual.graph import *
#from numpy import cos, pi, exp,arange

funct = gcurve(color=color.yellow)
for x in arange(0.0, 8.1, 0.1):
    funct.plot(pos=(x,3.0*cos(2*x)*exp(-0.2*x)))
