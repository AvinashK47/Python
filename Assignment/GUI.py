import tkinter as tk

def greet():
  label["text"] = "Hello, world!"

root = tk.Tk()
root.title("My First GUI")

button = tk.Button(root, text="Click me", command=greet)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
    