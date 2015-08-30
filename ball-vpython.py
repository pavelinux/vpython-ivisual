from visual import *

pelota = sphere(pos=(-6,0,0),radius=0.8,color=color.green)

wallR = box(pos=(6,0,0),size=(0.1,12,12),color=color.red)
wallL = box(pos=(-6,0,0),size=(0.1,12,12),color=color.red)
#wallT = box(pos=(0,6,-0.1),size=(12,0.1,12),color=color.red)
#wallB = box(pos=(0,-6,0.1),size=(12,0.1,12),color=color.red)


pelota.velocity = vector(15,0,0)
deltat = 0.005
t = 0

vscale = 0.2
velocity_arr = arrow(pos=pelota.pos, axis=vscale*(pelota.velocity), color=color.yellow)


while t < 4:
    rate(90)
    if(pelota.pos.x > wallR.pos.x):
        pelota.velocity.x = -pelota.velocity.x
        velocity_arr.axis.x = -velocity_arr.axis.x
    if(pelota.pos.x < wallL.pos.x):
        pelota.velocity.x = -pelota.velocity.x
        velocity_arr.axis.x = -velocity_arr.axis.x

    pelota.pos.x = pelota.pos.x + pelota.velocity.x * deltat
    velocity_arr.pos.x = velocity_arr.pos.x + pelota.velocity.x * deltat
 
    t = t + deltat
    
    
