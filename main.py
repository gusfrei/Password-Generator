import string
import secrets
import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Password Generator")
app.geometry("400x430")

frame = ctk.CTkFrame(app, fg_color="transparent")
frame.pack(padx=20, pady=20)

# Using the string module to create a dictionary with lowercase, uppercase, numbers, and symbols
char_sets = {
    "Lowercase Letters": string.ascii_lowercase,
    "Uppercase Letters": string.ascii_uppercase,
    "Digits": string.digits,
    "Symbols": string.punctuation
}

# Default length
pass_len = 8

# Generate password function based on selected character sets using secrets and string modules.
def generate_password():
    selected_chars = "".join(char_sets[option] for option, var in options.items() if var.get())

    if not selected_chars:
        return ""

    while True:
        password = ''.join(secrets.choice(selected_chars) for _ in range(pass_len))
        if (any(c.islower() for c in password) or not options["Lowercase Letters"].get()) and \
                (any(c.isupper() for c in password) or not options["Uppercase Letters"].get()) and \
                (not options["Digits"].get() or sum(c.isdigit() for c in password) >= 5) and \
                (any(c in string.punctuation for c in password) or not options["Symbols"].get()):
            return password
def update_password_field():
    global pass_len
    pass_len = int(length_combobox.get())
    password = generate_password()
    if password:
        new_password.delete(0, 'end')
        new_password.insert(0, password)

def copy_to_clipboard():
    password = new_password.get()
    app.clipboard_clear()
    app.clipboard_append(password)


title_label = ctk.CTkLabel(frame, text="Password Generator", font=('Arial', 24, 'bold'))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Password display entry
new_password = ctk.CTkEntry(frame, show="", font=('Arial', 14), width=300)
new_password.grid(row=1, column=0, columnspan=2, pady=10)

options = {}
row_idx = 2
for option in char_sets:
    var = ctk.BooleanVar(value=True)
    checkbox = ctk.CTkCheckBox(frame, text=option, variable=var, font=('Arial', 14))
    checkbox.grid(row=row_idx, column=0, columnspan=2, pady=5, sticky="w")
    options[option] = var
    row_idx += 1

combobox_label = ctk.CTkLabel(frame, text="Password Length:", font=('Arial', 14))
combobox_label.grid(row=row_idx, column=0, pady=10, sticky="w")

length_combobox = ctk.CTkComboBox(frame, values=[str(i) for i in range(8, 21)], font=('Arial', 14), width=150)
length_combobox.set(str(pass_len))
length_combobox.grid(row=row_idx, column=1, pady=5)

# Update row index after combobox
row_idx += 1

# Button to generate the password
generate_button = ctk.CTkButton(frame, text="Generate", font=('Arial', 14), fg_color="#2596be",
                                hover_color="#2e8cd2", command=update_password_field)
generate_button.grid(row=row_idx, column=0, columnspan=2, pady=10)

# Button to copy the password
copy_pass_button = ctk.CTkButton(frame, text="Copy to Clipboard", font=('Arial', 14), fg_color="#2596be",
                                 hover_color="#2e8cd2", command=copy_to_clipboard)
copy_pass_button.grid(row=row_idx + 1, column=0, columnspan=2, pady=10)

# Start the app
app.mainloop()

































