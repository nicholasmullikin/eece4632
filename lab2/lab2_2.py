import math
# Draw a circle
# Screen resolution is 128x32
def draw_half_circle(cx,cy, r):
    for i in range (0, 180):
        x = cx + r * math.cos(i*math.pi/180)
        if x > 127:
            x = 127
        if x < 0:
            x = 0
        y = cy + r * math.sin(i*math.pi/180)
        if y > 31:
            y = 31
        if y < 0:
            y = 0
        pmod_oled.draw_line(int(x),int(y),int(x+1),int(y))


pmod_oled.clear()
pmod_oled.write('Nicholas\nMullikin')

# head
draw_circle(100,16,16)
# eye 1
draw_circle(94,8,2)
# eye 2
draw_circle(105,8,2)
# smile curve
draw_half_circle(100, 17, 10)
# smile top
pmod_oled.draw_line(90,17,110,17)
# nose 1
pmod_oled.draw_line(100,12,95,15)
# nose 2
pmod_oled.draw_line(100,15,95,15)
