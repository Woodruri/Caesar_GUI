import tkinter as tk
import pygame


def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("tbh.mp3")
    pygame.mixer.music.play()


def encode(string, shift_no):
    list = []
    for letter in string:
        list.append(chr(ord(letter) + shift_no))
    return string(list)


def on_button_click():
    play_sound()
    to_encode = encoded_text.get()


root = tk.Tk()
root.title("Caesar Cypher App")
root.geometry("400x600")

encoded_text = tk.Entry(root, text="text to encode", height=5, width=30)
shift_amount = tk.Entry(root, text="Amount to shift given text by", height=4, width=4)
encode_btn = tk.Button(root, text="encode", command=on_button_click)

output = tk.Text(root, height=5, width=30)


root.mainloop()
