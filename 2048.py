import tkinter as tk
import random

class Game2048:
    def __init__(self, master, size):
        self.master = master
        self.n = size
        self.grid = [[0] * self.n for _ in range(self.n)]
        self.score = 0

        self.master.title("2048 Game")
        self.master.resizable(False, False)

        # Top Frame for Score and Restart Button
        top_frame = tk.Frame(self.master)
        top_frame.pack()

        self.score_label = tk.Label(top_frame, text=f"Score: {self.score}", font=("Arial", 18, "bold"))
        self.score_label.pack(side=tk.LEFT, padx=10)

        restart_button = tk.Button(top_frame, text="Restart", command=self.restart_game, font=("Arial", 14))
        restart_button.pack(side=tk.RIGHT, padx=10)

        # Main Grid Frame
        self.frame = tk.Frame(self.master, bg="#bbada0")
        self.frame.pack(padx=10, pady=10)

        self.cells = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                label = tk.Label(self.frame, text="", width=6, height=3,
                                 font=("Helvetica", 24, "bold"),
                                 bg="#cdc1b4", relief="ridge", borderwidth=3)
                label.grid(row=i, column=j, padx=5, pady=5)
                row.append(label)
            self.cells.append(row)

        self.start_game()
        self.master.bind("<Key>", self.key_handler)
        self.update_grid()

    def start_game(self):
        self.grid = [[0] * self.n for _ in range(self.n)]
        self.score = 0
        for _ in range(2):
            self.add_new_tile()
        self.update_grid()

    def restart_game(self):
        self.start_game()

    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(self.n) for j in range(self.n) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = random.choice([2, 4])

    def compress(self):
        new_grid = []
        for row in self.grid:
            new_row = [num for num in row if num != 0]
            new_row += [0] * (self.n - len(new_row))
            new_grid.append(new_row)
        self.grid = new_grid

    def merge(self):
        for i in range(self.n):
            for j in range(self.n - 1):
                if self.grid[i][j] == self.grid[i][j + 1] and self.grid[i][j] != 0:
                    self.grid[i][j] *= 2
                    self.score += self.grid[i][j]
                    self.grid[i][j + 1] = 0

    def reverse(self):
        for i in range(self.n):
            self.grid[i].reverse()

    def transpose(self):
        self.grid = [list(row) for row in zip(*self.grid)]

    def move_left(self):
        self.compress()
        self.merge()
        self.compress()

    def move_right(self):
        self.reverse()
        self.move_left()
        self.reverse()

    def move_up(self):
        self.transpose()
        self.move_left()
        self.transpose()

    def move_down(self):
        self.transpose()
        self.move_right()
        self.transpose()

    def check_status(self):
        for row in self.grid:
            if 2048 in row:
                return 1  # Win

        for row in self.grid:
            if 0 in row:
                return 0  # Still playable

        for i in range(self.n):
            for j in range(self.n - 1):
                if self.grid[i][j] == self.grid[i][j + 1]:
                    return 0
        for j in range(self.n):
            for i in range(self.n - 1):
                if self.grid[i][j] == self.grid[i + 1][j]:
                    return 0
        return 2  # Game Over

    def get_color(self, value):
        colors = {
            0: "#cdc1b4", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
            16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
            128: "#edcf72", 256: "#edcc61", 512: "#edc850",
            1024: "#edc53f", 2048: "#edc22e"
        }
        return colors.get(value, "#3c3a32")

    def update_grid(self):
        for i in range(self.n):
            for j in range(self.n):
                value = self.grid[i][j]
                if value == 0:
                    self.cells[i][j].config(text="", bg=self.get_color(value))
                else:
                    self.cells[i][j].config(text=str(value), bg=self.get_color(value))

        self.score_label.config(text=f"Score: {self.score}")

    def key_handler(self, event):
        key = event.keysym
        prev_grid = [row[:] for row in self.grid]

        if key == "Up":
            self.move_up()
        elif key == "Down":
            self.move_down()
        elif key == "Left":
            self.move_left()
        elif key == "Right":
            self.move_right()
        else:
            return

        if self.grid != prev_grid:
            self.add_new_tile()
            self.update_grid()
            status = self.check_status()

            if status == 1:
                self.show_message("🎉 You won!")
            elif status == 2:
                self.show_message("😞 Game Over!")

    def show_message(self, message):
        top = tk.Toplevel(self.master)
        top.title("Game Result")
        tk.Label(top, text=message, font=("Arial", 20, "bold")).pack(padx=20, pady=20)
        tk.Button(top, text="OK", command=top.destroy, font=("Arial", 14)).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    grid_size = 4  # 4x4 Grid size
    Game2048(root, grid_size)
    root.mainloop()
