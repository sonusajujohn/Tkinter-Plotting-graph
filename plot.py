import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
    canvas.draw()


# Create main Tkinter window
root = tk.Tk()
root.title("2D Graph Plotter")
root.geometry("600x500")

# Create Matplotlib figure and axis
fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Add a button to open a file
btn_open = tk.Button(root, text="Open File", command=open_file)
btn_open.pack()

root.mainloop()
