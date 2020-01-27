import sys
import tkinter as tk
import tkinter.ttk as ttk
from functools import partial
from tkinter import tix
from tkinter.constants import *
from datetime import datetime, date, time, timedelta
import time
import os
from PIL import Image, ImageTk
from RunGame import PlayGameInput, PlayGameGraphic
from NeuralNetwork import CallNN
from DrawBoard import HideBoard

class MainApp:

    def __init__(self):

        level = {'easy': {
                            'x_size': 8,
                            'y_size': 8,
                            'nb_bombs': 10
                         },
                'medium': {
                            'x_size': 16,
                            'y_size': 16,
                            'nb_bombs': 40
                        },
                'hard': {
                            'x_size': 30,
                            'y_size': 16,
                            'nb_bombs': 90
                        }}
        default_level = 'easy'

        self.x_size = level[default_level]['x_size']
        self.y_size = level[default_level]['y_size']
        self.nb_bombs = level[default_level]['nb_bombs']

        self.InitWindow()

    def InitWindow(self):

        self.root = tk.Tk()
        self.root.title = 'TITLE'

        self.grid = []
        for i in range(0, self.x_size):
            for j in range(0, self.y_size):
                self.grid.append([i, j])

        self.gaming_grid = tk.LabelFrame(self.root, text="Grid")
        self.gaming_grid.pack(side=RIGHT, fill="both", expand="yes")

        for coordinates in self.grid:
            b = tk.Button(self.gaming_grid, text=' ', command=partial(self.LeftClick, coordinates), relief=RAISED, background="#ccc", width=2, height=1)
            b.grid(column=coordinates[1], row=coordinates[0], sticky='NSEW')
            b.bind('<Button-3>', self.RightClick)

        menu = tk.LabelFrame(self.root, text="Menu")
        menu.pack(side=LEFT, fill="both", expand="yes")

        start_button = tk.Button(menu, text='Auto play', bg='white', command=partial(self.AutomatedGame))

        start_button.grid(column=0, row=0)
        start_button.bind('<Button-3>', self.RightClick)

        self.StartGame()
        self.root.mainloop()

    def StartGame(self):

        self.game = PlayGameGraphic(self.x_size, self.y_size, self.nb_bombs)
        self.UpdateBoardGraphic()

    def AutomatedGame(self):
        StopPlaying = False
        self.UpdateBoardGraphic()
        while StopPlaying is False:
            x, y = CallNN(HideBoard(self.game.board))
            StopPlaying = self.LeftClick([x, y])
            self.root.update()
            time.sleep(0.5)

        print(self.move_left)
        self.StartGame()
        self.UpdateBoardGraphic()
        self.AutomatedGame()

    def RightClick(self, event):
        w = event.widget.grid_info()
        x = w['row']
        y = w['column']
        self.game.flag(x, y)

    def LeftClick(self, coordinates):

        x = coordinates[0]
        y = coordinates[1]
        StopPlaying = self.game.UpdateBoard(x, y)
        self.UpdateBoardGraphic()

        return StopPlaying

    def UpdateBoardGraphic(self):

        self.move_left = 0

        for widget in self.gaming_grid.winfo_children():
            widget.destroy()

        for coordinates in self.grid:
            value = str(self.game.board[coordinates[0]][coordinates[1]])
            #Add actions depending on the value

            if value == '0':
                b = tk.Button(self.gaming_grid, text=' ',relief=FLAT, background="#ccc", width=2, height=1)
                b.grid(column=coordinates[1], row=coordinates[0])

            if value == '1':
                b = tk.Button(self.gaming_grid, text='1', relief=FLAT, background="#ccc", width=2, height=1, fg='#EA2626')
                b.grid(column=coordinates[1], row=coordinates[0])

            if value == '2':
                b = tk.Button(self.gaming_grid, text='2', relief=FLAT, background="#ccc", width=2, height=1, fg='#2647EA')
                b.grid(column=coordinates[1], row=coordinates[0])

            if value == '3':
                b = tk.Button(self.gaming_grid, text='3', relief=FLAT, background="#ccc", width=2, height=1, fg='#2647EA')
                b.grid(column=coordinates[1], row=coordinates[0])

            if value == '4':
                b = tk.Button(self.gaming_grid, text='4', relief=FLAT, background="#ccc", width=2, height=1, fg='#2647EA')
                b.grid(column=coordinates[1], row=coordinates[0])

            if value == '5':
                b = tk.Button(self.gaming_grid, text='5', relief=FLAT, background="#ccc", width=2, height=1, fg='#2647EA')
                b.grid(column=coordinates[1], row=coordinates[0])

            if value == '6':
                b = tk.Button(self.gaming_grid, text='6', relief=FLAT, background="#ccc", width=2, height=1, fg='#2647EA')
                b.grid(column=coordinates[1], row=coordinates[0])

            if value == '7':
                b = tk.Button(self.gaming_grid, text='7', relief=FLAT, background="#ccc", width=2, height=1, fg='#2647EA')
                b.grid(column=coordinates[1], row=coordinates[0])

            if value == '8':
                b = tk.Button(self.gaming_grid, text='8', relief=FLAT, background="#ccc", width=2, height=1, fg='#2647EA')
                b.grid(column=coordinates[1], row=coordinates[0])

            if value == '§' or value == '*§*':

                #img = ImageTk.PhotoImage(file="flag.png")
                b = tk.Button(self.gaming_grid, text='§', relief=RAISED, background="#ccc", width=2, height=1)#, image = img)
                b.grid(column=coordinates[1], row=coordinates[0])
                b.bind('<Button-3>', self.RightClick)

            if value == '?' or value == '*':

                b = tk.Button(self.gaming_grid, text=' ', command=partial(self.LeftClick, coordinates), #relief=RAISED,
                              background="#ccc", width=2, height=1)
                b.grid(column=coordinates[1], row=coordinates[0])
                b.bind('<Button-3>', self.RightClick)

            if value == '?':
                self.move_left += 1

        if self.move_left == 0:
            self.game.PrintWin()

MainApp()
