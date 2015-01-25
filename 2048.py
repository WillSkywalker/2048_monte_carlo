#!/usr/bin/env python
# coding: utf-8

# Author: Will Skywalker
# Email: cxbats@gmail.com

# Project 2048 - PyGame
# This code is available to use and share under the Apache license.

import math, random, sys
try:
    import pygame
    from pygame.locals import *
except ImportError, SystemError:
    raw_input("Please inatall Pygame first!")
    sys.exit()


white = (255, 255, 255)
FPS = 60


def openFile():
    global scoreFile, scoreList
    try:
        scoreFile = file("highscore.txt", "r+")
        scoreList = [0]
        for line in scoreFile:
            scoreList.append(int(line))
    except IOError:
        scoreFile = file("highscore.txt", "w")
        scoreList = [0]


class Gameplay:
    def __init__(self):
        openFile()
        self.maplist = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.score = 0
        self.highscore = max(scoreList)
        self.on_play = False

    def get_maplist(self):
        return self.maplist

    def get_score(self):
        return self.score

    def get_highscore(self):
        return self.highscore

    def game_playing(self):
        return self.on_play

    def start_game(self):
        self.on_play = True

    def end_game(self):
        global cubes
        self.on_play = False
        scoreFile.write(str(self.score) + "\n")
        if self.score >= self.highscore:
            self.highscore = self.score
        self.score = 0
        self.maplist = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        cubes = set([])
        cubes = create_new_cube(cubes)
        cubes = create_new_cube(cubes)

    def change_maplist(self, first_index, second_index, number=0):
        self.maplist[first_index][second_index] = number
        
    def update_score(self, number):
        self.score = number

class NumberCube:
    def __init__(self, pos):
        self.number = 2
        self.pos = pos
        self.actual_pos = [self.pos[0] * 100, self.pos[1] * 100]
        self.size = [90, 90]
        self.number_display = font_numbers.render(str(self.number), True, white)
        self.color = [51, 181, 229]
        gameplay.change_maplist(self.pos[0], self.pos[1], 1)

    def move(self, direction):
        global cubes
        gameplay.change_maplist(self.pos[0], self.pos[1])
        cubes_copy = list(cubes)
        for cube in cubes_copy[:]:
            if [self.pos[0] + direction[0], self.pos[1] + direction[1]] == cube.get_pos():
                if self.number == cube.get_number():
                    cube.change_number(self.number)
                    cubes.remove(self)
                else:
                    gameplay.change_maplist(self.pos[0], self.pos[1], 1)
                return None

        for cube in cubes_copy[:]:
            if [self.pos[0] + direction[0]*2, self.pos[1] + direction[1]*2] == cube.get_pos():
                if self.number == cube.get_number():
                    cube.change_number(self.number)
                    cubes.remove(self)
                else:
                    self.pos[0] = self.pos[0] + direction[0]
                    self.pos[1] = self.pos[1] + direction[1]
                    gameplay.change_maplist(self.pos[0], self.pos[1], 1)
                return None

        for cube in cubes_copy[:]:
            if [self.pos[0] + direction[0]*3, self.pos[1] + direction[1]*3] == cube.get_pos():
                if self.number == cube.get_number():
                    cube.change_number(self.number)
                    cubes.remove(self)
                else:
                    self.pos[0] = self.pos[0] + direction[0] * 2
                    self.pos[1] = self.pos[1] + direction[1] * 2
                    gameplay.change_maplist(self.pos[0], self.pos[1], 1)
                return None

        if direction[0] == -1:
            self.pos[0] = 0
        elif direction[0] == 1:
            self.pos[0] = 3

        if direction[1] == -1:
            self.pos[1] = 0
        elif direction[1] == 1:
            self.pos[1] = 3

        gameplay.change_maplist(self.pos[0], self.pos[1], 1)

    def update(self):
        self.actual_pos = [self.pos[0] * 100, self.pos[1] * 100]
        if self.number == 4:
            self.color = [170, 102, 204]
            self.number_display = font_numbers.render(str(self.number), True, white)
        if self.number == 8:
            self.color = [153, 204, 0]
            self.number_display = font_numbers.render(str(self.number), True, white)
        if self.number == 16:
            self.color = [255, 187, 51]
            self.number_display = font_numbers_med.render(str(self.number), True, white)
        if self.number == 32:
            self.color = [255, 68, 68]
            self.number_display = font_numbers_med.render(str(self.number), True, white)
        if self.number == 64:
            self.color = [0, 153, 204]
            self.number_display = font_numbers_med.render(str(self.number), True, white)
        if self.number == 128:
            self.color = [153, 51, 204]
            self.number_display = font_numbers_small.render(str(self.number), True, white)
        if self.number == 256:
            self.color = [102, 153, 0]
            self.number_display = font_numbers_small.render(str(self.number), True, white)
        if self.number == 512:
            self.color = [255, 136, 0]
            self.number_display = font_numbers_small.render(str(self.number), True, white)
        if self.number == 1024:
            self.color = [204, 0, 0]
            self.number_display = font_numbers_small.render(str(self.number), True, white)
        if self.number == 2048:
            self.color = [0, 0, 0]
            self.number_display = font_numbers_small.render(str(self.number), True, white)
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
    # move_sound.play()
    if pygame.key.name(key) == "space":
        if gameplay.game_playing():
            gameplay.end_game()
        elif not gameplay.game_playing():
            gameplay.start_game()

    if pygame.key.name(key) == "left" and gameplay.game_playing():
        sorted_cubelist = sorted(list(cubes), 
                                 key=lambda cube : cube.get_pos()[0] + cube.get_pos()[1] * 4)
        for cube in sorted_cubelist:
            cube.move([-1, 0])
        cubes = create_new_cube(cubes)

    if pygame.key.name(key) == "right" and gameplay.game_playing():
        sorted_cubelist = sorted(list(cubes), 
                                 key=lambda cube : cube.get_pos()[0] + cube.get_pos()[1] * 4,
                                 reverse=True)
        for cube in sorted_cubelist:
            cube.move([1, 0])
        cubes = create_new_cube(cubes)

    if pygame.key.name(key) == "up" and gameplay.game_playing():
        sorted_cubelist = sorted(list(cubes), 
                                 key=lambda cube : cube.get_pos()[0] + cube.get_pos()[1] * 4)
        for cube in sorted_cubelist:
            cube.move([0, -1])
        cubes = create_new_cube(cubes)

    if pygame.key.name(key) == "down" and gameplay.game_playing():
        sorted_cubelist = sorted(list(cubes), 
                                 key=lambda cube : cube.get_pos()[0] + cube.get_pos()[1] * 4,
                                 reverse=True)
        for cube in sorted_cubelist:
            cube.move([0, 1])
        cubes = create_new_cube(cubes)



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
    global canvas, cubes, font_numbers, font_numbers_med, font_numbers_small, maplist, move_sound
    pygame.init()
    canvas = pygame.display.set_mode((400, 420))
    font_numbers = pygame.font.Font("SketchRockwell_Bold.ttf", 96)
    font_numbers_med = pygame.font.Font("SketchRockwell_Bold.ttf", 72)
    font_numbers_small = pygame.font.Font("SketchRockwell_Bold.ttf", 48)
    font_numbers_text = pygame.font.Font("SketchRockwell_Bold.ttf", 24)
    font_toast = pygame.font.Font("Secrcode.ttf", 20)
    # move_sound = pygame.mixer.Sound("missile.ogg")
    temp_scr = 0

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

        if not gameplay.game_playing():
            pygame.draw.rect(canvas, [153, 204, 0], Rect((0, 130), [100, 100]))
            pygame.draw.rect(canvas, [255, 68, 68], Rect((100, 93), [100, 100]))
            pygame.draw.rect(canvas, [255, 136, 0], Rect((200, 146), [100, 100]))
            pygame.draw.rect(canvas, [170, 102, 204], Rect((300, 115), [100, 100]))
            num_dos = font_numbers.render("2", True, white)
            num_cero = font_numbers.render("0", True, white)
            num_cuatro = font_numbers.render("4", True, white)
            num_ocho = font_numbers.render("8", True, white)
            my_sign = font_numbers_text.render("Made by Will Skywalker", False, [0,153,204])
            toast = font_toast.render("Press Space to start the game", False, [0,0,0])
            canvas.blit(num_dos, (20, 140))
            canvas.blit(num_cero, (120, 103))
            canvas.blit(num_cuatro, (220, 156))
            canvas.blit(num_ocho, (320, 125))
            canvas.blit(my_sign, (48, 30))
            canvas.blit(toast, (50, 350))

        else:
            for cube in cubes:
                cube.update()
                temp_scr += cube.get_number()
            gameplay.update_score(temp_scr)
            temp_scr = 0
            scoretoast = font_toast.render("Your score: "+str(gameplay.get_score()), False, [0,0,0])
            highScoreToast = font_toast.render("High score: "+str(gameplay.get_highscore()), False, [0,0,0])
            canvas.blit(scoretoast, (10, 400))
            canvas.blit(highScoreToast, (220, 400))

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == "__main__":
    gameplay = Gameplay()
    main()
