from visual import *

scene.autoscale=1

flecha_scale=1.0
pelota_radio = 0.4

pelota1 = sphere(pos=vector(-1,0,0),radius=pelota_radio, color=color.cyan)


pelota2 = sphere(pos=vector(1,1,0),radius=pelota_radio, color=color.yellow)


pelota3 = sphere(pos=vector(1,-1,0),radius=pelota_radio, color=color.green)


flecha1 = arrow(pos=pelota1.pos, axis=flecha_scale*(pelota2.pos-pelota1.pos),color=color.red)
flecha2 = arrow(pos=pelota2.pos, axis=flecha_scale*(pelota3.pos-pelota2.pos),color=color.red)
flecha3 = arrow(pos=pelota3.pos, axis=flecha_scale*(pelota1.pos-pelota3.pos),color=color.red)
