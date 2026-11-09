from tkinter import *

def hours_to_seconds():
    hours = int(hours_input.get())
    seconds = hours * 3600
    seconds_result_label.config(text=f"{seconds}")

window = Tk()
window.config(padx=20, pady=20)
window.title("Seconds to Hours Converter")
window.rowconfigure((0, 1, 2), weight=1)
window.columnconfigure((0, 1, 2), weight=1)
window.configure(bg="pink")

hours_label = Label(text="Hour(s)")
hours_label.configure(bg="pink")
hours_label.grid(column=2, row=0, sticky="nsew")
is_equal_label = Label(text="is equal to")
is_equal_label.configure(bg="pink")
is_equal_label.grid(column=0, row=1, sticky="nsew")
seconds_label = Label(text="Seconds")
seconds_label.configure(bg="pink")
seconds_label.grid(column=2, row=1, sticky="nsew")
seconds_result_label = Label(text="0")
seconds_result_label.configure(bg="pink")
seconds_result_label.grid(column=1, row=1, sticky="nsew")

calculate_button = Button(text="Calculate", command=hours_to_seconds)
calculate_button.configure(bg="pink")
calculate_button.grid(column=1, row=3, sticky="nsew")

hours_input = Entry(width=7)
hours_input.configure(bg="pink")
hours_input.focus()
hours_input.grid(column=1, row=0, sticky="nsew")







window.mainloop()