#!/usr/bin/env python
# coding: utf-8

# Author: Will Skywalker
# Email: cxbats@gmail.com

# Project 2048 - Tkinter
# This code is available to use and share under the Apache license.



__version__ = 0.7
__author__  = "Will Skywalker"
__licence__ = "Apache"



import math, random, sys
import _2048, tkFont
try:
    from Tkinter import *
except ImportError, SystemError:
    raw_input("Environment Error")
    sys.exit()

colors = ['#33B5E5',
          '#AA66CC',
          '#99CC00',
          '#FFBB33',
          '#FF4444',
          '#0099CC',
          '#9933CC',
          '#669900',
          '#FF8800',
          '#CC0000']
FPS = 60


def openFile(score):
    try:
        scoreFile = file("highscore.txt", "r+")
        scoreList = [0]
        for line in scoreFile:
            scoreList.append(int(line))
    except IOError:
        scoreFile = file("highscore.txt", "w")
        scoreList = [0]


# class Gameplay:
#     def __init__(self):
#         openFile()
#         self.maplist = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#         self.score = 0
#         self.highscore = max(scoreList)
#         self.on_play = False

#     def get_maplist(self):
#         return self.maplist

#     def get_score(self):
#         return self.score

#     def get_highscore(self):
#         return self.highscore

#     def game_playing(self):
#         return self.on_play

#     def start_game(self):
#         self.on_play = True

#     def end_game(self):
#         global cubes
#         self.on_play = False
#         scoreFile.write(str(self.score) + "\n")
#         if self.score >= self.highscore:
#             self.highscore = self.score
#         self.score = 0
#         self.maplist = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#         cubes = set([])
#         cubes = create_new_cube(cubes)
#         cubes = create_new_cube(cubes)

#     def change_maplist(self, first_index, second_index, number=0):
#         self.maplist[first_index][second_index] = number
        
#     def update_score(self, number):
#         self.score = number

# class NumberCube:
#     def __init__(self, pos):
#         self.number = 2
#         self.pos = pos
#         self.actual_pos = [self.pos[0] * 100, self.pos[1] * 100]
#         self.size = [90, 90]
#         self.number_display = font_numbers.render(str(self.number), True, white)
#         self.color = [51, 181, 229]
#         gameplay.change_maplist(self.pos[0], self.pos[1], 1)

#     def move(self, direction):
#         global cubes
#         gameplay.change_maplist(self.pos[0], self.pos[1])
#         cubes_copy = list(cubes)
#         for cube in cubes_copy[:]:
#             if [self.pos[0] + direction[0], self.pos[1] + direction[1]] == cube.get_pos():
#                 if self.number == cube.get_number():
#                     cube.change_number(self.number)
#                     cubes.remove(self)
#                 else:
#                     gameplay.change_maplist(self.pos[0], self.pos[1], 1)
#                 return None

#         for cube in cubes_copy[:]:
#             if [self.pos[0] + direction[0]*2, self.pos[1] + direction[1]*2] == cube.get_pos():
#                 if self.number == cube.get_number():
#                     cube.change_number(self.number)
#                     cubes.remove(self)
#                 else:
#                     self.pos[0] = self.pos[0] + direction[0]
#                     self.pos[1] = self.pos[1] + direction[1]
#                     gameplay.change_maplist(self.pos[0], self.pos[1], 1)
#                 return None

#         for cube in cubes_copy[:]:
#             if [self.pos[0] + direction[0]*3, self.pos[1] + direction[1]*3] == cube.get_pos():
#                 if self.number == cube.get_number():
#                     cube.change_number(self.number)
#                     cubes.remove(self)
#                 else:
#                     self.pos[0] = self.pos[0] + direction[0] * 2
#                     self.pos[1] = self.pos[1] + direction[1] * 2
#                     gameplay.change_maplist(self.pos[0], self.pos[1], 1)
#                 return None

#         if direction[0] == -1:
#             self.pos[0] = 0
#         elif direction[0] == 1:
#             self.pos[0] = 3

#         if direction[1] == -1:
#             self.pos[1] = 0
#         elif direction[1] == 1:
#             self.pos[1] = 3

#         gameplay.change_maplist(self.pos[0], self.pos[1], 1)

#     def update(self):
#         self.actual_pos = [self.pos[0] * 100, self.pos[1] * 100]
#         if self.number == 4:
#             self.color = [170, 102, 204]
#             self.number_display = font_numbers.render(str(self.number), True, white)
#         if self.number == 8:
#             self.color = [153, 204, 0]
#             self.number_display = font_numbers.render(str(self.number), True, white)
#         if self.number == 16:
#             self.color = [255, 187, 51]
#             self.number_display = font_numbers_med.render(str(self.number), True, white)
#         if self.number == 32:
#             self.color = [255, 68, 68]
#             self.number_display = font_numbers_med.render(str(self.number), True, white)
#         if self.number == 64:
#             self.color = [0, 153, 204]
#             self.number_display = font_numbers_med.render(str(self.number), True, white)
#         if self.number == 128:
#             self.color = [153, 51, 204]
#             self.number_display = font_numbers_small.render(str(self.number), True, white)
#         if self.number == 256:
#             self.color = [102, 153, 0]
#             self.number_display = font_numbers_small.render(str(self.number), True, white)
#         if self.number == 512:
#             self.color = [255, 136, 0]
#             self.number_display = font_numbers_small.render(str(self.number), True, white)
#         if self.number == 1024:
#             self.color = [204, 0, 0]
#             self.number_display = font_numbers_small.render(str(self.number), True, white)
#         if self.number == 2048:
#             self.color = [0, 0, 0]
#             self.number_display = font_numbers_small.render(str(self.number), True, white)
#         pygame.draw.rect(canvas, self.color, Rect((self.actual_pos[0] + 5, self.actual_pos[1] + 5), self.size))
#         canvas.blit(self.number_display, (self.actual_pos[0] + 5, self.actual_pos[1] + 5))

#     def get_pos(self):
#         return self.pos

#     def get_actual_pos(self):
#         return self.actual_pos

#     def get_number(self):
#         return self.number

#     def change_number(self, num):
#         self.number += num


# def keydown(key):
#     global cubes
#     # move_sound.play()
#     if pygame.key.name(key) == "space":
#         if gameplay.game_playing():
#             gameplay.end_game()
#         elif not gameplay.game_playing():
#             gameplay.start_game()

#     if pygame.key.name(key) == "left" and gameplay.game_playing():
#         sorted_cubelist = sorted(list(cubes), 
#                                  key=lambda cube : cube.get_pos()[0] + cube.get_pos()[1] * 4)
#         for cube in sorted_cubelist:
#             cube.move([-1, 0])
#         cubes = create_new_cube(cubes)

#     if pygame.key.name(key) == "right" and gameplay.game_playing():
#         sorted_cubelist = sorted(list(cubes), 
#                                  key=lambda cube : cube.get_pos()[0] + cube.get_pos()[1] * 4,
#                                  reverse=True)
#         for cube in sorted_cubelist:
#             cube.move([1, 0])
#         cubes = create_new_cube(cubes)

#     if pygame.key.name(key) == "up" and gameplay.game_playing():
#         sorted_cubelist = sorted(list(cubes), 
#                                  key=lambda cube : cube.get_pos()[0] + cube.get_pos()[1] * 4)
#         for cube in sorted_cubelist:
#             cube.move([0, -1])
#         cubes = create_new_cube(cubes)

#     if pygame.key.name(key) == "down" and gameplay.game_playing():
#         sorted_cubelist = sorted(list(cubes), 
#                                  key=lambda cube : cube.get_pos()[0] + cube.get_pos()[1] * 4,
#                                  reverse=True)
#         for cube in sorted_cubelist:
#             cube.move([0, 1])
#         cubes = create_new_cube(cubes)



# def create_new_cube(cubes):
#     new_pos = [random.randrange(4), random.randrange(4)]

#     if gameplay.get_maplist()[new_pos[0]][new_pos[1]] == 1: 
#         for rows in gameplay.get_maplist():
#             try:
#                 new_pos[1] = rows.index(0)
#                 new_pos[0] = gameplay.get_maplist().index(rows)
#                 new_cube = NumberCube(new_pos)
#                 cubes.add(new_cube)
#                 break
#             except ValueError:
#                 continue
#     else: 
#         new_cube = NumberCube(new_pos)
#         cubes.add(new_cube)

#     return cubes


def main():
    global gameplay
    root = Tk()
    canvas = Canvas(root, bg='#FFFFFF', height=420, width=400) 
    font_numbers = tkFont.Font(family="SketchRockwell", size=96)
    font_numbers_med = tkFont.Font(family="SketchRockwell", size=72)
    font_numbers_small = tkFont.Font(family="SketchRockwell", size=48)
    font_numbers_text = tkFont.Font(family="SketchRockwell", size=24)
    gameplay = _2048.Gameplay()

    # move_sound = pygame.mixer.Sound("missile.ogg")
    playing = False


    # cubes = set([])
    # cubes = create_new_cube(cubes)
    # cubes = create_new_cube(cubes)
    def welcome():
        canvas.create_rectangle(0, 130, 100, 230, fill='#33B5E5', outline='#33B5E5', activefill='#0099CC', activeoutline='#0099CC', tags='splash')
        canvas.create_rectangle(100, 93, 200, 193, fill='#AA66CC', outline='#AA66CC', activefill='#9933CC', activeoutline='#9933CC', tags='splash')
        canvas.create_rectangle(200, 146, 300, 246, fill='#99CC00', outline='#99CC00', activefill='#669900', activeoutline='#669900', tags='splash')
        canvas.create_rectangle(300, 115, 401, 215, fill='#FFBB33', outline='#FFBB33', activefill='#FF8800', activeoutline='#FF8800', tags='splash')

        canvas.create_text(50, 182, text='2', font=font_numbers, fill='white', tags='splash')
        canvas.create_text(150, 145, text='0', font=font_numbers, fill='white', tags='splash')
        canvas.create_text(250, 198, text='4', font=font_numbers, fill='white', tags='splash')
        canvas.create_text(350, 167, text='8', font=font_numbers, fill='white', tags='splash')
        canvas.create_text(200, 52, text='Made by Will Skywalker', font=font_numbers_text, fill=random.choice(('#0099CC','#9933CC','#669900','#FF8800','#CC0000')), tags='splash')
        canvas.create_text(200, 350, text='v'+str(__version__), font=font_numbers_med, fill='#555555', tags='splash')

    def start_new_game():
        global gameplay
        gameplay = _2048.Gameplay()
        canvas.delete('splash')
        draw_tile()
        # playing = 

    def draw_tile():
        canvas.delete('tile')
        for row in xrange(gameplay.get_grid_height()):
            for col in xrange(gameplay.get_grid_width()):
                num = gameplay.get_tile(row, col)
                if num == 0:
                    continue
                actual_x = (col + 1) * 100 - 50
                actual_y = (row + 1) * 100 - 50
                if num < 2048:
                    color = colors[int(math.log(num, 2)-1)]
                else:
                    color = '#555555'
                canvas.create_rectangle(actual_x-45, actual_y-45, actual_x+45, actual_y+45, fill=color, outline=color, tags='tile')
                if num < 10:
                    canvas.create_text(actual_x+10, actual_y+5, text=str(num), font=font_numbers, fill='white', tags='tile')
                elif num < 100:
                    canvas.create_text(actual_x+8, actual_y+12, text=str(num), font=font_numbers_med, fill='white', tags='tile')
                else:
                    canvas.create_text(actual_x+5, actual_y+24, text=str(num), font=font_numbers_small, fill='white', tags='tile')

    def keyup(key):
        gameplay.move('UP')
        draw_tile()

    def keydown(key):
        gameplay.move('DOWN')
        draw_tile()

    def keyleft(key):
        gameplay.move('LEFT')
        draw_tile()

    def keyright(key):
        gameplay.move('RIGHT')
        draw_tile()




    game_button = Button(root, text='New Game', command=start_new_game)
    font_numbers = tkFont.Font(family="SketchRockwell", size=96)
    font_numbers_text = tkFont.Font(family="SketchRockwell", size=24)
    font_numbers_med = tkFont.Font(family="SketchRockwell", size=72)
    font_numbers_small = tkFont.Font(family="SketchRockwell", size=48)
    a_label = Label(root, text='This is a test')

    root.bind(sequence='<KeyPress-Up>', func=keyup)
    root.bind(sequence='<KeyPress-Down>', func=keydown)
    root.bind(sequence='<KeyPress-Left>', func=keyleft)
    root.bind(sequence='<KeyPress-Right>', func=keyright)

    welcome()
    canvas.grid(columnspan=4)
    game_button.grid(row=1, column=0)
    a_label.grid(row=1, column=3)

    root.title('Sample application')
    root.mainloop() 


    # while True:
    #     for event in pygame.event.get():
    #         if event.type == QUIT:
    #             sys.exit()

    #         if event.type == KEYDOWN:
    #             canvas.fill((255,255,255))
    #             keydown(event.key)

    #     if not gameplay.game_playing():
    #         pygame.draw.rect(canvas, [153, 204, 0], Rect((0, 130), [100, 100]))
    #         pygame.draw.rect(canvas, [255, 68, 68], Rect((100, 93), [100, 100]))
    #         pygame.draw.rect(canvas, [255, 136, 0], Rect((200, 146), [100, 100]))
    #         pygame.draw.rect(canvas, [170, 102, 204], Rect((300, 115), [100, 100]))
    #         num_dos = font_numbers.render("2", True, white)
    #         num_cero = font_numbers.render("0", True, white)
    #         num_cuatro = font_numbers.render("4", True, white)
    #         num_ocho = font_numbers.render("8", True, white)
    #         my_sign = font_numbers_text.render("Made by Will Skywalker", False, [0,153,204])
    #         toast = font_toast.render("Press Space to start the game", False, [0,0,0])
    #         canvas.blit(num_dos, (20, 140))
    #         canvas.blit(num_cero, (120, 103))
    #         canvas.blit(num_cuatro, (220, 156))
    #         canvas.blit(num_ocho, (320, 125))
    #         canvas.blit(my_sign, (48, 30))
    #         canvas.blit(toast, (50, 350))

    #     else:
    #         for cube in cubes:
    #             cube.update()
    #             temp_scr += cube.get_number()
    #         gameplay.update_score(temp_scr)
    #         temp_scr = 0
    #         scoretoast = font_toast.render("Your score: "+str(gameplay.get_score()), False, [0,0,0])
    #         highScoreToast = font_toast.render("High score: "+str(gameplay.get_highscore()), False, [0,0,0])
    #         canvas.blit(scoretoast, (10, 400))
    #         canvas.blit(highScoreToast, (220, 400))

    #     pygame.display.update()
    #     FPSCLOCK.tick(FPS)





if __name__ == "__main__":
    main()
