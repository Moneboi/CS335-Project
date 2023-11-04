# By: Kevin Kelmonas 11/4/2023
# Project for CS335
# 'Simon Says' Game

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QGridLayout # 4 different layouts, ...
# from PyQt6.QtGui import # ...
# from PyQt6.QtCore import # QSize, Qt, ...
import sys # For access to command line arguments
import random # for random color selector
import numpy as np # Alternative: import Array as arr

class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Project 335")

        self.Array = np.array([]) # stores sequence of colors, appends new color every turn
        self.click_count = 0 # tracks number of moves left during turn and iterates through color sequence

        # creates button
        self.button_red = QPushButton("Red")
        self.button_blue = QPushButton("Blue")
        self.button_green = QPushButton("Green")
        self.button_yellow = QPushButton("Yellow")
        self.button_start = QPushButton("Start Game")

        # sets size of button
        self.button_red.setFixedSize(100, 100)
        self.button_blue.setFixedSize(100, 100)
        self.button_green.setFixedSize(100, 100)
        self.button_yellow.setFixedSize(100, 100) 
        self.button_start.setFixedSize(100, 100) 

        # sets color of button
        self.button_red.setStyleSheet('background-color: red')
        self.button_blue.setStyleSheet('background-color: blue')
        self.button_green.setStyleSheet('background-color: green')
        self.button_yellow.setStyleSheet('background-color: yellow')
        self.button_start.setStyleSheet('background-color: black; color: white')

        # assigns function to button click action (use of lambda because ...)
        self.button_red.clicked.connect(lambda: self.makeGuess('Red'))
        self.button_blue.clicked.connect(lambda: self.makeGuess('Blue'))
        self.button_green.clicked.connect(lambda: self.makeGuess('Green'))
        self.button_yellow.clicked.connect(lambda: self.makeGuess('Yellow'))
        self.button_start.clicked.connect(self.StartGame) # when clicked, creates loop until true becomes false

        # uses Qt to format button layout
        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.layout.addWidget(self.button_red, 0, 0)
        self.layout.addWidget(self.button_blue, 0 , 1)
        self.layout.addWidget(self.button_green, 1, 0)
        self.layout.addWidget(self.button_yellow, 1, 1)
        self.layout.addWidget(self.button_start, 2, 0)

        self.widget = QWidget()
        self.widget.setLayout(self.layout) # apply button layout to widget
        self.setCentralWidget(self.widget) # center of screen

        self.game_active = False # When 'Start' clicked, game loops while true, necessary to have turns (add color)


    def makeGuess(self, color): # assgigned to button clicks, avaliable only after starting game, registers a singular color clicked

        # if: game loop is true, and: the button color clicked is equal to the current button in the sequence, and: the color sequence for the user's current turn is not completed (clicks by user remain)
        if self.game_active and color == self.Array[self.click_count] and self.click_count < self.Array.size: 
            self.click_count += 1 # iterate to the next spot in the array, update clicks remaining, ready for next click by user
            print(f'colors left to guess: {self.Array.size - self.click_count}') 
            if self.click_count == self.Array.size: # if after updating clicks remaining, 0 remain, then reloop start game and 
                print(f'adding color')
                self.StartGame() # proceeds to next turn (adds a color to the sequence)
        else:
            print(f'you lose')
            self.click_count = 0 # resets colors to be guessed
            self.Array = np.array([]) # resets array
            self.game_active = False # ends game loop


    def AddColor(self): # add random color to sequence
       random_number = random.choices(["Red", "Blue", "Green", "Yellow"], k=1) # randomly selects 1 of 4 colors
       self.Array = np.append(self.Array, random_number) # adds color to sequence 
       # print(self.Array)

    # Task: in GUI make it highlight the button repeated for 1 second then revert it back to normal color and go on to the next
    def Repeat(self): # prints color sequence
        for i in range(self.Array.size):
            print(f'Simon Says: {self.Array[i]}') # make it highlight button repeated for 1 second then revert back to normal color


    def StartGame(self): # starts turn, each turn a new color is added to sequence making game more challenging
       print("-------------------------") # games turn (output)
       print("~Game~")

       self.AddColor()
       self.Repeat() 
       self.game_active = True # starts game loop until you lose
       self.click_count = 0

       print("-------------------------") # your turn (input + output)
       print("~You~")

           
# Start Game, Add 1 button to array, repeat array in order, user makes guesses, if all right signal and repeat, if wrong along way then end game


app = QApplication(sys.argv) # Python list containing the command line arguments passed to the application
# app = QApplication([]) # for no command line arguments

window = MyWindow() # Create a Qt widget, which will be our window.
window.show()
app.exec() # Start the event loop
