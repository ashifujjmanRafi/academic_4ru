import pygame
pygame.init()

win  = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("b_curve")

f = pygame.font.get_fonts()[1]
font = pygame.font.SysFont(f,32)
WHITE=(255,255,255)

point0 = font.render("p0",True,WHITE)
point1 = font.render("p1",True,WHITE)
point2 = font.render("p3",True,WHITE)
point3 = font.render("p4",True,WHITE)

rect0 = point0.get_rect()
rect1 = point1.get_rect()
rect2 = point2.get_rect()
rect3 = point3.get_rect()

p0 = (100.0 , 500.0)
p1 = (200.0 , 100.0)
p2 = (600.0 , 80.0)
p3 = (650.0 , 410.0)

run = True
speed = .004
t=0
while run:
    win.fill((0,0,0))
    pygame.time.delay(100)

    for event in pygame.event.get():
        print(event)
        if(event.type==pygame.QUIT):
            run = False
    while(t<1):
        t+=speed

        bz0 = (pow(1-t,3)*p0[0],pow(1-t,3)*p0[1])
        bz1 = (pow(1-t,2)*3*t*p1[0],pow(1-t,2)*3*t*p1[1])
        bz2 = ((1-t)*t*t*3*p2[0],(1-t)*t*t*3*p2[1])
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

        pygame.draw.line(win,(0,255,0),p0,p1,1)
        pygame.draw.line(win,(0,255,0),p2,p3,1)

        pygame.draw.circle(win,(255,0,0),(x,y),2)
        pygame.display.update()


pygame.quit()