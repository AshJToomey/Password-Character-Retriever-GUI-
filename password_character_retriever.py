import tkinter as tk
from tkinter import messagebox

def is_valid_char(c):
    return c.isalnum()

def retrieve_characters():
    password = entry_password.get()
    positions_input = entry_positions.get()

    if not password:
        messagebox.showwarning("Input Error", "Please enter your password.")
        return

    try:
        positions = [int(pos.strip()) for pos in positions_input.split(",")]
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers (comma-separated).")
        return

    result_text.delete("1.0", tk.END)  # Clear previous output
    result_text.insert(tk.END, "Retrieving characters...\n\n")

    for pos in positions:
        if pos <= 0 or pos > len(password):
            result_text.insert(tk.END, f"Position {pos}: Out of range for this password.\n")
        else:
            char = password[pos - 1]
            if is_valid_char(char):
                result_text.insert(tk.END, f"Character {pos}: {char}\n")
            else:
                result_text.insert(tk.END, f"Character {pos}: Not a letter or number → Ask security questions instead\n")

# GUI setup
root = tk.Tk()
root.title("Password Character Retriever")
root.geometry("400x300")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Enter full password:").pack(pady=5)
entry_password = tk.Entry(root, width=30)  # Password now visible
entry_password.pack()

tk.Label(root, text="Enter character positions (e.g., 2,5,7):").pack(pady=5)
entry_positions = tk.Entry(root, width=30)
entry_positions.pack()

tk.Button(root, text="Retrieve", command=retrieve_characters).pack(pady=10)

result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=5)

# Run the GUI loop
root.mainloop()


