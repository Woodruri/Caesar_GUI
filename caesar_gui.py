import tkinter as tk


def on_button_click():
    label.config(text="button clicked")


root = tk.Tk()
root.title("Caesar Cypher App")

label = tk.Label(root, text="First lil guy")
button = tk.Button(root, text="hi mom")
button.config(command=on_button_click)

label.pack()
button.pack()

root.mainloop()
