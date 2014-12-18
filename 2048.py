#!/usr/bin/env python
# coding: utf-8

# Author: Will Skywalker
# Email: cxbats@gmail.com

# Project 2048 - PyGame
# This code is available to use and share under the Apache license.

from __future__ import division, print_function
import math, random, sys
try:
    import pygame
    from pygame.locals import *
except ImportError, SystemError:
    raw_input("Please inatall Pygame first!")
    sys.exit()


class Gameplay:
    def __init__(self):
        self.maplist = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    def get_maplist(self):
        return self.maplist

    def change_maplist(self, first_index, second_index, number=0):
        self.maplist[first_index][second_index] = number
        

class NumberCube:
    def __init__(self, pos):
        self.number = 2
        self.pos = pos
        self.actual_pos = [self.pos[0] * 100, self.pos[1] * 100]
        self.size = [90, 90]
        self.number_display = font_numbers.render(str(self.number), True, (255, 255, 255))
        self.color = [51, 181, 229]

    def move(self, direction):
        gameplay.change_maplist(self.pos[0], self.pos[1])
        cubes_copy = list(cubes)
        for cube in cubes_copy[:]:
            if [self.pos[0] + direction[0], self.pos[1] + direction[1]] == cube.get_pos():
                if self.number == cube.get_number():
                    cube.change_number(self.number)
                    cubes.remove(self)
                gameplay.change_maplist(self.pos[0], self.pos[1], 1)
                return None

        if not ((self.pos[0] == 0 and direction[0] == -1) or (self.pos[0] == 3 and direction[0] == 1)):
            self.pos[0] = self.pos[0] + direction[0] 
        if not ((self.pos[1] == 0 and direction[1] == -1) or (self.pos[1] == 3 and direction[1] == 1)):
            self.pos[1] = self.pos[1] + direction[1]
        gameplay.change_maplist(self.pos[0], self.pos[1], 1)


    def update(self):
        self.actual_pos = [self.pos[0] * 100, self.pos[1] * 100]
        if self.number == 4:
            self.color = [170, 102, 204]
            self.number_display = font_numbers.render(str(self.number), True, (255, 255, 255))
        if self.number == 8:
            self.color = [153, 204, 0]
            self.number_display = font_numbers.render(str(self.number), True, (255, 255, 255))
        if self.number == 16:
            self.color = [255, 187, 51]
            self.number_display = font_numbers_med.render(str(self.number), True, (255, 255, 255))
        if self.number == 32:
            self.color = [255, 68, 68]
            self.number_display = font_numbers_med.render(str(self.number), True, (255, 255, 255))
        if self.number == 64:
            self.color = [0, 153, 204]
            self.number_display = font_numbers_med.render(str(self.number), True, (255, 255, 255))
        if self.number == 128:
            self.color = [153, 51, 204]
            self.number_display = font_numbers_small.render(str(self.number), True, (255, 255, 255))
        if self.number == 256:
            self.color = [102, 153, 0]
            self.number_display = font_numbers_small.render(str(self.number), True, (255, 255, 255))
        if self.number == 512:
            self.color = [255, 136, 0]
            self.number_display = font_numbers_small.render(str(self.number), True, (255, 255, 255))
        if self.number == 1024:
            self.color = [204, 0, 0]
            self.number_display = font_numbers_small.render(str(self.number), True, (255, 255, 255))
        if self.number == 2048:
            self.color = [0, 0, 0]
            self.number_display = font_numbers_small.render(str(self.number), True, (255, 255, 255))
        pygame.draw.rect(canvas, self.color, Rect((self.actual_pos[0] + 5, self.actual_pos[1] + 5), self.size))
        canvas.blit(self.number_display, (self.actual_pos[0] + 5, self.actual_pos[1] + 5))



    def get_pos(self):
        return self.pos

    def get_actual_pos(self):
        return self.actual_pos

    def get_number(self):
        return self.number

    def change_number(self, num):
        self.number += num


def keydown(key):
    global cubes
    if pygame.key.name(key) == "left":
        for cube in list(cubes):
            cube.move([-1, 0])
        cubes = create_new_cube(cubes)

    if pygame.key.name(key) == "right":
        for cube in list(cubes):
            cube.move([1, 0])
        cubes = create_new_cube(cubes)

    if pygame.key.name(key) == "up":
        for cube in list(cubes):
            cube.move([0, -1])
        cubes = create_new_cube(cubes)

    if pygame.key.name(key) == "down":
        for cube in list(cubes):
            cube.move([0, 1])
        cubes = create_new_cube(cubes)

    if pygame.key.name(key) == "space":
        print("Spacekey Info:",gameplay.get_maplist(), len(cubes))



def create_new_cube(cubes):
    new_pos = [random.randrange(4), random.randrange(4)]

    if gameplay.get_maplist()[new_pos[0]][new_pos[1]] == 1: 
        for rows in gameplay.get_maplist():
            try:
                new_pos[1] = rows.index(0)
                new_pos[0] = gameplay.get_maplist().index(rows)
                new_cube = NumberCube(new_pos)
                cubes.add(new_cube)
                break
            except ValueError:
                continue
    else: 
        new_cube = NumberCube(new_pos)
        cubes.add(new_cube)

    return cubes


def main():
    global canvas, cubes, font_numbers, font_numbers_med, font_numbers_small, maplist
    pygame.init()
    canvas = pygame.display.set_mode((400, 400))
    font_numbers = pygame.font.Font("SketchRockwell_Bold.ttf", 96)
    font_numbers_med = pygame.font.Font("SketchRockwell_Bold.ttf", 72)
    font_numbers_small = pygame.font.Font("SketchRockwell_Bold.ttf", 48)
    pygame.display.set_caption("2048")

    canvas.fill((255,255,255))

    FPSCLOCK = pygame.time.Clock()

    cubes = set([])
    
    cubes = create_new_cube(cubes)
    cubes = create_new_cube(cubes)



    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            if event.type == KEYDOWN:
                canvas.fill((255,255,255))
                keydown(event.key)

        for cube in cubes:
            cube.update()



        pygame.display.update()
        FPSCLOCK.tick(60)



if __name__ == "__main__":
    gameplay = Gameplay()
    main()
