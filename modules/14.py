import customtkinter as ctk

window = ctk.CTk()

window.title("CustomTkinter")
window.geometry("400x300")

label = ctk.CTkLabel(
    window,
    text="Welcome Kapil",
    font=("Arial", 25)
)

label.pack(pady=50)

button = ctk.CTkButton(
    window,
    text="Click Me",
    command=lambda: label.configure(text="Button Clicked!")
)

button.pack()

window.mainloop()