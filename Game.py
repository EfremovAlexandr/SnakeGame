import time
import pygame
import random

pygame.init()

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.update()
pygame.display.set_caption('Змейка для Димы')

color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_blue = (0, 0, 255)
color_red = (255, 0, 0)
color_yellow = (222, 235, 143)
color_score = (133, 64, 15)
snake_block = 10
snake_speed = 10

clock = pygame.time.Clock()



font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render("Очки: " + str(score), True, color_score)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, color_black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):

    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/10, dis_height/2])

def gameLoop():

    game_over = False
    game_close = False
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_lenght = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    while not game_over:
        while  game_close == True:
            dis.fill(color_white)
            message("ТЫ ПРОИГРАЛ! В-Выход, И-Играть", color_red)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_b:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 < 0 or x1 >= dis_width or y1 < 0 or y1 > dis_height:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(color_yellow)

        pygame.draw.rect(dis, color_blue, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > snake_lenght:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        our_snake(snake_block, snake_list)
        your_score(snake_lenght-1)
        pygame.draw.rect(dis, color_black, [x1, y1, snake_block, snake_block])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            snake_lenght += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()

gameLoop()
