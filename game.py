import pygame ; import random ; import sys
pygame.init() 
from pygame import *
import os

def r(relative_path):
    """ Get the correct path for bundled files. """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

fps = 95 ; clock = pygame.time.Clock()
screen = display.set_mode((500,480),pygame.NOFRAME)
display.set_caption("FLAPPY BIRD")
display.set_icon(pygame.image.load(r("assets/ico.png")))

#images and sprites
nums = [
        
        image.load(r("assets/sprites/0.png")).convert_alpha(),
        image.load(r("assets/sprites/1.png")).convert_alpha(),
        image.load(r("assets/sprites/2.png")).convert_alpha(),
        image.load(r("assets/sprites/3.png")).convert_alpha(),
        image.load(r("assets/sprites/4.png")).convert_alpha(),
        image.load(r("assets/sprites/5.png")).convert_alpha(),
        image.load(r("assets/sprites/6.png")).convert_alpha(),
        image.load(r("assets/sprites/7.png")).convert_alpha(),
        image.load(r("assets/sprites/8.png")).convert_alpha(),
        image.load(r("assets/sprites/9.png")).convert_alpha(),
        
        ]

quit = pygame.transform.scale(pygame.image.load(r("assets/sprites/button0.png")).convert_alpha(),(40,40))
pause = pygame.transform.scale(pygame.image.load(r("assets/sprites/pause button.png")).convert_alpha(),(40,40))
bg = pygame.image.load(r("assets/sprites/bg.png")).convert_alpha()
title = pygame.transform.scale(pygame.image.load(r("assets/sprites/start.png")).convert_alpha(),(368,534))
ground = pygame.image.load(r("assets/sprites/base.png"))
pipe_up = pygame.transform.scale(pygame.image.load(r("assets/sprites/pipe.png")).convert_alpha(),(96,786))

over = pygame.transform.scale(pygame.image.load(r("assets/sprites/over.png")).convert_alpha(),(384,84))
start = pygame.transform.scale(pygame.image.load(r("assets/sprites/button1.png")).convert_alpha(),(96,96))
exit = pygame.transform.scale(pygame.image.load(r("assets/sprites/exit.png")).convert_alpha(),(96,96))
button = transform.scale(image.load(r("assets/sprites/begin.png")),(96,96))

#sounds
swoosh = mixer.Sound(r("assets/sfx/swoosh.wav"))
#more sounds are loaded at the time of playing

#animating the bird flap
duration = 5
index = 0
counter = 0
velocity = 0
sprites = [pygame.transform.scale(pygame.image.load(r("assets/sprites/bird1.png")).convert_alpha(),(34*1.5,24*1.5)),
pygame.transform.scale(pygame.image.load(r("assets/sprites/bird2.png")).convert_alpha(),(34*1.5,24*1.5)),
pygame.transform.scale(pygame.image.load(r("assets/sprites/bird3.png")).convert_alpha(),(34*1.5,24*1.5))]
    

def game():
    global bird_y,velocity
    global pipe_y1,pipe_y2,pipe_y3
    global pipe_x1,pipe_x2,pipe_x3
    global x1,x2,x3,x4,x5,pipe_x1
    global dead ,score_list_index
    dead = False

    bird_y = 80
    x1 = 0 ; x2 = 500
    x4 = 0 ; x5 = 500

    pipe_x1 = 300 ; pipe_y1 = random.randint(-250,-60)
    pipe_x2 = pipe_x1 + 96 + 150 ; pipe_y2 = random.randint(-250,-60)
    pipe_x3 = pipe_x2 + 96 + 150 ; pipe_y3 = random.randint(-250,-60)

    score_list_index = 0
    def animate():
    
        global bird, counter, index, duration,sprites, velocity,bird_y
        global player_mid, score_list_index, score_timer, score_duration
        

        bird = sprites[index]
        screen.blit(bird,(80,bird_y))
        if pipe_x1+50 <= 90+(34*1.5-12) < pipe_x1 + 52:
            mixer.Sound.play(mixer.Sound(r("assets/sfx/point.ogg")))
            score_list_index+=1
        
        if pipe_x2+50 <= 90+(34*1.5-12) < pipe_x2 + 52:
            mixer.Sound.play(mixer.Sound(r("assets/sfx/point.ogg")))
            score_list_index+=1

        if pipe_x3+50 <= 90+(34*1.5-12) < pipe_x3 + 52:
            mixer.Sound.play(mixer.Sound(r("assets/sfx/point.ogg")))
            score_list_index+=1

        if score_list_index<=9:
            screen.blit(nums[score_list_index],(240,20))
        elif score_list_index > 9 and score_list_index <= 99:
            double_digits = str(score_list_index)
            screen.blit(nums[int(double_digits[0])],(220,20)) ; screen.blit(nums[int(double_digits[1])],(220+24,20))
        elif score_list_index > 99:
            triple_digits = str(score_list_index)
            screen.blit(nums[int(triple_digits[0])],(210,20)) ; screen.blit(nums[int(triple_digits[1])],(210+24,20))
            screen.blit(nums[int(triple_digits[2])],(210+50,20))


        player_mid = bird.get_width()//2 + 80

        if dead == True:
            return
        velocity += 0.10
        if velocity >= 12:
            velocity = 12
        if bird_y+(24*1.5) < 429:
            bird_y += velocity
        else:
            velocity = 0
            bird_y = 429-(24*1.5)
        counter += 1
        if counter > duration:
            counter = 0
            index += 1
            if index >= len(sprites):
                index = 0  

    def scroll():
        if dead == True:
            return
        global pipe_y1,pipe_y2,pipe_y3
        global pipe_x1,pipe_x2,pipe_x3
        global x1,x2,x3,x4,x5,pipe_x1
        x1-=1 ; x2 -= 1
        if x1 <=-500:
            x1 += 1000
        if x2 <= -500:
            x2 += 1000
        
        x4-=1.5 ; x5 -= 1.5
        if x4 <=-500:
            x4 += 1000
        if x5 <= -500:
            x5 += 1000
        

        pipe_x1-=1.5 ;
        if pipe_x1 <= -96:
            pipe_x1 = 500 +150 
            pipe_y1 = random.randrange(-250,-60,50)
        
        pipe_x2-=1.5 ;
        if pipe_x2 <= -96:
            pipe_x2 = 500+150
            pipe_y2 = random.randrange(-250,-60,100)
        
        pipe_x3-=1.5 ;
        if pipe_x3 <= -96:
            pipe_x3 = 500 + 150
            pipe_y3 = random.randrange(-250,-60,50)

    

    run = True
    
    while run:
        global bird,scored
        screen.fill((78,192,202))

        pos = mouse.get_pos()
        for ev in event.get():
            if ev.type == QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    run=False
                    return True
                if ev.key == K_SPACE or ev.key == K_UP or ev.key == K_RETURN and dead != True:
                    if bird_y-20 <=0:
                        bird_y -= 0
                    else:
                        velocity = -2.5
                        bird_y+=velocity
                    mixer.Sound.play(mixer.Sound(r("assets/sfx/wing.ogg")))
                    continue
            if mouse.get_pressed()[0] == True and dead!= True:
                if bird_y-20 <=0:
                    bird_y -= 0
                else:
                    velocity = -2.5
                    bird_y += velocity
                mixer.Sound.play(mixer.Sound(r("assets/sfx/wing.ogg")))
                continue

        #3 hitboxes of the bird
        bird_rect_bottom = draw.rect(screen,(255,0,0),(90,bird_y+(24*1.5)-2,34*1.5-12,2))
        bird_rect_top = draw.rect(screen,(255,0,0),(90,bird_y-1,34*1.5-20,2))
        all_possible_collision = [pygame.draw.rect(screen,(255,0,0),(pipe_x1+9,pipe_y1,75,290)) , pygame.draw.rect(screen,(255,0,0),(pipe_x1+9,pipe_y1+345+76+50,75,290)),
        pygame.draw.rect(screen,(255,0,0),(pipe_x2+9,pipe_y2,75,290)) , pygame.draw.rect(screen,(255,0,0),(pipe_x2+9,pipe_y2+345+76+50,75,290)),
        pygame.draw.rect(screen,(255,0,0),(pipe_x3+9,pipe_y3,75,290)) , pygame.draw.rect(screen,(255,0,0),(pipe_x3+9,pipe_y3+345+76+50,75,290)),
        pygame.draw.rect(screen,(255,255,255),(0,430,500,50)),pygame.draw.rect(screen,(255,0,0),(pipe_x1,pipe_y1+335-52,96,50)),
        pygame.draw.rect(screen,(255,0,0),(pipe_x1,pipe_y1+345+76,96,52)),
        pygame.draw.rect(screen,(255,0,0),(pipe_x2,pipe_y2+335-52,96,50)),
        pygame.draw.rect(screen,(255,0,0),(pipe_x2,pipe_y2+345+76,96,52)),
        pygame.draw.rect(screen,(255,0,0),(pipe_x3,pipe_y3+335-52,96,50)),
        pygame.draw.rect(screen,(255,0,0),(pipe_x3,pipe_y3+345+76,96,52))]

        screen.blit(bg,(x1,0))
        screen.blit(bg,(x2,0))

        screen.blit(pipe_up,(pipe_x1,pipe_y1))
        screen.blit(pipe_up,(pipe_x2,pipe_y2))
        screen.blit(pipe_up,(pipe_x3,pipe_y3))
        
        screen.blit(ground,(x4,430))
        screen.blit(ground,(x5,430))
    
        scroll()

        animate()

        for obstacle in all_possible_collision:
            if bird_rect_bottom.colliderect(obstacle) or bird_rect_top.colliderect(obstacle):
                mixer.Sound.play(mixer.Sound(r("assets/sfx/hit.ogg")))
                mixer.Sound.play(mixer.Sound(r("assets/sfx/die.ogg")))
                pygame.time.delay(600)
                dead = True
                run = False
                return
        clock.tick(fps)
        display.update()

def menu():
    global x1,x2,x3,x4,x5
    run = True
    x1 = 0 ; x2 = 500
    x4 = 0 ; x5 = 500
    begin_y = 300
    while run:
        pos = mouse.get_pos()
        screen.fill((78,192,202))
        cross = pygame.draw.rect(screen,(255,3,72),(500-20-38,18,40,40))
        start_rect = draw.rect(screen,(255,0,0),(205,begin_y+10,96,70))
        screen.blit(bg,(x1,0))
        screen.blit(bg,(x2,0))

        x1-=0.5 ; x2 -= 0.5
        if x1 <=-500:
            x1 += 1000
        if x2 <= -500:
            x2 += 1000
        screen.blit(title,(64,55))
        
        for ev in event.get():
            if ev.type == QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    return False
                    if not menu():  run = False
                    pygame.quit() ; sys.exit()
                    return False
                if ev.key == K_RETURN or ev.key == K_SPACE:
                    begin_y = 305
            if ev.type == KEYUP:
                if ev.key == K_RETURN or ev.key == K_SPACE:
                    begin_y = 300
                    mixer.Sound.play(swoosh)
                    run = False
                    return True
            if cross.collidepoint(pos) and ev.type==MOUSEBUTTONDOWN:
                run = False
                return False
            if start_rect.collidepoint(pos) and ev.type == MOUSEBUTTONDOWN:
                begin_y = 305
            if start_rect.collidepoint(pos) and ev.type == MOUSEBUTTONUP:
                mixer.Sound.play(swoosh)
                begin_y = 300
                run = False
                return True
        
        screen.blit(button,(205,begin_y))
        screen.blit(quit,(500-20-40,20))
        clock.tick(fps)
        display.update()

def gameover():
    global x1,x2,x3,x4,x5,start

    
    exit_y=300 ; start_y=300
    run = True
    while run:
        pos = mouse.get_pos()
        screen.fill((78,192,202))
        start_rect = pygame.draw.rect(screen,(255,0,0),(100,320,96,50))
        exit_rect = pygame.draw.rect(screen,(255,0,0),(304,320,96,50))
        
        screen.blit(bg,(x1,0))
        screen.blit(bg,(x2,0))

        screen.blit(over,(55,150))


        x1-=0.5 ; x2 -= 0.5
        if x1 <=-500:
            x1 += 1000
        if x2 <= -500:
            x2 += 1000

        for ev in event.get():
            if ev.type == QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_RETURN:
                    start_y = 310
                if ev.key == K_ESCAPE:
                    exit_y = 310
            if ev.type == KEYUP:
                if ev.key == K_RETURN:
                    start_y = 300
                    run = False
                    return False
                if ev.key == K_ESCAPE:
                    exit_y = 300
                    run = False
                    return True
            if exit_rect.collidepoint(pos) and ev.type == MOUSEBUTTONDOWN:
                exit_y = 305
               
            if start_rect.collidepoint(pos) and ev.type == MOUSEBUTTONDOWN:
                start_y = 305
               
            if start_rect.collidepoint(pos) and ev.type == MOUSEBUTTONUP:
                start_y=300
                run=False
                return False
            
            if exit_rect.collidepoint(pos) and ev.type == MOUSEBUTTONUP:
                exit_y = 300
                run = False
                return True
            
            
        screen.blit(start,(100,start_y))

        screen.blit(exit,(304,exit_y))

        clock.tick(fps)
        display.update()

if not menu():
    pygame.quit() ; sys.exit()

while True:
    if game():
        mixer.Sound.play(mixer.Sound(r("assets/sfx/pause.mp3")))
        if not menu():
            pygame.quit() ; sys.exit()
        else:
            continue
    if dead == True:
        if not gameover():
            continue
        else:
            pygame.quit() ; sys.exit()