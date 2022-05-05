import pygame

class Snake():

    def __init__(self, dis):
        """инициализация змеи"""

        self.dis = dis
        self.snake_list = []
        self.lenght = 1
        self.speed = 5
        self.snake_block = 10
        self.direction = 'up'

    def output(self):
        """выводим змейку на экран"""

        i = 1
        for x in self.snake_list:
            if i == len(self.snake_list):
                image = pygame.image.load('images/' + self.direction + '.png')
                rect_image = image.get_rect()
                rect_image.x = x[0]
                rect_image.y = x[1]
                rect_image.size = (self.snake_block, self.snake_block)
                self.dis.blit(image, rect_image)
            elif i == 1:
                if x[0] > self.snake_list[1][0]:
                    image = pygame.image.load('images/tale_right.png')
                elif x[0] < self.snake_list[1][0]:
                    image = pygame.image.load('images/tale_left.png')
                elif x[1] > self.snake_list[1][1]:
                    image = pygame.image.load('images/tale_down.png')
                else:
                    image = pygame.image.load('images/tale_up.png')

                rect_image = image.get_rect()
                rect_image.x = x[0]
                rect_image.y = x[1]
                rect_image.size = (self.snake_block, self.snake_block)
                self.dis.blit(image, rect_image)
            else:
                image = pygame.image.load('images/body.png')
                rect_image = image.get_rect()
                rect_image.x = x[0]

                rect_image.y = x[1]
                rect_image.size = (self.snake_block, self.snake_block)
                self.dis.blit(image, rect_image)
            i += 1

    def addbody(self, x1, y1):
        """удлиняем тело змеи и взовращаем добавленный список"""
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        self.snake_list.append(snake_head)
        return snake_head
