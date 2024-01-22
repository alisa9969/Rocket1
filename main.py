import pygame
import random


class Button:
    def __init__(self, x, y, w, h, color, text=''):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.text = text

    def draw(self, fontt):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
        if self.text != '':
            font = pygame.font.SysFont('freemono', fontt)
            text = font.render(self.text, 1, '#0b0212')
            screen.blit(text,
                        (self.x + (self.w / 2 - text.get_width() / 2), self.y + (self.h / 2 - text.get_height() / 2)))


ends = 0
tm = 0
random_x = []
random_y = []

for _ in range(150):
    random_x.append(random.random() * 850)
    random_y.append(random.random() * 650)


def draw(screen):
    global random_x, random_y, tm
    screen.fill('#040008')
    if tm % 25 == 0:
        random_x, random_y = [], []
        for j in range(150):
            random_x.append(random.random() * 850)
            random_y.append(random.random() * 650)
    for i in range(150):
        screen.fill(pygame.Color('white'), (int(random_x[i]), int(random_y[i]), 1, 1))


last_rand = []


class Asteroids(pygame.sprite.Sprite):
    asteroids = [pygame.image.load('aster.png'),
                 pygame.image.load('nlo.png'), pygame.image.load('cometa.png'), pygame.image.load('star.png')]

    def __init__(self, im):
        super().__init__()
        global last_rand
        image = im
        rx = random.randrange(90, 700)
        while rx - self.asteroids[image].get_size()[0] in last_rand:
            rx = random.randrange(90, 700)
        sz = self.asteroids[image].get_size()[0]
        last_rand = [i for i in range(rx, sz)]
        self.rect = self.asteroids[image].get_rect(center=(rx, -100))

    def move(self, v):
        self.rect.y += v


def restart():
    global flag, asteroid4, asteroid, asteroid2, asteroid3, sprite1, flyevent, flyevent2, flyevent3, flyevent4
    flag = 0
    pygame.time.set_timer(flyevent, 0)
    pygame.time.set_timer(flyevent2, 0)
    pygame.time.set_timer(flyevent3, 0)
    pygame.time.set_timer(flyevent4, 0)
    asteroid3 = pygame.sprite.Group()
    asteroid2 = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    asteroid4 = pygame.sprite.Group()
    sprite1.rect.x = 370


if __name__ == '__main__':
    pygame.init()
    x = 1
    size = width, height = 850, 650
    rec1 = open('record.txt').readlines()
    rec = int(rec1[0])
    screen = pygame.display.set_mode(size)
    screen.fill('#040008')
    flyevent = pygame.USEREVENT + 1
    flyevent3 = pygame.USEREVENT + 2
    flyevent2 = pygame.USEREVENT + 3
    flyevent4 = pygame.USEREVENT + 4
    MYEVENTTYPE = pygame.USEREVENT
    pygame.time.set_timer(MYEVENTTYPE, 10)
    draw(screen)
    running = True
    sp = pygame.sprite.Group()
    sprite1 = pygame.sprite.Sprite()
    sprite1.image = pygame.image.load('rocet1.png')
    sprite1.rect = sprite1.image.get_rect()
    sprite1.rect.x = 370
    sprite1.rect.y = 370
    sp.add(sprite1)

    sprite2 = pygame.sprite.Sprite()
    sprite2.image = pygame.image.load('left.png')
    sprite2.rect = sprite2.image.get_rect()
    sprite2.rect.x = 270
    sprite2.rect.y = 560
    sp.add(sprite2)

    sprite3 = pygame.sprite.Sprite()
    sprite3.image = pygame.image.load('again.png')
    sprite3.rect = sprite3.image.get_rect()
    sprite3.rect.x = 20
    sprite3.rect.y = 80
    sp.add(sprite3)

    sprite4 = pygame.sprite.Sprite()
    sprite4.image = pygame.image.load('right.png')
    sprite4.rect = sprite4.image.get_rect()
    sprite4.rect.x = 450
    sprite4.rect.y = 560
    sp.add(sprite4)

    sprite5 = pygame.sprite.Sprite()
    sprite5.image = pygame.image.load('pause.png')
    sprite5.rect = sprite5.image.get_rect()
    sprite5.rect.x = 400
    sprite5.rect.y = 580
    sp.add(sprite5)
    sp2 = pygame.sprite.Group()
    sprite6 = pygame.sprite.Sprite()
    sprite6.image = pygame.image.load('star.png')
    sprite6.rect = sprite5.image.get_rect()
    sprite6.rect.x = 730
    sprite6.rect.y = 25
    sp2.add(sprite6)

    flag = 0
    e = 0
    f = pygame.font.SysFont('freemono', 19)
    t = f.render(f'Record: {rec} km', 1, '#f5e8ff')
    t2 = f.render(f'{e} km', 1, '#f5e8ff')
    screen.blit(t, (20, 20))
    clock = pygame.time.Clock()
    pygame.display.flip()
    img_index = 0
    asteroid3 = pygame.sprite.Group()
    asteroid2 = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    asteroid4 = pygame.sprite.Group()
    pygame.time.set_timer(flyevent, 3000)
    pygame.time.set_timer(flyevent2, 5000)
    pygame.time.set_timer(flyevent4, 4500)
    pause = 0
    spr = Asteroids(0)
    lose = 0
    pygame.time.set_timer(flyevent3, 7000)
    spr2 = Asteroids(1)
    spr3 = Asteroids(2)
    loseevent = pygame.USEREVENT + 5
    stars = int(rec1[1])
    while running:
        font = pygame.font.SysFont('freemono', 20, bold=True)
        text3 = font.render(f'{stars}', 1, '#ffffff')
        screen.blit(text3, (770, 30))
        collide = pygame.sprite.spritecollideany(sprite1, asteroid)
        collide2 = pygame.sprite.spritecollideany(sprite1, asteroid2)
        collide3 = pygame.sprite.spritecollideany(sprite1, asteroid3)
        if (collide or collide2 or collide3) and flag:
            pygame.time.set_timer(loseevent, 10)
        if pygame.sprite.spritecollide(sprite1, asteroid4, True):
            stars += 1
        img_index += 1
        sprite1.rect.x += 1
        if img_index == 4:
            sprite1.rect.x -= 4
            img_index = 0
        tm += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and flag == 0:
            flag = 1
        if (flag or (not flag and e != 0)) and pause == 0:
            if keys[pygame.K_LEFT] and sprite1.rect.x >= 0:
                sprite1.rect.x -= 2
            elif keys[pygame.K_RIGHT] and sprite1.rect.x <= 760:
                sprite1.rect.x += 2
            if flag == 0:
                pygame.time.set_timer(flyevent, 3000)
                pygame.time.set_timer(flyevent2, 5000)
                pygame.time.set_timer(flyevent3, 7000)
                pygame.time.set_timer(flyevent4, 2000)
                flag = 1
                e = 0
            e += 1
            if e % 20 == 0:
                t2 = f.render(f'{e // 20} km', 1, '#f5e8ff')
            if e // 20 >= rec:
                rec = e // 20
                t = f.render(f'Record: {rec} km', 1, '#f5e8ff')
        pygame.event.pump()
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == loseevent:
                pygame.time.set_timer(loseevent, 0)
                lose = 1
                while lose:
                    draw(screen)
                    screen.blit(t, (20, 20))
                    screen.blit(t2, (20, 50))
                    font = pygame.font.SysFont('freemono', 80, bold=True)
                    text = font.render('You lose!', 1, '#f0e3fa')
                    screen.blit(text, (200, 200))
                    Button(275, 300, 280, 50, '#958e9c', 'Restart').draw(35)
                    Button(275, 370, 280, 50, '#958e9c', 'Home').draw(35)
                    pygame.event.pump()
                    clock.tick(120)
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if 275 <= event.pos[0] <= 555 and 300 <= event.pos[1] <= 350:
                                lose = 0
                                restart()
                            if 275 <= event.pos[0] <= 555 and 370 <= event.pos[1] <= 420:
                                e, lose = 0, 0
                                restart()
                        if event.type == pygame.QUIT:
                            lose = 0
                            running = 0
                    screen.blit(text3, (770, 30))
                    sp2.draw(screen)
                    pygame.display.flip()
            if event.type == pygame.QUIT:
                running = False
            if flag or (not flag and e != 0):
                if event.type == flyevent:
                    spr = Asteroids(0)
                    spr.image = Asteroids.asteroids[0]
                    asteroid.add(spr)
                if event.type == flyevent4:
                    spr4 = Asteroids(3)
                    spr4.image = Asteroids.asteroids[3]
                    asteroid4.add(spr4)
                if event.type == flyevent2:
                    spr2 = Asteroids(1)
                    spr2.image = Asteroids.asteroids[1]
                    asteroid2.add(spr2)
                if event.type == flyevent3:
                    spr3 = Asteroids(2)
                    spr3.image = Asteroids.asteroids[2]
                    asteroid3.add(spr3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if flag or (not flag and e != 0):
                    if (280 <= event.pos[0] <= 350 and 575 <= event.pos[1] <= 600) or (
                            275 <= event.pos[0] <= 300 and 565 <= event.pos[1] <= 610) and not pause:
                        sprite1.rect.x -= 10
                        pygame.display.flip()
                    if (468 <= event.pos[0] <= 530 and 575 <= event.pos[1] <= 600) or (
                            517 <= event.pos[0] <= 545 and 565 <= event.pos[1] <= 610) and not pause:
                        sprite1.rect.x += 10
                        pygame.display.flip()
                    if 20 <= event.pos[0] <= 45 and 80 <= event.pos[1] <= 105:
                        restart()
                    if 400 <= event.pos[0] <= 425 and 582 <= event.pos[1] <= 604 and pause == 0:
                        pause = 1
                        while pause:
                            Button(225, 200, 400, 100, '#f0e3fa', 'Pause').draw(80)
                            Button(275, 350, 280, 50, '#958e9c', 'Restart').draw(35)
                            Button(275, 420, 280, 50, '#958e9c', 'Home').draw(35)
                            pygame.event.pump()
                            clock.tick(120)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if (400 <= event.pos[0] <= 425 and 582 <= event.pos[1] <= 604) or (
                                            225 <= event.pos[0] <= 625 and 200 <= event.pos[1] <= 300):
                                        pause = 0
                                    if 275 <= event.pos[0] <= 555 and 350 <= event.pos[1] <= 400:
                                        pause = 0
                                        restart()
                                    if 275 <= event.pos[0] <= 555 and 420 <= event.pos[1] <= 470:
                                        flag, e = 0, 0
                                        pause = 0
                                if event.type == pygame.QUIT:
                                    pause, running = 0, 0
                            pygame.display.flip()
                else:
                    if 220 <= event.pos[0] <= 390 + 220 and 170 <= event.pos[1] <= 110 + 170:
                        flag = 1
            if event.type == MYEVENTTYPE:
                draw(screen)
                screen.blit(t, (20, 20))
                screen.blit(t2, (20, 50))
                if flag or (not flag and e != 0):
                    sp.draw(screen)
                elif not flag and e == 0:
                    Button(220, 170, 390, 110, '#f0e3fa', 'Start').draw(80)
        if flag:
            for ast in asteroid:
                ast.move(1)
            for ast4 in asteroid4:
                ast4.move(1)
            for ast2 in asteroid2:
                ast2.move(1.5)
            for ast3 in asteroid3:
                ast3.move(2)
            draw(screen)
            screen.blit(t, (20, 20))
        if not flag and e == 0:
            draw(screen)
            screen.blit(t, (20, 20))
            Button(220, 170, 390, 110, '#f0e3fa', 'Start').draw(80)
        if flag:
            asteroid.draw(screen)
            asteroid2.draw(screen)
            asteroid3.draw(screen)
            asteroid4.draw(screen)
            screen.blit(t2, (20, 50))
            sp.draw(screen)
            screen.blit(t, (20, 20))
        screen.blit(text3, (770, 30))
        sp2.draw(screen)
        pygame.display.flip()

file = open("record.txt", 'w')
file.write(str(rec) + '\n' + str(stars))
pygame.quit()
