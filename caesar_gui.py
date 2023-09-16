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
    return list


def on_button_click():
    play_sound()
    encoded = encode(encoded_text.get(), shift_amount.get())
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.end)
    output_text.insert(tk.END, encoded)
    output_text.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Caesar Cypher App")
root.geometry("400x600")

encoded_text = tk.Entry(root, text="text to encode")
shift_amount = tk.Entry(root, text="Amount to shift given text by")
encode_btn = tk.Button(root, text="encode", command=on_button_click)

output_text = tk.Text(root, height=5, width=30)


encoded_text.grid(row=0, column=0, padx=10, pady=5)
shift_amount.grid(row=1, column=0, padx=10, pady=5)
encode_btn.grid(row=2, column=0, padx=10, pady=5)
output_text.grid(row=4, column=0, padx=10, pady=10)

root.mainloop()
