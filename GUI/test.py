import tkinter as tk

def display():
    text1 = entry.get()
    label2.config(text=text1)
    
root = tk.Tk()
root.title("MyGUI")

label1=tk.Label(root, text = "WYSIWYG" , font=("Arial",18,'bold'),width="125",height="30")
label1.pack()

button=tk.Button(root,text="Done",command = display ) 
button.pack()

entry=tk.Entry(root)
entry.pack()

label2=tk.Label(root,text="Output")
label2.pack()

root.mainloop()