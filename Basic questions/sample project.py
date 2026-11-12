import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("500x800")
root.resizable(False, False)

# Game variables
current_player = "X"
game_over = False
x_score = 0
o_score = 0
buttons = []
# Score display
score_label = tk.Label(
    root,
    text="X: 0    O: 0",
    font=("Arial", 20, "bold")
)
score_label.pack(pady=15)
turn_label = tk.Label(
    root,
    text="Player X's Turn",
    font=("Arial", 16)
)
turn_label.pack(pady=5)
# Game board
board_frame = tk.Frame(root)
board_frame.pack()
def check_winner():
    # Winning combinations
    winning_positions = [

       
    ]

    for a, b, c in winning_positions:
        if (
            buttons[a]["text"] != "" and
            buttons[a]["text"] == buttons[b]["text"] and
            buttons[a]["text"] == buttons[c]["text"]
        ):
            return buttons[a]["text"]

    return None


def check_draw():
    for button in buttons:
        if button["text"] == "":
            return False
    return True


def button_click(index):
    global current_player
    global game_over
    global x_score
    global o_score

    if game_over:
        return

    # Don't allow clicking an already filled box
    if buttons[index]["text"] != "":
        return

    # Put X or O
    buttons[index]["text"] = current_player

    winner = check_winner()

    if winner:
        game_over = True

        if winner == "X":
            x_score += 1
        else:
            o_score += 1

        score_label.config(
            text=f"X: {x_score}    O: {o_score}"
        )

        turn_label.config(
            text=f"Player {winner} Wins!"
        )

        messagebox.showinfo(
            "Game Over",
            f"Player {winner} Wins!"
        )
        return
    # Check draw
    if check_draw():
        game_over = True

        turn_label.config(
            text="Game Draw!"
        )

        messagebox.showinfo(
            "Game Over",
            "It's a Draw!"
        )

        return

    # Change player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    turn_label.config(
        text=f"Player {current_player}'s Turn"
    )


