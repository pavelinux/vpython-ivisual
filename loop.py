from visual import *

i = 0

while i < 2:
    radius_ball = 0.5
    redballi  = sphere(pos=vector(i,0,0),size=(1,1,1),radius=radius_ball,color=color.red)
    blueballj = sphere(pos=vector(0,i,0),size=(1,1,1),radius=radius_ball,color=color.blue)
    
    i+=1
