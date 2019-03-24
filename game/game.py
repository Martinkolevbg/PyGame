import pygame
import os
pygame.init()
print "hi"

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("First Game")

walkRight = [
    pygame.image.load('game/images/R1.png'),
    pygame.image.load('game/images/R2.png'),
    pygame.image.load('game/images/R3.png'),
    pygame.image.load('game/images/R4.png'),
    pygame.image.load('game/images/R5.png'),
    pygame.image.load('game/images/R6.png'),
    pygame.image.load('game/images/R7.png'),
    pygame.image.load('game/images/R8.png'),
    pygame.image.load('game/images/R9.png')
]
walkLeft = [
    pygame.image.load('game/images/L1.png'),
    pygame.image.load('game/images/L2.png'),
    pygame.image.load('game/images/L3.png'),
    pygame.image.load('game/images/L4.png'),
    pygame.image.load('game/images/L5.png'),
    pygame.image.load('game/images/L6.png'),
    pygame.image.load('game/images/L7.png'),
    pygame.image.load('game/images/L8.png'),
    pygame.image.load('game/images/L9.png')
]
bg = pygame.image.load('game/images/bg.jpg')
char = pygame.image.load('game/images/standing.png')

clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)

    pygame.display.update()


#mainloop
man = player(200, 410, 64, 64)
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.right = False
        man.left = False
        man.walkCount = 0

    if not (man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount**2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()