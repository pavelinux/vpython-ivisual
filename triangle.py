from visual import *

scene.autoscale=1
#scene.width=800
#scene.height=600

flecha_scale=0.5
pelota_radio = 0.4

pelota1 = sphere(pos=vector(-sqrt(2),0,0),radius=pelota_radio, color=color.cyan)
flecha1 = arrow(pos=pelota1.pos, axis=flecha_scale*vector(0,-2,0),color=color.red)

pelota2 = sphere(pos=vector(0,1,0),radius=pelota_radio, color=color.yellow)
flecha2 = arrow(pos=pelota2.pos, axis=flecha_scale*vector(-2,0,0),color=color.red)

pelota3 = sphere(pos=vector(0,-1,0),radius=pelota_radio, color=color.green)
flecha3 = arrow(pos=pelota3.pos, axis=flecha_scale*vector(2,sqrt(2),0),color=color.red)
