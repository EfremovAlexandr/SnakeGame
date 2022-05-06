import pygame
from snake import Snake
from apple import Apple

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
    snake.speed = ((value // 5) + 1) * 5
    value = score_font.render("Уровень: " + str(((value // 5) + 1)), True, color_score)
    dis.blit(value, [200, 0])
    value = score_font.render("Скорость: " + str(snake.speed), True, color_score)
    dis.blit(value, [400, 0])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 10, dis_height / 2])


def gameloop():
    pygame.mixer.music.load('sounds/snake_crowling.mp3')
    pygame.mixer.music.play(-1)
    snake = Snake(dis)
    apple = Apple()
    apple.apple_coordinates(dis_width, dis_height)
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

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
                        gameloop()

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
            s = pygame.mixer.Sound("sounds/zvuk-kogda-uroven-ne-proshli.wav")
            s.play()
        x1 += x1_change
        y1 += y1_change
        dis.fill(color_yellow)

        snake_head = snake.addbody(x1, y1)

        if len(snake.snake_list) > snake.lenght:
            del snake.snake_list[0]
        for x in snake.snake_list[:-1]:
            if x == snake_head:
                game_close = True
                s = pygame.mixer.Sound("sounds/zvuk-kogda-uroven-ne-proshli.wav")
                s.play()
        snake.output()
        apple.output(dis)

        your_score(snake.lenght - 1)
        your_level(snake.lenght - 1, snake)

        pygame.display.update()

        if x1 == apple.x and y1 == apple.y:
            s = pygame.mixer.Sound("sounds/sglatyivanie-byistroe.wav")
            s.play()
            snake.lenght += 1
            apple.get_color()
            apple.apple_coordinates(dis_width, dis_height)

        clock.tick(snake.speed)
    pygame.quit()
    quit()


gameloop()
