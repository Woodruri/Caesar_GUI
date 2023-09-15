import tkinter as tk
import pygame
import random
import time


def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("tbh.mp3")
    pygame.mixer.music.play()


def create_confetti(canvas):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    size = random.randint(10, 30)
    x = random.randint(0, canvas.winfo_width())
    y = 0
    confetti = canvas.create_rectangle(
        x, y, x + size, y + size, fill=random.choice(colors), tags="confetti"
    )
    return confetti


def animate_confetti(canvas):
    confetti_list = canvas.find_withtag("confetti")
    for c in confetti_list:
        """time.sleep(0.05)"""
        canvas.move(c, 0, 2)
    canvas.after(5, animate_confetti, canvas)


def start_confetti():
    animate_confetti(canvas)


def on_button_click():
    play_sound()
    for i in range(random.randint(40, 75)):
        create_confetti(canvas)
    start_confetti()


root = tk.Tk()
root.title("Caesar Cypher App")


canvas = tk.Canvas(root, width=400, height=600, bg="white")
canvas.pack()

start_button = tk.Button(canvas, text="Start Confetti", command=on_button_click)
start_button_window = canvas.create_window(10, 10, anchor=tk.NW, window=start_button)


root.mainloop()
