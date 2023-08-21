
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from band_allocator import BandAllocator
import numpy as np

def update_plot():
    allocations, users = allocator.get_allocations()
    
    colors = plt.cm.jet(np.linspace(0, 1, allocator.levels))  # Generate unique colors for each level

    plt.cla()  # Clear current plot

    for i, (allocation, user) in enumerate(zip(allocations, users)):
        plt.bar(i, allocation, width=0.5, color=colors[i], label=user if allocation else None)
        if allocation:
            plt.text(i, allocation/2, user, ha='center', va='center', color='white')

    plt.xlabel('Band Index')
    plt.ylabel('Frequency (kHz)')
    plt.title('Spectrum Band Allocation')
    plt.ylim(allocator.start_freq, allocator.end_freq)
    canvas.draw()

def allocate():
    user_name = name_entry.get()
    if not user_name:
        messagebox.showerror("Error", "Please provide a user name!")
        return

    try:
        freq = float(freq_entry.get())
        if allocator.allocate_band(freq, user_name):
            update_plot()
        else:
            messagebox.showerror("Error", "Band is already allocated or frequency is out of range!")
    except ValueError:
        messagebox.showerror("Error", "Invalid frequency value!")

root = tk.Tk()
root.title("Spectrum Band Allocation App")

allocator = BandAllocator(1, 200000, 20)

fig, ax = plt.subplots(figsize=(6, 6))
canvas = tk.Canvas(master=root, width=600, height=600)
canvas.pack()

name_label = tk.Label(root, text="User Name:")
name_label.pack(pady=10)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

freq_label = tk.Label(root, text="Enter frequency (kHz):")
freq_label.pack(pady=10)
freq_entry = tk.Entry(root)
freq_entry.pack(pady=5)

allocate_button = tk.Button(root, text="Allocate", command=allocate)
allocate_button.pack(pady=20)

update_plot()

root.mainloop()

