#!/usr/bin/env python
# coding: utf-8

# Author: Will Skywalker
# Email: cxbats@gmail.com

# Project 2048 - Tkinter
# This code is available to use and share under the Apache license.



__version__ = '0.7.2'
__author__  = "Will Skywalker"
__licence__ = "Apache"



import math, random, sys, tkFont
import _2048, monte_carlo
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

    def welcome():
        canvas.create_rectangle(0, 130, 100, 230, fill='#33B5E5', outline='#33B5E5', 
                                activefill='#0099CC', activeoutline='#0099CC', tags='splash')
        canvas.create_rectangle(100, 93, 200, 193, fill='#AA66CC', outline='#AA66CC', 
                                activefill='#9933CC', activeoutline='#9933CC', tags='splash')
        canvas.create_rectangle(200, 146, 300, 246, fill='#99CC00', outline='#99CC00', 
                                activefill='#669900', activeoutline='#669900', tags='splash')
        canvas.create_rectangle(300, 115, 401, 215, fill='#FFBB33', outline='#FFBB33', 
                                activefill='#FF8800', activeoutline='#FF8800', tags='splash')

        canvas.create_text(50, 182, text='2', font=font_numbers, fill='white', tags='splash')
        canvas.create_text(150, 145, text='0', font=font_numbers, fill='white', tags='splash')
        canvas.create_text(250, 198, text='4', font=font_numbers, fill='white', tags='splash')
        canvas.create_text(350, 167, text='8', font=font_numbers, fill='white', tags='splash')
        canvas.create_text(200, 52, text='Made by Will Skywalker', font=font_numbers_text, 
                           fill=random.choice(('#0099CC','#9933CC','#669900','#FF8800','#CC0000')), 
                           tags='splash')
        canvas.create_text(200, 350, text='v'+str(__version__), font=font_numbers_med, 
                           fill='#555555', tags='splash')

    def start_new_game():
        global gameplay
        gameplay = _2048.Gameplay()
        canvas.delete('splash')
        draw_tile()

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
                canvas.create_rectangle(actual_x-45, actual_y-45, actual_x+45, actual_y+45, 
                                        fill=color, outline=color, tags='tile')
                if num < 10:
                    canvas.create_text(actual_x+10, actual_y+5, text=str(num), 
                                       font=font_numbers, fill='white', tags='tile')
                elif num < 100:
                    canvas.create_text(actual_x+8, actual_y+12, text=str(num), 
                                       font=font_numbers_med, fill='white', tags='tile')
                else:
                    canvas.create_text(actual_x+5, actual_y+24, text=str(num), 
                                       font=font_numbers_small, fill='white', tags='tile')

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

    def find_best(key=None):
        best = monte_carlo.monte_carlo(gameplay)
        if best:
            popup = Toplevel()
            popup.title("Recommendation")
            msg = Message(popup, text='Computed Best Strategy: '+best).pack()
            # popup.bind(sequence='<KeyPress-Return>', func=popup.destroy)
            button = Button(popup, text="Got It!", command=popup.destroy)
            button.pack()
        else:
            popup = Toplevel()
            popup.title("Lose")
            msg = Message(popup, text='You\'ve lost!').pack()
            button = Button(popup, text="OK", command=popup.destroy)
            button.pack()



    game_button = Button(root, text='New Game', command=start_new_game)
    font_numbers = tkFont.Font(family="SketchRockwell", size=96)
    font_numbers_text = tkFont.Font(family="SketchRockwell", size=24)
    font_numbers_med = tkFont.Font(family="SketchRockwell", size=72)
    font_numbers_small = tkFont.Font(family="SketchRockwell", size=48)
    solve_button = Button(root, text='Find the Best Stretegy',command=find_best)

    root.bind(sequence='<KeyPress-Up>', func=keyup)
    root.bind(sequence='<KeyPress-Down>', func=keydown)
    root.bind(sequence='<KeyPress-Left>', func=keyleft)
    root.bind(sequence='<KeyPress-Right>', func=keyright)
    root.bind(sequence='<Shift-KeyPress-R>', func=find_best)

    welcome()
    canvas.grid(columnspan=4)
    game_button.grid(row=1, column=0)
    solve_button.grid(row=1, column=3)

    root.title('2048')
    root.mainloop() 




if __name__ == "__main__":
    main()
