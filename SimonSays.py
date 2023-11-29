# By: Kevin Kelmonas 11/4/2023
# Project for CS335
# 'Simon Says' Game

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QGridLayout, QLabel, QComboBox # 4 different layouts, ...
from PyQt6.QtCore import Qt, QTimer, QEventLoop
from PyQt6.QtGui import QPalette, QBrush, QImage
import sys # For access to command line arguments
import random # for random color selector
import numpy as np # Alternative: import Array as arr
from IceCreamGUI import *
from IceCreamOrder import *

#---------------------------------------------------------------------------------------------------------
# Code For Main Menu
#---------------------------------------------------------------------------------------------------------

class StartMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Game Menu") # set title of widget
        self.setFixedSize(1000,800) # set size of widget

        # Set Image as background for menu
        palette = QPalette()
        image = QImage("MenuBackground.png")  # Use image as background
        image = image.scaled(1000, 800)  # Scale image to fit the window
        palette.setBrush(QPalette.ColorRole.Window, QBrush(image)) 
        self.setPalette(palette)

        # creates button
        self.button_Simon = QPushButton("Simon Says")
        self.button_Matcher = QPushButton("Color Matcher")
        self.button_IceCream = QPushButton("Ice Cream Shop")
    
        # sets size of button
        self.button_Simon.setFixedSize(250, 100)
        self.button_Matcher.setFixedSize(250, 100)
        self.button_IceCream.setFixedSize(250, 100)

        # assigns function to button click action (use of lambda because ...)
        self.button_Simon.clicked.connect(lambda: self.start_Simon())
        self.button_Matcher.clicked.connect(lambda: self.start_Matcher())
        self.button_IceCream.clicked.connect(lambda: self.start_IceCream())

        # sets background, border look, and font specifics of button and text within it
        self.button_Simon.setStyleSheet("border-image: url(MainMenuButton.png); font-family: Cooper Black; font-size: 30px; font-weight: bold; border-radius: 15px;")
        self.button_Matcher.setStyleSheet("border-image: url(MainMenuButton.png); font-family: Cooper Black; font-size: 30px; font-weight: bold; border-radius: 15px;")
        self.button_IceCream.setStyleSheet("border-image: url(MainMenuButton.png); font-family: Cooper Black; font-size: 30px; font-weight: bold; border-radius: 15px;")

        # Create a QLabel and set the image as its display
        self.title = QLabel(self) 
        self.titlePixmap = QPixmap('GameMenuTitle.png')
        self.title.setFixedSize(900, 125)

        self.title.setPixmap(self.titlePixmap)
        self.title.setScaledContents(True)

        # Create a QHBoxLayout for the buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button_Simon)
        button_layout.addWidget(self.button_Matcher)
        button_layout.addWidget(self.button_IceCream)

        # Create a Grid layout in the center of the screen with title (0,1) and buttons (1,1)
        self.layout = QGridLayout()
        self.layout.setSpacing(25)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter) # center layout
        self.layout.addWidget(self.title, 0, 1)  # add title to the grid layout
        self.layout.addLayout(button_layout, 1, 1)  # add button layout to the grid layout

        self.widget = QWidget() 
        self.widget.setLayout(self.layout) # apply button layout to widget
        self.setCentralWidget(self.widget) # center of screen


    def start_Simon(self):

        # Create window for matching game.
        self.game_window = Simon_Says()
        # Sets dimensions of widget
        self.game_window.setFixedSize(1000,800) 
        # Show the new window
        self.game_window.show()
        # Close the current window.
        self.close()

    def start_Matcher(self):

        # Create window for matching game.
        self.game_window = DifficultySelection()
        # Sets dimensions of widget
        self.game_window.setFixedSize(250,200)
        # Show the new window
        self.game_window.show()
        # Close the current window.
        self.close()

    def start_IceCream(self):

        # Create IceCreamGUI instance
        self.game_window = IceCreamGUI() 
        # Show the new window
        self.game_window.show()
        # Close the current window
        self.close()

#---------------------------------------------------------------------------------------------------------
# Code For Simon Says Game
#---------------------------------------------------------------------------------------------------------

# Game Over pop up window (displays message, score, and close option)
class GameOver(QDialog):
        
        def __init__(self, score = None): # score paramater is passed in from Simon_Says() and is players score at the point the game ended
            super().__init__()

            # play mario song
            data, fs = sf.read('marioSimon.mp3')
            sd.play(data,fs, loop = False)

            self.setWindowTitle("Result") # Set title
            self.resize(400, 200)  # Set the size of the window
            self.setStyleSheet("background-color: #1a1a1a;")  # Set the background color

            self.label1 = QLabel("Game Over") # display message
            self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the label
            self.label1.setStyleSheet("font-size: 40px; color: red") # set size and color

            self.label2 = QLabel(f"You Scored: {score}") # display message with players score
            self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the label
            self.label2.setStyleSheet("font-size: 20px; color: white;") # set size and color

            self.button = QPushButton("Close") # create close window button
            self.button.clicked.connect(self.close) # assigns function to close window when clicked
            self.button.setStyleSheet("background-color: grey; color: white") # sets colors

            # displays every element vertically
            layout = QVBoxLayout(self)
            layout.addWidget(self.label1)
            layout.addWidget(self.label2)
            layout.addWidget(self.button)

# Code for Simon Says Game
class Simon_Says(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Simon Says")
        self.Array = np.array([]) # stores sequence of colors, appends new color every turn
        self.click_count = 0 # tracks number of moves left during turn and iterates through color sequence
        self.score = -1 # tracks players current score

        # creates button
        self.button_red = QPushButton()
        self.button_blue = QPushButton()
        self.button_green = QPushButton()
        self.button_yellow = QPushButton()
        self.button_start = QPushButton("Start Game")
        self.button_exit = QPushButton("Main Menu")

        # sets size of button
        self.button_red.setFixedSize(200, 200)
        self.button_blue.setFixedSize(200, 200)
        self.button_green.setFixedSize(200, 200)
        self.button_yellow.setFixedSize(200, 200) 
        self.button_start.setFixedSize(200, 75) 
        self.button_exit.setFixedSize(200, 75)

        # sets color of button
        self.button_red.setStyleSheet('background-color: red; border-color: black; border-style: outset; border-width: 3px; border-top-left-radius: 200px;')
        self.button_blue.setStyleSheet('background-color: blue; border-color: black; border-style: outset; border-width: 3px; border-top-right-radius: 200px;')
        self.button_green.setStyleSheet('background-color: green; border-color: black; border-style: outset; border-width: 3px; border-bottom-left-radius: 200px;')
        self.button_yellow.setStyleSheet('background-color: yellow; border-color: black; border-style: outset; border-width: 3px; border-bottom-right-radius: 200px;')
        self.button_start.setStyleSheet('background-color: grey; color: white; font-family: Broadway; font-size: 25px; border-radius: 15px;')
        self.button_exit.setStyleSheet('background-color: grey; color: white; font-family: Broadway; font-size: 25px; border-radius: 15px;')

        # assigns function to button click action (use of lambda because ...)
        self.button_red.clicked.connect(lambda: self.makeGuess('Red'))
        self.button_blue.clicked.connect(lambda: self.makeGuess('Blue'))
        self.button_green.clicked.connect(lambda: self.makeGuess('Green'))
        self.button_yellow.clicked.connect(lambda: self.makeGuess('Yellow'))
        self.button_start.clicked.connect(self.StartGame) # when clicked, creates loop until true becomes false
        self.button_exit.clicked.connect(lambda: self.exitGame())

        # First row, Title at top of simon says
        self.simon_label = QLabel("Simon Says")
        self.simon_label.setStyleSheet('font-size: 65px; font-family: Broadway; color: white;')
        # Second row, Red and Blue buttons
        self.top_layout = QHBoxLayout()
        self.top_layout.addWidget(self.button_red)
        self.top_layout.addWidget(self.button_blue)
        # Third row, Green and Yellow buttons
        self.bot_layout = QHBoxLayout()
        self.bot_layout.addWidget(self.button_green)
        self.bot_layout.addWidget(self.button_yellow)
        # Fourth row, Start and Exit buttons
        self.opt_layout = QHBoxLayout()
        self.opt_layout.addWidget(self.button_start)
        self.opt_layout.addWidget(self.button_exit)
        # Fith row, Current score
        self.score_label = QLabel(f"Score: {self.click_count}")
        self.score_label.setStyleSheet('font-size: 20px; font-family: Broadway; color: white;')
        # Center and align each row vertically
        self.all_layout = QGridLayout()
        self.all_layout.setAlignment(Qt.AlignmentFlag.AlignCenter) # center layout
        self.all_layout.addWidget(self.simon_label, 0, 1)
        self.all_layout.addLayout(self.top_layout, 1, 1)
        self.all_layout.addLayout(self.bot_layout, 2, 1)
        self.all_layout.addWidget(self.score_label, 3, 1)
        self.all_layout.addLayout(self.opt_layout, 4, 1)
        # Add to Widget
        self.widget = QWidget()
        self.widget.setStyleSheet("background-color: #1a1a1a;") # Set background color of widget
        self.widget.setLayout(self.all_layout) # apply button layout to widget
        self.setCentralWidget(self.widget) # center of screen

        self.game_active = False # When 'Start' clicked, game loops while true, necessary to have turns (each turn adds color)

    def makeGuess(self, color): # assgigned to button clicks, avaliable only after starting game, registers a singular color clicked

        # if: game loop is true, and: the button color clicked is equal to the current button in the sequence, and: the color sequence for the user's current turn is not completed (clicks by user remain)
        if self.game_active and color == self.Array[self.click_count] and self.click_count < self.Array.size: 
            self.click_count += 1 # Iterate to the next spot in the array, update clicks remaining, ready for next click by user
            print(f'colors left to guess: {self.Array.size - self.click_count}') # prints in terminal
            if self.click_count == self.Array.size: # if after updating clicks remaining, 0 remain, then reloop start game and 
                print(f'adding color') # prints in terminal
                self.StartGame() # proceeds to next turn (adds a color to the sequence)
        else:
            dialog = GameOver(self.score) # Calls game over popup
            dialog.exec() # runs popup
            print(f'Game Over') # prints in terminal
            self.click_count = 0 # resets colors to be guessed
            self.score = -1 # resets players score
            self.Array = np.array([]) # resets array containing sequence of colors needed to be guessed
            self.game_active = False # ends game loop

    def AddColor(self): # add random color to sequence
       random_number = random.choices(["Red", "Blue", "Green", "Yellow"], k=1) # randomly selects 1 of 4 colors
       self.Array = np.append(self.Array, random_number) # adds color to sequence 
       # print(self.Array)

    # Task: in GUI make it highlight the button repeated for a second then revert it back to normal color and go on to the next index
    def Repeat(self): # prints color sequence

        self.i = 0 # increments until arrays entire sequence has been displayed (dependent on players current score)
        while self.i < len(self.Array):

            data, fs = sf.read('buttonSimon2.wav') # calls audio file 
            print(f'Simon Says: {self.Array[self.i]}') # make it highlight button repeated for 1 second then revert back to normal color

            if self.Array[self.i] == 'Red': # if this color is current index in sequence
                sd.play(data,fs, loop = False) # plays audio file
                self.button_red.setStyleSheet('background-color: red; border-color: white; border-style: outset; border-width: 3px; border-top-left-radius: 200px;') # highlights current color in sequence
                QTimer.singleShot(1500, lambda: self.button_red.setStyleSheet('background-color: red; border-color: black; border-style: outset; border-width: 3px; border-top-left-radius: 200px;')) # revert to original look

            elif self.Array[self.i] == 'Blue': # if this color is current index in sequence
                sd.play(data,fs, loop = False) # plays audio file
                self.button_blue.setStyleSheet('background-color: blue; border-color: white; border-style: outset; border-width: 3px; border-top-right-radius: 200px;') # highlights current color in sequence
                QTimer.singleShot(1500, lambda: self.button_blue.setStyleSheet('background-color: blue; border-color: black; border-style: outset; border-width: 3px; border-top-right-radius: 200px;')) # revert to original look

            elif self.Array[self.i] == 'Green': # if this color is current index in sequence
                sd.play(data,fs, loop = False) # plays audio file
                self.button_green.setStyleSheet('background-color: green; border-color: white; border-style: outset; border-width: 3px; border-bottom-left-radius: 200px;') # highlights current color in sequence
                QTimer.singleShot(1500, lambda: self.button_green.setStyleSheet('background-color: green; border-color: black; border-style: outset; border-width: 3px; border-bottom-left-radius: 200px;')) # revert to original look

            if self.Array[self.i] == 'Yellow': # if this color is current index in sequence
                sd.play(data,fs, loop = False) # plays audio file
                self.button_yellow.setStyleSheet('background-color: yellow; border-color: white; border-style: outset; border-width: 3px; border-bottom-right-radius: 200px;') # highlights current color in sequence
                QTimer.singleShot(1500, lambda: self.button_yellow.setStyleSheet('background-color: yellow; border-color: black; border-style: outset; border-width: 3px; border-bottom-right-radius: 200px;')) # revert to original look

            self.i += 1 # iterates to next color in sequence

            loop = QEventLoop()
            QTimer.singleShot(2000, loop.quit) 
            loop.exec()


    def StartGame(self): # starts turn, each turn a new color is added to sequence making game more challenging
       print("-------------------------") # games turn (output)
       print("~Game~")
       self.score += 1 # Adds to users score
       self.score_label.setText(f"Score: {self.score}") # Updates score label based on current score
       self.AddColor() # Adds new color to sequence
       self.Repeat() # Repeats the colors back to user
       self.game_active = True # starts game loop until you lose, essentially allows user to guess until wrong guess is made
       self.click_count = 0 # resets click count, tracks number of clicks made by user as they are guessing until max required guesses reached
       print("-------------------------") # your turn (input + output)

    def exitGame(self):

        # Create window for matching game.
        self.game_window = StartMenu()
        self.game_window.show()

        # Close the current window.
        self.close()

#---------------------------------------------------------------------------------------------------------
# Code For Matching Game
#---------------------------------------------------------------------------------------------------------

# Inital window for difficulty selection.
class DifficultySelection(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title.
        self.setWindowTitle("Difficulty Selection")

        # Set the grid layout.
        self.layout = QGridLayout()

        # Create difficulty selection box.
        self.difficulty_label = QLabel("Select Difficulty:")
        self.layout.addWidget(self.difficulty_label, 0, 0, 1, 2)

        # Create options for difficulty.
        self.difficulty_combo = QComboBox()
        self.difficulty_combo.addItems(["Easy", "Medium", "Hard"])
        self.layout.addWidget(self.difficulty_combo, 1, 0, 1, 2)

        # Create start game button.
        start_game_button = QPushButton("Start Game")
        start_game_button.clicked.connect(self.start_game)
        self.layout.addWidget(start_game_button, 2, 0, 1, 2)

        # Set layout.
        self.setLayout(self.layout)

    # Definition to open game window.
    def start_game(self):
        # Get selected difficulty.
        selected_difficulty = self.difficulty_combo.currentText()

        # Create window for matching game.
        self.game_window = MatchingGame(selected_difficulty)
        self.game_window.setFixedSize(500,400)
        self.game_window.show()

        # Close the current window.
        self.close()

# Class for the matching game.
class MatchingGame(QWidget):
    def __init__(self, difficulty):
        super().__init__()

        # Matching Game title for window.
        self.setWindowTitle("Matching Game")

        # Initialize lists and size of the game.
        self.color_pairs = []
        self.selected_colors = []
        self.button_size = 50
        self.guess_count = 0

        # Default game difficulty.
        self.difficulty = difficulty

        # Set grid size.
        match self.difficulty:
            case "Easy":
                self.grid_size = 2
            case "Hard":
                self.grid_size = 6
            case _:
                self.grid_size = 4

        # Potential colors for the matching game.
        self.potential_colors = ['red', 'blue', 'green', 'yellow', 'lime', 'orange', 'cyan', 'magenta', 'khaki', 'silver', 'pink', 'beige', 'olive', 'chocolate', 'salmon', 'brown', 'indigo', 'black']
        self.colors = []

        # Choose colors for the grid size.
        for i in range(int((self.grid_size * self.grid_size) / 2)):
            self.colors.append(self.potential_colors[i])

        # Lists for buttons.
        self.buttons = []
        self.selected_buttons = []

        # Run setup UI.
        self.setup_ui()

    # Setup UI function.
    def setup_ui(self):
        # Layout for the game.
        layout = QGridLayout()

        # Create buttons and connect them to the slot.
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                button = QPushButton()
                button.setFixedSize(self.button_size, self.button_size)
                layout.addWidget(button, i + 1, j)
                button.clicked.connect(lambda _, row=i, col=j: self.button_clicked(row, col))
                self.buttons.append(button)

        # Create a new game button.
        self.reset_button = QPushButton("Start New Game")
        self.reset_button.clicked.connect(self.new_game)
        layout.addWidget(self.reset_button, self.grid_size + 1, 0, 1, self.grid_size)

        # Create a change difficulty button.
        difficulty_button = QPushButton("Change Difficulty")
        difficulty_button.clicked.connect(self.change_difficulty)
        layout.addWidget(difficulty_button, self.grid_size + 2, 0, 1, self.grid_size)

        # Create a button to go back to Main Menu
        exit_button = QPushButton("Main Menu")
        exit_button.clicked.connect(lambda: self.exitGame()) 
        layout.addWidget(exit_button, self.grid_size + 3, 0, 1, self.grid_size)

        # Create a label for the guess count.
        self.guess_count_label = QLabel()
        layout.addWidget(self.guess_count_label, self.grid_size + 4, 0, 1, self.grid_size)
        self.guess_count_label.setText(f"Guesses: {self.guess_count}")

        # Create a new game.
        self.new_game()

        # Set the layout.
        self.setLayout(layout)

    # For a new game setup.
    def new_game(self):
        # Generate pairs of colors.
        self.color_pairs = self.colors * 2
        random.shuffle(self.color_pairs)

        # Reset the guess count.
        self.guess_count = 0
        self.guess_count_label.setText(f"Guesses: {self.guess_count}")

        # Reset the new game button.
        self.reset_button.setText(f"Start New Game")

        # Assign colors to buttons.
        for button, color in zip(self.buttons, self.color_pairs):
            button.setStyleSheet(f'background-color: {color};')
            # Comment the below line to see colors.
            button.setStyleSheet(f'')
            button.setDisabled(False)

        # Reset the selected buttons and number of pairs matched.
        self.selected_buttons = []
        self.matched_pairs = 0

    def exitGame(self):

        # Create window for matching game.
        self.game_window = StartMenu()
        self.game_window.show()

        # Close the current window.
        self.close()

    # To change the difficulty.
    def change_difficulty(self):

        # Reopen the difficulty selection window.
        self.difficulty_window = DifficultySelection()
        self.difficulty_window.show()

        self.close() # Close the current game window

    # Button click.
    def button_clicked(self, row, col):
        # Reset the colors if two non-matches were selected.
        if len(self.selected_buttons) == 2:
            for button in self.selected_buttons:
                    button.setStyleSheet('')
                    self.selected_buttons = []
                    self.selected_colors = []

        # Get the button at the coordinate.
        button = self.buttons[row * self.grid_size + col]

        # Do not allow a currently selected button to be selected again.
        if button in self.selected_buttons:
            return

        # Reveal the color of the selected button.
        button.setStyleSheet(f'background-color: {self.color_pairs[row * self.grid_size + col]};')

        # Append to the selected colors list for matching.
        self.selected_colors.append(self.color_pairs[row * self.grid_size + col])

        # Show the color of the button.
        button.setStyleSheet(button.styleSheet() + 'border: 2px solid white;')
        self.selected_buttons.append(button)

        # Check for a match when two buttons are selected.
        if len(self.selected_buttons) == 2:
            # Increment the guess counter.
            self.guess_count += 1

            # Update the guess count label.
            self.guess_count_label.setText(f"Guesses: {self.guess_count}")

            # Check for a match.
            self.check_for_match()

    # Check for a match.
    def check_for_match(self):
        # Check if the color of buttons match.
        if self.selected_colors[0] == self.selected_colors[1]:
            # Match found.
            for button in self.selected_buttons:
                button.setDisabled(True)
            # Increase the number of pairs matched.
            self.matched_pairs += 1

            # Reset selected buttons and colors list.
            self.selected_buttons = []
            self.selected_colors = []

            # Check if all pairs are matched.
            if self.matched_pairs == len(self.colors):
                # Display winning text.
                print("Congratulations! You've matched all pairs. Start a new game?")
                self.reset_button.setText(f"Play Again")

#---------------------------------------------------------------------------------------------------------
# Code To Run Main Menu GUI
#---------------------------------------------------------------------------------------------------------

app = QApplication(sys.argv) # Python list containing the command line arguments passed to the application ( for no command line arguments: app = QApplication([]) )
window = StartMenu() # Create a Qt widget, which will be our window.
window.show()
app.exec() # Start the event loop
