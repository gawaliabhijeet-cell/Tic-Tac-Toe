import tkinter as tk
from tkinter import messagebox

class TicTacToe:

    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Tic-Tac-Toe")

        self.current_player = "X"
        self.buttons = []
        self.score_x = 0
        self.score_o = 0

        self.create_widgets()

    # ---------------- UI ----------------
    def create_widgets(self):

        # Turn Label
        self.turn_label = tk.Label(
            self.root,
            text=f"Player {self.current_player}'s Turn",
            font=("Arial", 16, "bold")
        )
        self.turn_label.grid(row=0, column=0, columnspan=3, pady=5)

        # Scoreboard
        self.score_label = tk.Label(
            self.root,
            text="Score  X: 0   O: 0",
            font=("Arial", 14)
        )
        self.score_label.grid(row=1, column=0, columnspan=3)

        # Buttons Grid
        for i in range(9):
            btn = tk.Button(
                self.root,
                text="",
                font=("Arial", 25),
                width=6,
                height=2,
                command=lambda i=i: self.button_click(i)
            )
            btn.grid(row=2 + i//3, column=i%3)
            self.buttons.append(btn)

        # Restart Button
        restart_btn = tk.Button(
            self.root,
            text="Restart Game",
            font=("Arial", 12),
            bg="lightblue",
            command=self.reset_board
        )
        restart_btn.grid(row=5, column=0, columnspan=3, pady=10)

    # ---------------- Game Logic ----------------
    def button_click(self, index):
        if self.buttons[index]["text"] == "":
            self.buttons[index]["text"] = self.current_player
            self.buttons[index]["fg"] = "blue" if self.current_player == "X" else "red"

            if self.check_winner():
                return

            if self.check_draw():
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.disable_buttons()
                return

            self.toggle_player()

    def toggle_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.turn_label.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self):

        winning_combinations = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]

        for combo in winning_combinations:
            if (self.buttons[combo[0]]["text"] ==
                self.buttons[combo[1]]["text"] ==
                self.buttons[combo[2]]["text"] != ""):

                for i in combo:
                    self.buttons[i].config(bg="lightgreen")

                winner = self.buttons[combo[0]]["text"]

                if winner == "X":
                    self.score_x += 1
                else:
                    self.score_o += 1

                self.update_score()
                messagebox.showinfo("Winner", f"Player {winner} Wins!")
                self.disable_buttons()
                return True

        return False

    def check_draw(self):
        for btn in self.buttons:
            if btn["text"] == "":
                return False
        return True

    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def update_score(self):
        self.score_label.config(
            text=f"Score  X: {self.score_x}   O: {self.score_o}"
        )

    def reset_board(self):
        for btn in self.buttons:
            btn.config(text="", bg="SystemButtonFace", state="normal")

        self.current_player = "X"
        self.turn_label.config(text=f"Player {self.current_player}'s Turn")


# ---------------- Run Program ----------------
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()


