import functools
import sys
from random import seed, randint

from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from InitGame import InitGame
from NeuralNetwork import CallNN, HideBoard
import time

from PyQt5.uic.properties import QtCore

"""
self.setStyleSheet("margin: 1px; padding: 10px;\
                   background-color: rgba(255,255,0,255);\
                   color: rgba(0,0,0,255);\
                   border-style: solid;\
                   border-radius: 4px;\
                   border-width: 3px;\
                   border-color: rgba(0,0,0,255);")

font_button.setFamily("Corbel")
font_button.setPointSize(10)
font_button.setWeight(100)
self.my_button.setText("Blue")
self.my_button.setFixedWidth(72)
self.my_button.setFont(font_button)
"""


BUTTON_STYLE = {
    '??':   "background-color: rgb(150,150,150);\
            border-style: solid;\
            border-radius: 1px;\
            border-width: 1px;\
            border-color: rgb(100,100,100);",

    '0':    "background-color: rgb(200,200,200);\
            border-style: solid;\
            border-radius: 1px;\
            border-width: 1px;\
            border-color: rgb(100,100,100);",

    '1':    "background-color: rgb(200,200,200);\
            color: rgb(30,150,44);\
            font-size:15px;\
            border-style: solid;\
            border-radius: 1px;\
            border-width: 1px;\
            border-color: rgb(100,100,100);",

    '2':    "background-color: rgb(200,200,200);\
            color: rgb(250, 130, 30);\
            font-size:15px;\
            border-style: solid;\
            border-radius: 1px;\
            border-width: 1px;\
            border-color: rgb(100,100,100);",

    '3':    "background-color: rgb(200,200,200);\
            color: rgb(200, 0, 0);\
            font-size:15px;\
            border-style: solid;\
            border-radius: 1px;\
            border-width: 1px;\
            border-color: rgb(100,100,100);",

    '4':    "background-color: rgb(200,200,200);\
            color: rgb(100, 100, 100);\
            font-size:15px;\
            border-style: solid;\
            border-radius: 1px;\
            border-width: 1px;\
            border-color: rgb(100,100,100);",

    '5':    "background-color: rgb(200,200,200);\
            color: rgb(100, 100, 100);\
            font-size:15px;\
            border-style: solid;\
            border-radius: 1px;\
            border-width: 1px;\
            border-color: rgb(100,100,100);",

    '6':    "background-color: rgb(200,200,200);\
            color: rgb(100, 100, 100);\
            font-size:15px;\
            border-style: solid;\
            border-radius: 1px;\
            border-width: 1px;\
            border-color: rgb(100,100,100);",

    '7':    "background-color: rgb(200,200,200);\
            color: rgb(100, 100, 100);\
            font-size:15px;\
            border-style: solid;\
            border-radius: 1px;\
            border-width: 1px;\
            border-color: rgb(100,100,100);",

    '8':    "background-color: rgb(200,200,200);\
            color: rgb(100, 100, 100);\
            font-size:15px;\
            border-style: solid;\
            border-radius: 1px;\
            border-width: 1px;\
            border-color: rgb(100,100,100);",

    '*':    "background-color: rgb(200,200,200);\
            color: rgb(100, 100, 100);\
            border-style: solid;\
            border-radius: 1px;\
            border-width: 1px;\
            border-color: rgb(100,100,100);",
}

class MyPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        button = QPushButton('Exit')
        # button.clicked.connect(functools.partial(sys.exit))
        self.setCentralWidget(button)


class Window(QWidget):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)

        self.xSize = 8
        self.ySize = 8
        self.nbBombs = 10

        self.Game = InitGame(self.xSize, self.ySize, self.nbBombs)
        self.InitWindow()

    def InitWindow(self):

        """
        Initialize the main window grid
        """
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        """
        Initialize the top part of the grid
        """
        self.RightWidget = QWidget()
        #Adds widget position 0, 0, expand on the full row
        grid_layout.addWidget(self.RightWidget, 0, 0, 1, -1)
        self.GridLayout = QGridLayout(self.RightWidget)
        self.GridLayout.setSpacing(0)

        label = QLabel("<b> Champi's Minesweeper <\b>")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Helvetica [Cronyx]", 12))
        self.GridLayout.addWidget(label, 0, 1)
        #self.GridLayout.addWidget(QPushButton(), 1, 2)
        #self.GridLayout.addWidget(QPushButton(), 0, 3)

        """
        Initialize the left part of the grid
        """
        self.LeftWidget = QWidget()
        grid_layout.addWidget(self.LeftWidget, 1, 0, 1, 1)
        #Design the left part
        lay = QVBoxLayout(self.LeftWidget)
        button = QPushButton('Autoplay')
        button.clicked.connect(functools.partial(self.AutomatedGame))
        lay.addWidget(button)

        button = QPushButton('Again Again')
        button.clicked.connect(functools.partial(self.NewGame))
        lay.addWidget(button)

        """
        Initialize the right part of the grid
        """
        self.RightWidget = QWidget()
        grid_layout.addWidget(self.RightWidget, 1, 1, 1, 3)
        self.GridLayout = QGridLayout(self.RightWidget)
        self.GridLayout.setSpacing(0)

        for x in range(0, 8):
            for y in range(0, 8):
                button = QPushButton()
                button.setFixedSize(QSize(30, 30))
                button.clicked.connect(functools.partial(self.LeftClick, [x, y]))
                self.GridLayout.addWidget(button, x, y)

        #QtGui.QGuiApplication.processEvents()

    def InitWindow2(self): #Deprecated

        self.setWindowTitle('Main App')
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        lay = QGridLayout(central_widget)
        ##lay.setColumnStretch(0, 2)
        #lay.setRowStretch(0, 2)

        # Design the right part Add RightWidget coordinate 0, 1
        self.RightWidget = QWidget()
        lay.addWidget(self.RightWidget, 0, 0, 1, -1)
        self.GridLayout = QGridLayout(self.RightWidget)
        self.GridLayout.setSpacing(0)

        for x in range(0, self.xSize):
            for y in range(0, self.ySize):
                button = QPushButton()
                #button.setStyleSheet(BUTTON_STYLE['?'])
                #button.installEventFilter(button)
                button.clicked.connect(functools.partial(self.LeftClick, [x, y]))
                button.setFixedSize(QSize(30, 30))
                self.GridLayout.addWidget(button, x, y)


        self.LeftWidget = QWidget()
        lay.addWidget(self.LeftWidget, 1, 0)
        #Design the left part
        lay = QVBoxLayout(self.LeftWidget)
        button = QPushButton('Autoplay')
        button.clicked.connect(functools.partial(self.AutomatedGame))
        lay.addWidget(button)


        #button = QPushButton('1-3')
        #lay.addWidget(button, 0, 0, 1, -1)

    def NewGame(self):
        self.Game = InitGame(self.xSize, self.ySize, self.nbBombs)
        self.InitWindow()
        self.UpdateBoardGraphic(StopPlaying=False)
        QtGui.QGuiApplication.processEvents()

    def LeftClick(self, coordinates):

        x = coordinates[0]
        y = coordinates[1]
        StopPlaying = self.Game.UpdateBoard(x, y)
        self.UpdateBoardGraphic(StopPlaying)

        return StopPlaying

    def RightClick(self, event):
        w = event.widget.grid_info()
        x = w['row']
        y = w['column']
        self.Game.Flag(x, y)

    def UpdateBoardGraphic(self, StopPlaying):

        self.MoveLeft = 0
        if StopPlaying is True:
            for coordinates in self.Game.Grid:
                value = str(self.Game.GameBoard[coordinates[0]][coordinates[1]])
                x = coordinates[0]
                y = coordinates[1]
                if value in ['*$', '*']:
                    button = QPushButton()
                    button.setIcon(QIcon(QPixmap("bomb.jpg")))
                    button.setFixedSize(QSize(30, 30))
                    self.GridLayout.addWidget(button, x, y)
            QtGui.QGuiApplication.processEvents()
            self.PrintLost()

        if StopPlaying is False:
            #self.Game.PrintGameBoard()

            for coordinates in self.Game.Grid:

                value = str(self.Game.GameBoard[coordinates[0]][coordinates[1]])
                x = coordinates[0]
                y = coordinates[1]
                if value == '0':
                    button = QPushButton()
                    button.setStyleSheet(BUTTON_STYLE[value])
                    button.setFixedSize(QSize(30, 30))
                    self.GridLayout.addWidget(button, x, y)

                if value in ['1', '2', '3', '4', '5', '6', '7', '8']:
                    button = QPushButton(value)
                    button.installEventFilter(QPushButton())
                    button.setStyleSheet(BUTTON_STYLE[value])
                    button.setFixedSize(QSize(30, 30))
                    self.GridLayout.addWidget(button, x, y)

                if value in ['?', '*']:
                    button = QPushButton()
                    #button.setStyleSheet(BUTTON_STYLE['?'])
                    button.clicked.connect(functools.partial(self.LeftClick, [x, y]))
                    button.installEventFilter(QPushButton())
                    button.setFixedSize(QSize(30, 30))
                    self.GridLayout.addWidget(button, x, y)

                if value in ['*$', '*']:
                    button = QPushButton()
                    button.setFixedSize(QSize(30, 30))
                    button.clicked.connect(functools.partial(self.LeftClick, [x, y]))
                    self.GridLayout.addWidget(button, x, y)

                if value == '?':
                    self.MoveLeft += 1

            if self.MoveLeft == 0:
                self.PrintWin()

    def PrintLost(self):
        print('Lost')
        self.Game = InitGame(self.xSize, self.ySize, self.nbBombs)
        #self.InitWindow()
        #self.UpdateBoardGraphic(StopPlaying = False)


    def PrintWin(self):
        print('Win')

    def AutomatedGame(self):
        StopPlaying = False
        self.UpdateBoardGraphic(StopPlaying)

        while StopPlaying is False:
            x, y = CallNN(HideBoard(self.Game.GameBoard))
            StopPlaying = self.LeftClick([x, y])
            QtGui.QGuiApplication.processEvents()
            time.sleep(0.5)

        self.Game = InitGame(self.xSize, self.ySize, self.nbBombs)

        self.AutomatedGame()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
