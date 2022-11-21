import pygame as pg 
pg.init()

win = pg.display.set_mode((1000,1000))
pg.display.set_caption("b_curve")

f = pg.font.get_fonts()[0]
font  = pg.font.SysFont(f,32)
White = (255,255,255)

point0 = font.render("P0",True,White)
point1 = font.render("P1",True,White)
point2 = font.render("P2",True,White)
point3 = font.render("P3",True,White)

rect0 = point0.get_rect()
rect1 = point1.get_rect()
rect2 = point2.get_rect()
rect3 = point3.get_rect()

p0 = (100,500)
p1 = (100,100)
p2 = (500,100)
p3 = (500,500)

run = True
speed = .0004
t = 0

while run:
    win.fill((0,0,0))
    pg.time.delay(500)

    for event in pg.event.get():
        if(event.type == pg.QUIT):
            run = False
    while(t<1):
        t += speed
        bz0 = (pow(1-t,3)*p0[0],pow(1-t,3)*p0[1])
        bz1 = (pow(1-t,2)*3*t*p1[0],pow(1-t,2)*3*t*p1[1])
        bz2 = ((1-t)*3*t*t*p2[0],(1-t)*3*t*t*p2[1])
        bz3 = (pow(t,3)*p3[0],pow(t,3)*p3[1])

        p = (bz0[0]+bz1[0]+bz2[0]+bz3[0],bz0[1]+bz1[1]+bz2[1]+bz3[1])
        x,y = round(p[0]),round(p[1])

        rect0.center = p0
        rect1.center = p1
        rect2.center = p2
        rect3.center = p3

        win.blit(point0,rect0)
        win.blit(point1,rect1)
        win.blit(point2,rect2)
        win.blit(point3,rect3)

        pg.draw.line(win,(0,0,255),p0,p1,2)
        pg.draw.line(win,(0,0,255),p2,p3,2)
        pg.draw.circle(win,(0,255,0),(x,y),2)
        pg.display.update()
pg.quit()



pg.quit()