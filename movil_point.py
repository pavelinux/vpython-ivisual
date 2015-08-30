from visual import *

radio_esfera = 0.5

esfera1 = sphere(pos=vector(0,0,0),radius=radio_esfera,color=color.yellow)
esfera2 = sphere(pos=vector(-3,4,0),radius=radio_esfera,color=color.yellow)

flecha = arrow(pos=vector(0,0,0),axis=esfera2.pos - esfera1.pos, color=color.red)

r = vector(-3,4,0)

while r.x < 10:
    rate(5)
    esfera2.pos = r
    flecha.axis = r
    
    r.x += 1
