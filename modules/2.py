import tkinter as tk

window = tk.Tk()
window.title("My First GUI")
window.geometry("400x300")

label = tk.Label(window, text="Hello Kapil", font=("Arial", 20))
label.pack(pady=50)

button = tk.Button(window, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
button.pack()

window.mainloop()