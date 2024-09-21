import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password(length, exclude):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    if exclude:
        exclude_set = set(exclude)
        alphabet = ''.join(char for char in alphabet if char not in exclude_set)
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def generate_and_display_password(length=None, exclude=None):
    if length is None:
        length = length_scale.get()
    if exclude is None:
        exclude = exclude_entry.get()

    password = generate_password(length, exclude)
    output_entry.delete(0, tk.END)
    output_entry.insert(0, password)

def copy_to_clipboard():
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(output_entry.get())  # Append the password
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def update_length_label(value):
    length_label.config(text=f"Password Length: {value}")
    generate_and_display_password(length=int(value))  # Generate password on scale change

def manual_generate():
    generate_and_display_password()  # Generate password based on current settings

def main():
    global root, length_scale, length_label, exclude_entry, output_entry
    root = tk.Tk()
    root.title("Password Generator")
    
    # Set window size
    root.geometry("500x400")  # Adjusted width for larger input field

    # Create and place the length label and scale
    length_label = tk.Label(root, text="Password Length: 12", font=("Arial", 14))  # Increased font size
    length_label.pack(pady=5)

    length_scale = tk.Scale(root, from_=8, to=20, orient=tk.HORIZONTAL, command=update_length_label, length=300)  # Set max to 30
    length_scale.set(12)  # Set default value
    length_scale.pack(pady=10)

    # Create and place the Exclude label and entry
    exclude_label = tk.Label(root, text="Exclude Characters:", font=("Arial", 14))  # Increased font size
    exclude_label.pack(pady=5)
    
    exclude_entry = tk.Entry(root, font=("Arial", 14))  # Increased font size
    exclude_entry.pack(pady=5)

    # Create and place the output label and entry
    output_label = tk.Label(root, text="Generated Password:", font=("Arial", 14))  # Increased font size
    output_label.pack(pady=5)
    
    output_entry = tk.Entry(root, font=("Arial", 14), width=30)  # Increased font size and width
    output_entry.pack(pady=5)

    # Create and place the Generate button
    generate_button = tk.Button(root, text="Generate", command=manual_generate, font=("Arial", 14))  # Increased font size
    generate_button.pack(pady=10)

    # Create and place the Copy button
    copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard, font=("Arial", 14))  # Increased font size
    copy_button.pack(pady=10)

    # Generate initial password
    generate_and_display_password(length=length_scale.get())

    root.mainloop()

if __name__ == "__main__":
    main()
