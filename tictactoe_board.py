import tkinter as tk
import random
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.board = [" "]*9
        self.current_player = "X"
        self.buttons = []
        self.create_board()
        self.root.mainloop()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=" ", font=("Helvetica", 20), width=4, height=2,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def on_button_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.show_winner()
            else:
                self.switch_player()
                self.computer_move()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def computer_move(self):
        empty_cells = [i for i in range(9) if self.board[i] == " "]
        if empty_cells:
            index = random.choice(empty_cells)
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.show_winner()
            else:
                self.switch_player()

    def check_winner(self):
        win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != " ":
                return True
        return False

    def show_winner(self):
        winner = self.current_player
        if winner == "X":
            winner = "You Win"
        elif winner == "O":
            winner = "You Lose"
        tk.messagebox.showinfo("Game Over", f"{winner} wins!")
        self.root.quit()


if __name__ == "__main__":
    TicTacToe()
