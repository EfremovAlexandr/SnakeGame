import pygame
import random
from snake import Snake

pygame.init()

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.update()
pygame.display.set_caption('Змейка для  Димы')

color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_blue = (0, 0, 255)
color_red = (255, 0, 0)
color_yellow = (222, 235, 143)
color_score = (133, 64, 15)

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render("Очки: " + str(score), True, color_score)
    dis.blit(value, [0, 0])

def your_level(score, snake):
    value = score
    snake.speed = ((value//5)+1) * 5
    value = score_font.render("Уровень: " + str(((value//5)+1)), True, color_score)
    dis.blit(value, [200, 0])
    value = score_font.render("Скорость: " + str(snake.speed), True, color_score)
    dis.blit(value, [400, 0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 10, dis_height / 2])


def gameLoop():

    snake = Snake(dis)

    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake.snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake.snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
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
                if event.key == pygame.K_LEFT and snake.direction != 'right':
                    snake.direction = 'left'
                    x1_change = -snake.snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and snake.direction != 'left':
                    snake.direction = 'right'
                    x1_change = snake.snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and snake.direction != 'down':
                    snake.direction = 'up'
                    x1_change = 0
                    y1_change = -snake.snake_block
                elif event.key == pygame.K_DOWN and snake.direction != 'up':
                    snake.direction = 'down'
                    x1_change = 0
                    y1_change = snake.snake_block

        if x1 < 0 or x1 >= dis_width or y1 < 0 or y1 > dis_height:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(color_yellow)

        #pygame.draw.rect(dis, color_blue, [foodx, foody, snake.snake_block, snake.snake_block])
        image = pygame.image.load('images/red_apple.png')
        rect_image = image.get_rect()
        rect_image.x = foodx
        rect_image.y = foody
        rect_image.size = (snake.snake_block, snake.snake_block)
        dis.blit(image, rect_image)

        #value = score_font.render("яблоко: x " + str(foodx) + " y " + str(foody), True, color_score)
        #dis.blit(value, [0, 60])

        snake_head = snake.addbody(x1, y1)


        if len(snake.snake_list) > snake.lenght:
            del snake.snake_list[0]
        for x in snake.snake_list[:-1]:
            if x == snake_head:
                game_close = True
        snake.output()

        your_score(snake.lenght - 1)
        your_level(snake.lenght - 1, snake)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake.snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake.snake_block) / 10.0) * 10.0
            snake.lenght += 1

        clock.tick(snake.speed)
    pygame.quit()
    quit()


gameLoop()
