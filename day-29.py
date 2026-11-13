from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password_letter_list = [choice(letters) for _ in range(randint(8, 10))]

    password_symbol_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter_list + password_number_list + password_symbol_list
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_input.get()
    email = email_user_input.get()
    password = password_input.get()

    if not len(website) or not len(password):
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title= website, message=f"These are the details entered: \nEmail: {email} "
                                                f"\nPassword: {password} \nShould we continue to save?")

        if is_ok:
            with open("_data.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=80)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="_logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

generate_button = Button(text="Generate Password")
generate_button.grid(row=4, column=2)

add_button = Button(text="Add", width=27, command=save_password)
add_button.grid(row=4, column=1)

website_input = Entry(width=51)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

email_user_input = Entry(width=51)
email_user_input.insert(0, "mohsanjavedqureshi@icloud.com")
email_user_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=51)
password_input.grid(column=1, row=3, columnspan=2)

window.mainloop()