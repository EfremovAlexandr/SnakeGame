import pygame
import random

class Apple():

    def __init__(self):
        """инициализация яблока"""

        self.size = 10
        self.color = 'red'

    def get_color(self):
        color_list = []
        red_list = ['red']*10
        green_list = ['green']
        blue_list = ['blue']
        color_list.extend(red_list)
        color_list.extend(green_list)
        color_list.extend(blue_list)
        self.color = random.choice(color_list)

    def output(self, dis):
        self.image = pygame.image.load('images/' + self.color + '_apple.png')
        self.rect_image = self.image.get_rect()
        self.rect_image.x = self.x
        self.rect_image.y = self.y
        self.rect_image.size = (self.size, self.size)
        dis.blit(self.image, self.rect_image)

    def apple_coordinates(self, dis_width, dis_height):
        self.x = round(random.randrange(0, dis_width - self.size) / 10.0) * 10.0
        self.y = round(random.randrange(0, dis_height - self.size) / 10.0) * 10.0
