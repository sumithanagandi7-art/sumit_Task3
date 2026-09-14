import string
import secrets
import tkinter as tk
from tkinter import messagebox
import pyperclip
import random

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("500x600")
        
        # Variables
        self.length_var = tk.IntVar(value=12)
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        self.exclude_ambiguous_var = tk.BooleanVar(value=False)
        self.history = []
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        tk.Label(self.root, text="Secure Password Generator", font=("Helvetica", 16, "bold")).pack(pady=10)
        
        # Length
        length_frame = tk.Frame(self.root)
        length_frame.pack(fill="x", padx=20, pady=5)
        tk.Label(length_frame, text="Password Length:").pack(side="left")
        self.length_scale = tk.Scale(length_frame, from_=8, to=128, orient="horizontal", variable=self.length_var)
        self.length_scale.pack(side="right", fill="x", expand=True, padx=10)
        
        # Character Types
        types_frame = tk.LabelFrame(self.root, text="Character Types")
        types_frame.pack(fill="x", padx=20, pady=10)
        
        tk.Checkbutton(types_frame, text="Uppercase (A-Z)", variable=self.upper_var).pack(anchor="w", padx=10)
        tk.Checkbutton(types_frame, text="Lowercase (a-z)", variable=self.lower_var).pack(anchor="w", padx=10)
        tk.Checkbutton(types_frame, text="Numbers (0-9)", variable=self.digits_var).pack(anchor="w", padx=10)
        tk.Checkbutton(types_frame, text="Symbols (!@#$)", variable=self.symbols_var).pack(anchor="w", padx=10)
        
        # Exclude Ambiguous
        tk.Checkbutton(self.root, text="Exclude Ambiguous Characters (e.g., 0, O, l, 1, I)", variable=self.exclude_ambiguous_var).pack(anchor="w", padx=20, pady=5)
        
        # Generate Button
        tk.Button(self.root, text="Generate Password", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", command=self.generate_password).pack(pady=15)
        
        # Password Display
        self.password_entry = tk.Entry(self.root, font=("Courier", 14), justify="center")
        self.password_entry.pack(fill="x", padx=20, ipady=5)
        
        # Copy Button
        tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=5)
        
        # Strength Indicator
        self.strength_label = tk.Label(self.root, text="Strength: N/A", font=("Helvetica", 12))
        self.strength_label.pack(pady=5)
        
        # History
        history_frame = tk.LabelFrame(self.root, text="Generation History (Last 5)")
        history_frame.pack(fill="both", expand=True, padx=20, pady=10)
        self.history_listbox = tk.Listbox(history_frame, font=("Courier", 10), height=5)
        self.history_listbox.pack(fill="both", expand=True, padx=5, pady=5)

    def generate_password(self):
        length = self.length_var.get()
        use_upper = self.upper_var.get()
        use_lower = self.lower_var.get()
        use_digits = self.digits_var.get()
        use_symbols = self.symbols_var.get()
        exclude_ambiguous = self.exclude_ambiguous_var.get()
        
        pool_parts = []
        pools = []
        
        ambiguous_chars = "0Ol1I"
        
        if use_upper:
            chars = string.ascii_uppercase
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in ambiguous_chars)
            if chars:
                pool_parts.append(chars)
                pools.append(chars)
                
        if use_lower:
            chars = string.ascii_lowercase
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in ambiguous_chars)
            if chars:
                pool_parts.append(chars)
                pools.append(chars)
                
        if use_digits:
            chars = string.digits
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in ambiguous_chars)
            if chars:
                pool_parts.append(chars)
                pools.append(chars)
                
        if use_symbols:
            chars = string.punctuation
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in ambiguous_chars)
            if chars:
                pool_parts.append(chars)
                pools.append(chars)
        
        if len(pools) < 2:
            messagebox.showerror("Error", "Please select at least two character types!")
            return
            
        if length < 8:
            messagebox.showerror("Error", "Password length must be at least 8!")
            return
            
        full_pool = "".join(pool_parts)
        if not full_pool:
            messagebox.showerror("Error", "Selected character types yielded no valid characters.")
            return

        # Ensure at least one from each selected pool
        password_chars = []
        for pool in pools:
            password_chars.append(secrets.choice(pool))
            
        # Fill the rest
        for _ in range(length - len(pools)):
            password_chars.append(secrets.choice(full_pool))
            
        # Shuffle the password to avoid predictable structure
        # (secrets module does not provide shuffle, use SystemRandom)
        sys_random = random.SystemRandom()
        sys_random.shuffle(password_chars)
        
        password = "".join(password_chars)
        
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        
        self.update_strength(length, len(pools))
        
        # Copy to clipboard automatically on generation
        try:
            pyperclip.copy(password)
        except Exception as e:
            print(f"Failed to copy to clipboard: {e}")
            
        self.update_history(password)
        
    def update_strength(self, length, types_count):
        # Basic strength logic
        if length < 10 or types_count < 3:
            strength = "Weak"
            color = "red"
        elif length < 14 or types_count < 4:
            strength = "Medium"
            color = "orange"
        else:
            strength = "Strong"
            color = "green"
            
        self.strength_label.config(text=f"Strength: {strength}", fg=color)
        
    def update_history(self, password):
        self.history.insert(0, password)
        if len(self.history) > 5:
            self.history.pop()
            
        self.history_listbox.delete(0, tk.END)
        for p in self.history:
            self.history_listbox.insert(tk.END, p)
            
    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            try:
                pyperclip.copy(password)
                messagebox.showinfo("Success", "Password copied to clipboard!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to copy: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
