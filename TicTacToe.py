from tkinter import *
from tkinter import messagebox
import random

# Function to handle the next player's turn
def next_turn(row, column):
    # Declare 'player' as a global variable
    global player

    # Check if the button at the specified row and column is empty and the game is not won
    if buttons[row][column]['text'] == "" and check_winner() is False:

        # If it's Player 1's turn
        if player == players[0]:
            # Set the button's text to Player 1's symbol (X or O)
            buttons[row][column]['text'] = player

            # Check if the game is still not won
            if check_winner() is False:
                # Switch to Player 2's turn
                player = players[1]
                # Update the label to indicate Player 2's turn
                label.config(text=(players[1] + " turn"))

            # If Player 1 wins
            elif check_winner() is True:
                # Update the label to indicate Player 1's victory
                label.config(text=(players[0] + " wins"))

            # If the game is a tie
            elif check_winner() == "Tie":
                # Update the label to indicate a tie
                label.config(text="Tie!")

        # If it's Player 2's turn
        else:
            # Set the button's text to Player 2's symbol (X or O)
            buttons[row][column]['text'] = player

            # Check if the game is still not won
            if check_winner() is False:
                # Switch to Player 1's turn
                player = players[0]
                # Update the label to indicate Player 1's turn
                label.config(text=(players[0] + " turn"))

            # If Player 2 wins
            elif check_winner() is True:
                # Update the label to indicate Player 2's victory
                label.config(text=(players[1] + " wins"))

            # If the game is a tie
            elif check_winner() == "Tie":
                # Update the label to indicate a tie
                label.config(text="Tie!")

# Function to check if there's a winner
def check_winner():
# row winning conditon
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            # Highlight the winning row in green
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
#column winning condtion
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
             # Highlight the winning column in green
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
#diagonal from top-left to bottom-right
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        # Highlight the winning diagonal in green
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
#diagonal from top-right to bottom-left winning condition
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        # Highlight the winning diagonal in green
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    
# If there are no empty spaces and no winner, the game is a tie
    elif empty_spaces() is False:
        #Highlight all buttons in yellow to indicate a tie
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
# If none of the above conditions are met, the game is still ongoing 
    else:
        return False
    
# Function to check if there are empty spaces on the board
def empty_spaces():
 # Initialize the total number of spaces on the board
    spaces = 9
# Iterate through each cell on the 3x3 game board
    for row in range(3):
        for column in range(3):
        # If the text of a button is not empty, decrement the count of spaces
            if buttons[row][column]['text'] != "":
                spaces -= 1
# If there are no empty spaces left, return False
    if spaces == 0:
        return False
    else:
         # If there are still empty spaces, return True
        return True

# Function to initialize a new game
def new_game():
# Declare 'player' as a global variable
    global player

# Randomly choose the starting player from the 'players' list
    player = random.choice(players)

 # Update the label to indicate the current player's turn
    label.config(text="player " + player+" turn")

# Reset the text and background color of all buttons on the game board
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="sky blue")

def mechanics():
    messagebox.showinfo(title="tutorial", message= "1. Each player takes turn while playing\n2. 1st to complete a horizontal line, vertical line or\n diagonal line wins")

# Main Tkinter window initialization
window = Tk()

# Make the window non-resizable
window.resizable(width = False, height = False)

# Set the window icon
img=PhotoImage(file='C:\\game icons\\tic-tac-toe.png')

# Configure window title, background color, and geometry
window.iconphoto(False,img)
window.title("Tech Titan Tic Tac Toe")
window['background']='#FFE5B4'
window.geometry("550x700+500+50")

# Define player symbols
players = ["X","O"]

# Randomly choose the starting player
player = random.choice(players)

# Initialize a 3x3 2d list to represent the game board
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

#a label to display information about the current player's turn
label = Label(text="Player " + player + " turn", font=('cooper black',40),bg='#FFE5B4')
label.pack(side="top")

#a "Restart" button to start a new game
reset_button = Button(text="restart", font=('consolas',15), command=new_game,bg='sky blue')
reset_button.pack(side="top",pady=20)

# the initial coordinates for the question button
j = 10
i = 500
question_button = Button(text= "?", font=('vijaya',20), command=mechanics)
question_button.place(y=j, x=i)

# Create a frame to hold the game board buttons
frame = Frame(window)
frame.pack()

# Create a 3x3 grid of buttons for the Tic-Tac-Toe game
for row in range(3):
    for column in range(3):
        # Each button is configured with specific properties and the 'next_turn' function as the command
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2, 
                                      command= lambda row=row, column=column: next_turn(row,column),bg='sky blue')
        buttons[row][column].grid(row=row,column=column)



window.mainloop()
