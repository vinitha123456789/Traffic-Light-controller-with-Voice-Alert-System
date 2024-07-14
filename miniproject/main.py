from tkinter import *
import time


def change_light(color):
    red.config(bg='gray')
    yellow.config(bg='gray')
    green.config(bg='gray')

    if color == 'red':
        red.config(bg='red')
    elif color == 'yellow':
        yellow.config(bg='yellow')
    elif color == 'green':
        green.config(bg='green')


# Create a tkinter window
window = Tk()
window.title("Traffic Light")

# Create the traffic light circles
red = Label(window, bg='gray', width=20, height=10, relief=SUNKEN)
red.grid(row=0, padx=10, pady=10)
yellow = Label(window, bg='gray', width=20, height=10, relief=SUNKEN)
yellow.grid(row=1, padx=10, pady=10)
green = Label(window, bg='gray', width=20, height=10, relief=SUNKEN)
green.grid(row=2, padx=10, pady=10)

window.mainloop()
