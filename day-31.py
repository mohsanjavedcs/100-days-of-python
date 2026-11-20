from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=200, height=200)
card_front_img = PhotoImage(file="_logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)




window.mainloop()