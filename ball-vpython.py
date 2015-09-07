from visual import *
from visual.graph import *
win=500
scene = display(width=win, height=win)
pelota = sphere(pos=(-6,0,0),radius=0.8,color=color.green)

wallR = box(pos=(6,0,0),size=(0.1,12,12),color=color.red)
wallL = box(pos=(-6,0,0),size=(0.1,12,12),color=color.red)
wallT = box(pos=(0,6,-0.1),size=(12,0.1,12),color=color.red)
wallB = box(pos=(0,-6,0.1),size=(12,0.1,12),color=color.red)


pelota.velocity = vector(15,1,2)
deltat = 0.005
t = 0

vscale = 0.2
velocity_arr = arrow(pos=pelota.pos, axis=vscale*(pelota.velocity), color=color.yellow)
pelota.trail = curve(color=pelota.color) 

while t < 4:
    rate(90)
    if(pelota.pos.x > wallR.pos.x):
        pelota.velocity.x = -pelota.velocity.x
        velocity_arr.axis = -velocity_arr.axis
    if(pelota.pos.x < wallL.pos.x):
        pelota.velocity.x = -pelota.velocity.x
        velocity_arr.axis = -velocity_arr.axis

    pelota.pos.x = pelota.pos.x + pelota.velocity.x * deltat
    velocity_arr.pos.x = velocity_arr.pos.x + pelota.velocity.x * deltat
    pelota.trail.append(pos=pelota.pos)
                        
 
    t = t + deltat
    
    
