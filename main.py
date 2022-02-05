# Import the required libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Generator import rr_main

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Add an optional Label widget
Label(win, text="Indian Sign Language Generator",
      font=('Aerial 17 bold italic')).pack(pady=30)

# Create a Button to display the message
ttk.Button(win, text="Start Recognizing", command=rr_main).pack(pady=20)
win.mainloop()
