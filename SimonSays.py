# By: Kevin Kelmonas 11/4/2023
# Project for CS335
# 'Simon Says' Game

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QGridLayout, QLabel, QComboBox # 4 different layouts, ...
from PyQt6.QtCore import Qt, QTimer, QEventLoop
import time
import sys # For access to command line arguments
import random # for random color selector
import numpy as np # Alternative: import Array as arr

class StartMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Game Menu")

        # creates button
        self.button_Simon = QPushButton("Simon Says")
        self.button_Matcher = QPushButton("Color Matcher")
        self.button_IceCream = QPushButton("Ice Cream Shop")
    
        # sets size of button
        self.button_Simon.setFixedSize(300, 100)
        self.button_Matcher.setFixedSize(300, 100)
        self.button_IceCream.setFixedSize(300, 100)

        # assigns function to button click action (use of lambda because ...)
        self.button_Simon.clicked.connect(lambda: self.start_Simon())
        self.button_Matcher.clicked.connect(lambda: self.start_Matcher())
        self.button_IceCream.clicked.connect(lambda: self.start_Simon())

        # creates title
        self.title = QLabel("Game Menu")
        font = self.title.font()  # get the current font
        font.setPointSize(24) # change font
        self.title.setFont(font)  # set the new font
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter) # center title within layout

        self.layout = QGridLayout()
        self.layout.setSpacing(40)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter) # center layout
        self.layout.addWidget(self.title, 0, 1)  # add title to the grid layout
        self.layout.addWidget(self.button_Simon, 1, 0)
        self.layout.addWidget(self.button_Matcher, 1 , 1)
        self.layout.addWidget(self.button_IceCream, 1, 2)

        self.widget = QWidget()
        self.widget.setLayout(self.layout) # apply button layout to widget
        self.setCentralWidget(self.widget) # center of screen


    def start_Simon(self):

        # Create window for matching game.
        self.game_window = Simon_Says()
        self.game_window.show()

        # Close the current window.
        self.close()

    def start_Matcher(self):

        # Create window for matching game.
        self.game_window = DifficultySelection()
        self.game_window.show()

        # Close the current window.
        self.close()

    def start_IceCream(self):

        # Create window for matching game.
        self.game_window = Simon_Says()
        self.game_window.show()

        # Close the current window.
        self.self.close()

class Simon_Says(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Simon Says")

        self.Array = np.array([]) # stores sequence of colors, appends new color every turn
        self.click_count = 0 # tracks number of moves left during turn and iterates through color sequence

        # creates button
        self.button_red = QPushButton("Red")
        self.button_blue = QPushButton("Blue")
        self.button_green = QPushButton("Green")
        self.button_yellow = QPushButton("Yellow")
        self.button_start = QPushButton("Start Game")
        self.button_exit = QPushButton("Exit Game")

        # sets size of button
        self.button_red.setFixedSize(100, 100)
        self.button_blue.setFixedSize(100, 100)
        self.button_green.setFixedSize(100, 100)
        self.button_yellow.setFixedSize(100, 100) 
        self.button_start.setFixedSize(100, 100) 
        self.button_exit.setFixedSize(100, 100)

        # sets color of button
        self.button_red.setStyleSheet('background-color: red')
        self.button_blue.setStyleSheet('background-color: blue')
        self.button_green.setStyleSheet('background-color: green')
        self.button_yellow.setStyleSheet('background-color: yellow')
        #self.button_start.setStyleSheet('background-color: black; color: white')
        #self.button_exit.setStyleSheet('background-color: black; color: white')

        # assigns function to button click action (use of lambda because ...)
        self.button_red.clicked.connect(lambda: self.makeGuess('Red'))
        self.button_blue.clicked.connect(lambda: self.makeGuess('Blue'))
        self.button_green.clicked.connect(lambda: self.makeGuess('Green'))
        self.button_yellow.clicked.connect(lambda: self.makeGuess('Yellow'))
        self.button_start.clicked.connect(self.StartGame) # when clicked, creates loop until true becomes false
        self.button_exit.clicked.connect(lambda: self.exitGame())

        # uses Qt to format button layout
        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.layout.addWidget(self.button_red, 0, 0)
        self.layout.addWidget(self.button_blue, 0 , 1)
        self.layout.addWidget(self.button_green, 1, 0)
        self.layout.addWidget(self.button_yellow, 1, 1)
        self.layout.addWidget(self.button_start, 2, 0)
        self.layout.addWidget(self.button_exit, 2, 1)

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

        self.i = 0
        while self.i < len(self.Array):

            print(f'Simon Says: {self.Array[self.i]}') # make it highlight button repeated for 1 second then revert back to normal color

            if self.Array[self.i] == 'Red':
                self.button_red.setStyleSheet("background-color: white")
                QTimer.singleShot(1500, lambda: self.button_red.setStyleSheet("background-color: red"))

            elif self.Array[self.i] == 'Blue':
                self.button_blue.setStyleSheet("background-color: white")
                QTimer.singleShot(1500, lambda: self.button_blue.setStyleSheet("background-color: blue"))

            elif self.Array[self.i] == 'Green':
                self.button_green.setStyleSheet("background-color: white")
                QTimer.singleShot(1500, lambda: self.button_green.setStyleSheet("background-color: green"))

            if self.Array[self.i] == 'Yellow':
                self.button_yellow.setStyleSheet("background-color: white")
                QTimer.singleShot(1500, lambda: self.button_yellow.setStyleSheet("background-color: yellow"))

            self.i += 1

            loop = QEventLoop()
            QTimer.singleShot(2000, loop.quit) 
            loop.exec()


    def StartGame(self): # starts turn, each turn a new color is added to sequence making game more challenging
       print("-------------------------") # games turn (output)
       print("~Game~")

       self.AddColor()
       self.Repeat() 
       self.game_active = True # starts game loop until you lose
       self.click_count = 0

       print("-------------------------") # your turn (input + output)
       print("~You~")

    def exitGame(self):

        # Create window for matching game.
        self.game_window = StartMenu()
        self.game_window.show()

        # Close the current window.
        self.close()


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
        game_window = MatchingGame(selected_difficulty)
        game_window.show()

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

        # Create a label for the guess count.
        self.guess_count_label = QLabel()
        layout.addWidget(self.guess_count_label, self.grid_size + 3, 0, 1, self.grid_size)
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
           
# Start Game, Add 1 button to array, repeat array in order, user makes guesses, if all right signal and repeat, if wrong along way then end game


app = QApplication(sys.argv) # Python list containing the command line arguments passed to the application
# app = QApplication([]) # for no command line arguments

window = StartMenu() # Create a Qt widget, which will be our window.
window.show()
app.exec() # Start the event loop
