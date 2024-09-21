import tkinter as tk
from tkinter import messagebox

def submit_form():
    # Get the input values from the form
    username = username_entry.get()
    password = password_entry.get()

    # Display the values in a message box
    messagebox.showinfo("Form Submitted", f"Username: {username}\nPassword: {password}")

    # Clear the entry fields after submission
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    root.title("Password Generator")
    
    # Set window size to 300x200
    root.geometry("300x200")

    # Create and place the Username label and entry
    username_label = tk.Label(root, text="Username:")
    username_label.pack(pady=5)
    
    global username_entry
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    # Create and place the Password label and entry
    password_label = tk.Label(root, text="Password:")
    password_label.pack(pady=5)
    
    global password_entry
    password_entry = tk.Entry(root, show="*")  # Show password as asterisks
    password_entry.pack(pady=5)

    # Create and place the Submit button
    submit_button = tk.Button(root, text="Submit", command=submit_form)
    submit_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()