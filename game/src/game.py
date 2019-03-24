import pygame
pygame.init()

screenres_w = 800
screenres_h = 600
win = pygame.display.set_mode((screenres_w, screenres_h))

pygame.display.set_caption("1v1Me")

x = 50
y = 450
width = 30
height = 45
vel = 10
is_jump = False
jump_count = 10
run = True

while run:
    pygame.time.delay(33)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenres_w - width - vel:
        x += vel
    if not (is_jump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < screenres_h - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count**2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
pygame.quit()
