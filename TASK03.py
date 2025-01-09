import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f8ff")  

        
        self.title_label = tk.Label(
            root, text="Password Generator", font=("Helvetica", 24, "bold"), bg="#f0f8ff", fg="#4682b4"
        )
        self.title_label.pack(pady=10)

        
        self.length_label = tk.Label(
            root, text="Password Length:", font=("Helvetica", 14), bg="#f0f8ff", fg="#4682b4"
        )
        self.length_label.pack(pady=5)

        self.length_slider = tk.Scale(
            root, from_=6, to_=32, orient="horizontal", font=("Helvetica", 12), bg="#87ceeb", fg="#000",
            troughcolor="#4682b4", highlightbackground="#f0f8ff"
        )
        self.length_slider.set(12)
        self.length_slider.pack(pady=5)

        
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)

        self.uppercase_check = tk.Checkbutton(
            root, text="Include Uppercase Letters", font=("Helvetica", 12), bg="#f0f8ff", fg="#4682b4",
            variable=self.include_uppercase
        )
        self.uppercase_check.pack(pady=2)

        self.digits_check = tk.Checkbutton(
            root, text="Include Digits", font=("Helvetica", 12), bg="#f0f8ff", fg="#4682b4",
            variable=self.include_digits
        )
        self.digits_check.pack(pady=2)

        self.special_check = tk.Checkbutton(
            root, text="Include Special Characters", font=("Helvetica", 12), bg="#f0f8ff", fg="#4682b4",
            variable=self.include_special
        )
        self.special_check.pack(pady=2)

        
        self.generate_button = tk.Button(
            root, text="Generate Password", font=("Helvetica", 14, "bold"), bg="#4682b4", fg="#ffffff",
            command=self.generate_password
        )
        self.generate_button.pack(pady=20)
        self.generate_button.bind("<Enter>", lambda e: self.on_hover(self.generate_button))
        self.generate_button.bind("<Leave>", lambda e: self.on_leave(self.generate_button))

        
        self.password_entry = tk.Entry(
            root, font=("Helvetica", 16), bg="#ffffff", fg="#000", justify="center", bd=2
        )
        self.password_entry.pack(pady=10, padx=20, fill="x")

    def generate_password(self):
        length = self.length_slider.get()
        characters = string.ascii_lowercase
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_digits.get():
            characters += string.digits
        if self.include_special.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Please select at least one character set.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def on_hover(self, button):
        button.configure(bg="#87ceeb")  

    def on_leave(self, button):
        button.configure(bg="#4682b4")  

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
