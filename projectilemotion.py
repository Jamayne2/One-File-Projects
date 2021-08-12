import pygame
import math

wScreen = 1200
hScreen = 500

win = pygame.display.set_mode((wScreen ,hScreen))

class Ball(object):
    def __init__(self ,x ,y ,radius , color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    def draw(self , win):
        pygame.draw.circle(win , (0  , 0 ,0) , (self.x , self.y) , self.radius)
        pygame.draw.circle(win , self.color , (self.x , self.y) , self.radius-1)
    
    @staticmethod
    def ballPath(startx , starty , power , ang ,time):
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distX = velx * time
        distY = (vely * time) + ((-4.9*(time)**2)/2) # s = ut + 1/2at^2

        newx = round(distX + startx)
        newy = round(starty - distY)

        return(newx ,newy)


def redrawWindow():
    win.fill((64 , 64 , 64))
    ball1.draw(win)
    pygame.draw.line(win , (255 ,255 ,255) , line[0] , line[1])

    pygame.display.update()

def findAngle(pos):
    sX = ball1.x
    sY = ball1.y
    try:
        angle = math.atan((sY-pos[1])/(sX-pos[0]))
    except:
        angle = math.pi/2
    
    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = (math.pi*2) - angle
    
    return angle

ball1 = Ball(300 , 494 ,5,(255 ,255 ,255))

x = 0
y = 0
time = 0
power = 0
angle = 0
shoot = False
run = True
while run:

    if shoot:
        if ball1.y < 500-ball1.radius:
            time += 0.01
            pos2 = ball1.ballPath(x , y ,power , angle , time)
            ball1.x = pos2[0]
            ball1.y = pos2[1]
            
        else:
            shoot = False
            ball1.y = 494
    pos = pygame.mouse.get_pos()
    line = [(ball1.x , ball1.y),  pos]
    redrawWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if shoot == False:
                shoot = True
                x = ball1.x
                y = ball1.y
                time = 0
                power = math.sqrt((line[1][1] - line[0][1])**2 + ((line[1][0] - line[0][0])**2))/8#Using Line function --> sqrt(chnage in x **2 + change in y**2)
                angle = findAngle(pos)
pygame.quit()

