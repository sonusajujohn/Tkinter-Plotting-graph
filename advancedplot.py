import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("CSV Files", "*.csv"), ("All Files", "*.*")])
    if file_path:
        load_and_plot(file_path)


def load_and_plot(file_path):
    data = np.loadtxt(file_path, skiprows=1)  # Skip the header row
    x, y = data[:, 0], data[:, 1]

    ax.clear()
    ax.plot(x, y, marker='o', linestyle='-', color='b')
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_title("2D Plot from File Data")
    ax.grid(grid_on)  # Apply grid setting
    canvas.draw()


def toggle_grid():
    global grid_on
    grid_on = not grid_on
    ax.grid(grid_on)
    canvas.draw()


def save_plot():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg"),
                                                        ("All Files", "*.*")])
    if file_path:
        fig.savefig(file_path)


# Create main Tkinter window
root = tk.Tk()
root.title("2D Graph Plotter")
root.geometry("700x600")

# Create Matplotlib figure and axis
fig, ax = plt.subplots(figsize=(5, 4))
grid_on = True  # Grid state
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Add toolbar for zoom & pan
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack()

# Add buttons
btn_open = tk.Button(root, text="Open File", command=open_file)
btn_open.pack()
btn_grid = tk.Button(root, text="Toggle Grid", command=toggle_grid)
btn_grid.pack()
btn_save = tk.Button(root, text="Save Plot", command=save_plot)
btn_save.pack()

root.mainloop()
