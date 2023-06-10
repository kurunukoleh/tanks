import pygame
import time
import random

class tank :
    def __init__(self, x, y, color, w, h, filename ):
        self.x = x
        self.y = y
        self.color = color
        self.w = w
        self.h = h
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (w*1.2 , h*1.2 ))

    def render(self, screen):
        #pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, [self.rect.x, self.rect.y])

class tnt :
    def __init__(self, x, y, color, w, h, filename ):
        self.x = x
        self.y = y
        self.color = color
        self.w = w
        self.h = h
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (w , h ))

    def render(self, screen):
        #pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, [self.rect.x, self.rect.y])


class bribr :
    def __init__(self, x, y, color, w, h, filename ):
        self.x = x
        self.y = y
        self.color = color
        self.w = w
        self.h = h
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (w , h ))

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, [self.rect.x, self.rect.y])


class boom :
    def __init__(self, x, y, color, w, h, filename ):
        self.x = x
        self.y = y
        self.color = color
        self.w = w
        self.h = h
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (w , h ))

    def render(self, screen):
        #pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, [self.rect.x, self.rect.y])


pygame.init()
screen =pygame.display.set_mode((640 , 640))
fps =pygame.time.Clock()
tsp = 3
speed = 0
kut = 3
badsco = 0
enp = 0
textor = 0
mshren = 0
textor2 = 0
endlist = []
dimlist = []
tntlist = []
birlist = []
boomlist = []
badtnt = []
lastChanges1 = time.time()
lastChanges2 = time.time()
lastChanges3 = time.time()
lastChanges4 = time.time()
music1 = pygame.mixer.music.load('00567.mp3')
for i in range(5):
    birlist.append(bribr(random.randint(50 , 600) , random.randint(200 , 400) , (0,0,0) ,random.randint(50 , 200) ,random.randint(20 , 100) , "pixelartbir.png" ))
dimlist.append(tank(320 , 500 , (0 , 0 , 0) , 40 , 40 , "pixelarttankup.png" ))
endlist.append(tank(320 , 140 , (0 , 0 , 0) , 40 , 40 , "pixelartenemytankdown.png" ))
winText = pygame.font.Font(None , 72).render("ти виграв", True , (0,255,0))
loseText = pygame.font.Font(None , 72).render("ти програв", True , (255,0,0))
while True :
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                speed = 1
                dimlist.append(tank( dimlist[0].rect.x, dimlist[0].rect.y, (0, 0, 0), 40, 40, "pixelarttankleft.png" ))
                dimlist.pop(0)
                kut = 1
                endlist.append(tank( endlist[0].rect.x, endlist[0].rect.y, (0, 0, 0), 40, 40, "pixelartenemytankright.png" ))
                endlist.pop(0)
                mshren = 1


            if event.key == pygame.K_d:
                speed = 2
                dimlist.append(tank( dimlist[0].rect.x, dimlist[0].rect.y, (0, 0, 0), 40, 40, "pixelarttankright.png" ))
                dimlist.pop(0)
                kut = 2
                endlist.append(
                tank(endlist[0].rect.x, endlist[0].rect.y, (0, 0, 0), 40, 40, "pixelartenemytankleft.png"))
                endlist.pop(0)
                mshren = 2


            if event.key == pygame.K_w:
                speed = 3
                dimlist.append(tank( dimlist[0].rect.x, dimlist[0].rect.y, (0, 0, 0), 40, 40, "pixelarttankup.png" ))
                dimlist.pop(0)
                kut = 3
                endlist.append(
                tank(endlist[0].rect.x, endlist[0].rect.y, (0, 0, 0), 40, 40, "pixelartenemytankdown.png"))
                endlist.pop(0)
                mshren = 3


            if event.key == pygame.K_s:
                speed = 4
                dimlist.append(tank( dimlist[0].rect.x, dimlist[0].rect.y, (0, 0, 0), 40, 40, "pixelarttankdown.png" ))
                dimlist.pop(0)
                kut =4
                endlist.append(
                tank(endlist[0].rect.x, endlist[0].rect.y, (0, 0, 0), 40, 40, "pixelartennemytankup.png"))
                endlist.pop(0)
                mshren = 4


            if event.key == pygame.K_LEFT:
                speed = 1
                dimlist.append(tank( dimlist[0].rect.x, dimlist[0].rect.y, (0, 0, 0), 40, 40, "pixelarttankleft.png" ))
                dimlist.pop(0)
                kut = 1
                endlist.append(
                tank(endlist[0].rect.x, endlist[0].rect.y, (0, 0, 0), 40, 40, "pixelartenemytankright.png"))
                endlist.pop(0)


            if event.key == pygame.K_RIGHT:
                speed = 2
                dimlist.append(tank( dimlist[0].rect.x, dimlist[0].rect.y, (0, 0, 0), 40, 40, "pixelarttankright.png" ))
                dimlist.pop(0)
                kut = 2
                endlist.append(
                tank(endlist[0].rect.x, endlist[0].rect.y, (0, 0, 0), 40, 40, "pixelartenemytankleft.png"))
                endlist.pop(0)

            if event.key == pygame.K_UP:
                speed = 3
                dimlist.append(tank(dimlist[0].rect.x, dimlist[0].rect.y, (0, 0, 0), 40, 40, "pixelarttankup.png" ))
                dimlist.pop(0)
                kut = 3
                endlist.append(
                tank(endlist[0].rect.x, endlist[0].rect.y, (0, 0, 0), 40, 40, "pixelartenemytankdown.png"))
                endlist.pop(0)

            if event.key == pygame.K_DOWN:
                speed = 4
                dimlist.append(tank(dimlist[0].rect.x, dimlist[0].rect.y, (0, 0, 0), 40, 40, "pixelarttankdown.png" ))
                dimlist.pop(0)
                kut = 4
                endlist.append(
                tank(endlist[0].rect.x, endlist[0].rect.y, (0, 0, 0), 40, 40, "pixelartennemytankup.png"))
                endlist.pop(0)

            if event.key == pygame.K_SPACE:
                if time.time() - lastChanges1 > 3:
                    lastChanges1 = time.time()
                    pygame.mixer.music.play(- 1, 0, 3)
                    if kut == 1 :
                        tntlist.append(tnt(dimlist[0].rect.x - 15 , dimlist[0].rect.y ,(0 ,0 , 0) , 10 , 10 , "pixelarttnt1.png" ))
                        badsco = 1

                    if kut == 2 :
                        tntlist.append(tnt(dimlist[0].rect.x + 15 , dimlist[0].rect.y, (0, 0, 0), 10, 10, "pixelarttnt1.png"))
                        badsco = 2

                    if kut == 3 :
                        tntlist.append(tnt(dimlist[0].rect.x + 15, dimlist[0].rect.y - 15 , (0, 0, 0), 10, 10, "pixelarttnt1.png"))
                        badsco = 3

                    if kut == 4 :
                        tntlist.append(tnt(dimlist[0].rect.x + 15, dimlist[0].rect.y + 15 , (0, 0, 0), 10, 10, "pixelarttnt1.png"))
                        badsco = 4


        if event.type == pygame.KEYUP:
            speed = 0
            mshren = 0

    if speed == 1 :
        dimlist[0].rect.x -= 1
    if speed == 2 :
        dimlist[0].rect.x += 1

    if speed == 3 :
        dimlist[0].rect.y -= 1

    if speed == 4 :
        dimlist[0].rect.y += 1

    if badsco == 1 :
        for i in range(len(tntlist)):
            tntlist[i].rect.x -= tsp

    if badsco == 2 :
        for i in range(len(tntlist)):
            tntlist[i].rect.x += tsp

    if badsco == 3 :
        for i in range(len(tntlist)):
            tntlist[i].rect.y -= tsp

    if badsco == 4 :
        for i in range(len(tntlist)):
            tntlist[i].rect.y += tsp

    if kut == 1 :
        endlist[0].rect.x += 1
    if kut == 2 :
        endlist[0].rect.x -= 1
    if kut == 3 :
        endlist[0].rect.y += 1
    if kut == 4 :
        endlist[0].rect.y -= 1

    if time.time() - lastChanges4 > 2 :
        lastChanges4 = time.time()
        if kut == 1 :
            enp = 2
            badtnt.append(tnt(endlist[0].rect.x - 15, endlist[0].rect.y, (0, 0, 0), 10, 10, "pixelarttnt2.png"))
        if kut == 2 :
            enp = 1
            badtnt.append(tnt(endlist[0].rect.x + 15, endlist[0].rect.y, (0, 0, 0), 10, 10, "pixelarttnt2.png"))
        if kut == 3 :
            enp = 4
            badtnt.append(tnt(endlist[0].rect.x + 15, endlist[0].rect.y - 15, (0, 0, 0), 10, 10, "pixelarttnt2.png"))
            badtnt.pop(0)
        if kut == 4 :
            enp = 3
            badtnt.append(tnt(endlist[0].rect.x + 15, endlist[0].rect.y + 15, (0, 0, 0), 10, 10, "pixelarttnt2.png"))



    if enp == 1 or kut == 0 :
        for i in range(len(badtnt)):
            badtnt[i].rect.x -= 5

    if enp == 2 or kut == 0 :
        for i in range(len(badtnt)):
            badtnt[i].rect.x += 5

    if enp == 3 or kut == 0 :
        for i in range(len(badtnt)):
            badtnt[i].rect.y -= 5

    if enp == 4  or kut == 0 :
        for i in range(len(badtnt)):
            badtnt[i].rect.y += 5



    for i in range(5):
        if dimlist[0].rect.colliderect(birlist[i].rect) :
            speed = 0

    for i in range(5):
        if endlist[0].rect.colliderect(birlist[i].rect) :
            if kut == 1:
                endlist[0].rect.x -= 1
            if kut == 2:
                endlist[0].rect.x += 1
            if kut == 3:
                endlist[0].rect.y -= 1
            if kut == 4:
                endlist[0].rect.y += 1


    if dimlist[0].rect.x > 600 or dimlist[0].rect.x < 0 or dimlist[0].rect.y > 600 or dimlist[0].rect.y < 0  :
        speed = 0

    if endlist[0].rect.x > 600 or endlist[0].rect.x < 0 or endlist[0].rect.y > 600 or endlist[0].rect.y < 0 :
        if kut == 1:
            endlist[0].rect.x -= 1
        if kut == 2:
            endlist[0].rect.x += 1
        if kut == 3:
            endlist[0].rect.y -= 1
        if kut == 4:
            endlist[0].rect.y += 1


    for i in range(5):
        for f in range(len(tntlist)):
            if tntlist[f].rect.colliderect(birlist[i].rect) :
                tntlist.pop(0)

    for i in range(5):
        for f in range(len(badtnt)):
            if badtnt[f].rect.colliderect(birlist[i].rect) :
                badtnt.pop(0)


    for i in range(len(tntlist)):
        if tntlist[i].rect.colliderect(endlist[0].rect):
            endlist.append(boom(endlist[0].rect.x, endlist[0].rect.y, (0, 0, 0), 70, 70, "pixelartboom.png"))
            pygame.mixer.music.play(- 1, 0, 3)
            endlist.pop(0)
            textor = 1

    for i in range(len(badtnt)):
        if badtnt[i].rect.colliderect(dimlist[0].rect):
            dimlist.append(boom(dimlist[0].rect.x, dimlist[0].rect.y, (0, 0, 0), 70, 70, "pixelartboom.png"))
            pygame.mixer.music.play(- 1, 0, 3)
            dimlist.pop(0)
            textor2 = 1


    if textor == 1 :
        screen.blit(winText, [100, 100])
        pygame.display.flip()


    if time.time() - lastChanges2  > 2 :
        lastChanges2 = time.time()
        tsp = 3

    bacground = pygame.image.load("pikselartback.png")
    bacground = pygame.transform.scale(bacground, (640, 640))
    screen.fill((0, 0, 255))
    screen.blit(bacground, [0, 0])
    for i in range(5):
        birlist[i].render(screen)
    dimlist[0].render(screen)
    endlist[0].render(screen)
    if len(tntlist) > 0 :
        for i in range(len(tntlist)):
            tntlist[i].render(screen)
    if len(badtnt) > 0 :
        for i in range(len(badtnt)):
            badtnt[i].render(screen)

    if textor == 1 :
        screen.blit(winText , [ 200 , 320])

    if textor2 == 1 :
        screen.blit(loseText , [ 200 , 320])

    pygame.display.flip()

    if textor == 1 :
        time.sleep(1000)

    if textor2 == 1 :
        time.sleep(1000)

    fps.tick(60)