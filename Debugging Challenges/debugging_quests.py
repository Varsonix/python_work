import tkinter as tk

window = tk.Tk()

window.title("My First GUI")

window.geometry("800x600")

def button_clicked():
    print("Button clicked!")

label = tk.Label(window, text="Hello, GUI!")
label.pack() # place label in the window (I guess)

button = tk.Button(window, 
                   text="Click Me", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)
button.pack(padx=20, pady=20)
window.mainloop()

