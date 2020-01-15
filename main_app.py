import tkinter as tk
import tkinter.ttk as ttk
from functools import partial
from tkinter import tix
from tkinter.constants import *
from datetime import datetime, date, time, timedelta
import os
from play_game import play_game, play_game2


class MainApp:

    def __init__(self):
        root = tk.Tk()
        root.title = 'TITLE'

        x_size = 8
        y_size = 8

        self.grid = []
        for i in range(0, x_size):
            for j in range(0, y_size):
                self.grid.append([i, j])

        self.gaming_grid = tk.LabelFrame(root, text="Grid")
        self.gaming_grid.pack(side=RIGHT, fill="both", expand="yes")

        for coordinates in self.grid:
            b = tk.Button(self.gaming_grid, text=' ', command=partial(self.left_click, coordinates), relief=RAISED, background="#ccc", width=2, height=1)
            b.grid(column=coordinates[1], row=coordinates[0], sticky='NSEW')
            b.bind('<Button-3>', self.right_click)

        menu = tk.LabelFrame(root, text="Menu")
        menu.pack(side=LEFT, fill="both", expand="yes")

        start_button = tk.Button(menu, text='Start game', bg='white', command=partial(self.start_game))
        start_button.grid(column=0, row=0)
        start_button.bind('<Button-3>', self.right_click)

        root.mainloop()

    def create_grid(self, level):
        if level == 1:
            x_size = 8
            y_size = 8
            nb_bomb = 10

    def start_game(self):

        self.game = play_game2(x_size=8, y_size=8, nb_bombs=10)
        self.game.print_game_2D()

    def right_click(self, event):
        w = event.widget.grid_info()
        x = w['row']
        y = w['column']
        self.game.flag(x, y)
        self.update_board_graphic()

    def left_click(self, coordinates):

        x = coordinates[0]
        y = coordinates[1]
        self.game.update_board(x, y)
        self.update_board_graphic()

        #To be removed soon
        self.game.print_game_2D()

    def update_board_graphic(self):
        self.move_left = 0

        for widget in self.gaming_grid.winfo_children():
            widget.destroy()

        for coordinates in self.grid:
            value = str(self.game.board[coordinates[0]][coordinates[1]])
            #Add actions depending on the value
            if value == '0':
                b = tk.Button(self.gaming_grid, text='0',relief=FLAT, background="#ccc", width=2, height=1, fg='red')
                b.grid(column=coordinates[1], row=coordinates[0])
                b.bind('<Button-3>', self.right_click)

            if value == '1':
                b = tk.Button(self.gaming_grid, text='1', relief=FLAT, background="#ccc", width=2, height=1, fg='red')
                b.grid(column=coordinates[1], row=coordinates[0])
                b.bind('<Button-3>', self.right_click)

            if value == '2':
                b = tk.Button(self.gaming_grid, text='2', relief=FLAT, background="#ccc", width=2, height=1, fg='red')
                b.grid(column=coordinates[1], row=coordinates[0])
                b.bind('<Button-3>', self.right_click)

            if value == '3':
                b = tk.Button(self.gaming_grid, text='3', relief=FLAT, background="#ccc", width=2, height=1, fg='red')
                b.grid(column=coordinates[1], row=coordinates[0])
                b.bind('<Button-3>', self.right_click)

            if value == '4':
                b = tk.Button(self.gaming_grid, text='4', relief=FLAT, background="#ccc", width=2, height=1, fg='red')
                b.grid(column=coordinates[1], row=coordinates[0])
                b.bind('<Button-3>', self.right_click)

            if value == '5':
                b = tk.Button(self.gaming_grid, text='5', relief=FLAT, background="#ccc", width=2, height=1, fg='red')
                b.grid(column=coordinates[1], row=coordinates[0])
                b.bind('<Button-3>', self.right_click)

            if value == '6':
                b = tk.Button(self.gaming_grid, text='6', relief=FLAT, background="#ccc", width=2, height=1, fg='red')
                b.grid(column=coordinates[1], row=coordinates[0])
                b.bind('<Button-3>', self.right_click)

            if value == '7':
                b = tk.Button(self.gaming_grid, text='7', relief=FLAT, background="#ccc", width=2, height=1, fg='red')
                b.grid(column=coordinates[1], row=coordinates[0])
                b.bind('<Button-3>', self.right_click)

            if value == '8':
                b = tk.Button(self.gaming_grid, text='8', relief=FLAT, background="#ccc", width=2, height=1, fg='red')
                b.grid(column=coordinates[1], row=coordinates[0])
                b.bind('<Button-3>', self.right_click)


            if value == '§' or value == '*§*':
                b = tk.Button(self.gaming_grid, text='§', relief=RAISED, background="#ccc", width=2, height=1, fg='blue')
                b.grid(column=coordinates[1], row=coordinates[0])
                b.bind('<Button-3>', self.right_click)


            if value == '?' or value == '*':
                b = tk.Button(self.gaming_grid, text=' ', command=partial(self.left_click, coordinates), relief=RAISED,
                              background="#ccc", width=2, height=1)
                b.grid(column=coordinates[1], row=coordinates[0])
                b.bind('<Button-3>', self.right_click)

            if value == '?':
                self.move_left += 1

        if self.move_left == 0:
            self.game.print_win()

MainApp()

