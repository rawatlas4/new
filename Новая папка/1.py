import pygame

pygame.init()
win_width = 1200
win_height = 700
window = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()
with open("2","r",) as file:
    level1 = file.readlines()
class Pryamokytnuk():
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rec = pygame.Rect(self.x,self.y,self.width,self.height)
    def risovka(self):
        pygame.draw.rect(window,self.color,self.rec)
class Ball():
    def __init__(self,x,y,color,radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed_x = 10
        self.speed_y = 10
    def risovka(self):
        pygame.draw.circle(window,self.color,(self.x,self.y),self.radius)
    def dvizhenie(self):
        self.x+=self.speed_x
        self.y+=self.speed_y
        if self.y > 699:
            self.speed_y*=-1
        if self.x > 1199:
            self.speed_x*=-1
        if self.y < 0:
            self.speed_y*=-1
        if self.x < 0:
            self.speed_x*=-1
a = []
for row,line in enumerate(level1):
    for index,char in enumerate(line):
        if char == '#':
            pygame.draw.rect(window,(255,0,0),(index*100,500,70,50))
            block1 = Pryamokytnuk(index*100,row*100,52,25,(52,78,124))
            a.append(block1)


ball = Ball(10,200,(0,0,255),10)
enemy = Ball(650,310,(0,255,0),35)
game = 1
while game:
    window.fill((0,0,0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = 0
    ball.risovka()
    ball.dvizhenie()
    enemy.risovka()
    enemy.dvizhenie()
    pygame.draw.line(window,(255,255,0),(0,0),(0,700),10)
    pygame.draw.line(window,(0,255,255),(0,690),(1200,700),10)
    pygame.draw.line(window,(0,255,0),(1199,699),(1199,0),10)
    pygame.draw.line(window,(0,255,0),(1199,0),(0,0),10)

    for i in a:
        i.risovka()

    pygame.display.update()
    clock.tick(60)
