import tkinter as tk
from tkinter import messagebox
import math


# ---------------- Multiplication Table ----------------
class MultiplicationWindow:
    def __init__(self, parent):
        self.win = tk.Toplevel(parent)
        self.win.title("Multiplication Table")
        self.win.geometry("300x420")

        tk.Label(self.win, text="Enter a number:").pack(pady=5)
        self.entry = tk.Entry(self.win)
        self.entry.pack(pady=5)
        tk.Button(self.win, text="Generate", command=self.generate).pack(pady=5)

        self.output = tk.Text(self.win, height=15, width=30)
        self.output.pack(pady=5)

    def generate(self):
        try:
            num = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            return
        self.output.delete("1.0", tk.END)
        for i in range(1, 11):
            self.output.insert(tk.END, f"{num} * {i} = {num * i}\n")


# ---------------- Number Guessing Game ----------------
class GuessingGameWindow:
    def __init__(self, parent):
        self.win = tk.Toplevel(parent)
        self.win.title("Number Guessing Game")
        self.win.geometry("300x220")
        self.target = 25

        tk.Label(self.win, text="Guess the number:").pack(pady=5)
        self.entry = tk.Entry(self.win)
        self.entry.pack(pady=5)
        tk.Button(self.win, text="Guess", command=self.check_guess).pack(pady=5)

        self.status = tk.Label(self.win, text="", font=("Arial", 11))
        self.status.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            return
        if guess == self.target:
            self.status.config(text="Gotchaa!! Correct!", fg="green")
        elif guess < self.target:
            self.status.config(text="Too low, try again.", fg="orange")
        else:
            self.status.config(text="Too high, try again.", fg="orange")
        self.entry.delete(0, tk.END)


# ---------------- Area & Perimeter Calculator ----------------
class AreaPerimeterWindow:
    def __init__(self, parent):
        self.win = tk.Toplevel(parent)
        self.win.title("Area & Perimeter Calculator")
        self.win.geometry("350x420")

        tk.Label(self.win, text="Choose a shape:").pack(pady=5)
        self.shape_var = tk.StringVar(value="circle")
        for shape in ["circle", "rectangle", "triangle"]:
            tk.Radiobutton(
                self.win, text=shape.capitalize(), variable=self.shape_var,
                value=shape, command=self.build_inputs
            ).pack(anchor="w", padx=20)

        self.input_frame = tk.Frame(self.win)
        self.input_frame.pack(pady=10)
        self.entries = {}
        self.build_inputs()

        tk.Button(self.win, text="Calculate", command=self.calculate).pack(pady=10)
        self.result = tk.Label(self.win, text="", justify="left")
        self.result.pack(pady=10)

    def build_inputs(self):
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        self.entries = {}
        shape = self.shape_var.get()
        if shape == "circle":
            fields = ["radius"]
        elif shape == "rectangle":
            fields = ["length", "breadth"]
        else:
            fields = ["base", "height", "side1", "side2", "side3"]
        for field in fields:
            row = tk.Frame(self.input_frame)
            row.pack(pady=2)
            tk.Label(row, text=f"{field.capitalize()}:", width=10, anchor="w").pack(side="left")
            entry = tk.Entry(row)
            entry.pack(side="left")
            self.entries[field] = entry

    def calculate(self):
        shape = self.shape_var.get()
        try:
            values = {k: float(e.get()) for k, e in self.entries.items()}
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for all fields.")
            return

        if shape == "circle":
            r = values["radius"]
            area = math.pi * r * r
            perimeter = 2 * math.pi * r
        elif shape == "rectangle":
            l, b = values["length"], values["breadth"]
            area = l * b
            perimeter = 2 * (l + b)
        else:
            ba, h = values["base"], values["height"]
            a, b, c = values["side1"], values["side2"], values["side3"]
            area = 0.5 * ba * h
            perimeter = a + b + c

        self.result.config(text=f"Area: {area:.2f}\nPerimeter: {perimeter:.2f}")


# ---------------- To-Do List ----------------
class ToDoListWindow:
    def __init__(self, parent):
        self.win = tk.Toplevel(parent)
        self.win.title("To-Do List")
        self.win.geometry("350x420")
        self.tasks = []

        entry_frame = tk.Frame(self.win)
        entry_frame.pack(pady=5)
        self.entry = tk.Entry(entry_frame, width=25)
        self.entry.pack(side="left", padx=5)
        tk.Button(entry_frame, text="Add", command=self.add_item).pack(side="left")

        self.listbox = tk.Listbox(self.win, width=40, height=15)
        self.listbox.pack(pady=10)

        tk.Button(self.win, text="Remove Selected", command=self.remove_item).pack(pady=5)

    def add_item(self):
        item = self.entry.get().strip()
        if not item:
            messagebox.showerror("Invalid Input", "Task cannot be empty.")
            return
        self.tasks.append(item)
        self.listbox.insert(tk.END, item)
        self.entry.delete(0, tk.END)

    def remove_item(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showerror("No Selection", "Please select a task to remove.")
            return
        index = selection[0]
        removed = self.tasks.pop(index)
        self.listbox.delete(index)
        messagebox.showinfo("Removed", f"Removed: {removed}")


# ---------------- Contact Book ----------------
class ContactBookWindow:
    def __init__(self, parent):
        self.win = tk.Toplevel(parent)
        self.win.title("Contact Book")
        self.win.geometry("400x480")
        self.contacts = {}

        form = tk.Frame(self.win)
        form.pack(pady=10)

        tk.Label(form, text="Name:").grid(row=0, column=0, sticky="e", padx=3, pady=2)
        self.name_entry = tk.Entry(form)
        self.name_entry.grid(row=0, column=1, pady=2)

        tk.Label(form, text="Number:").grid(row=1, column=0, sticky="e", padx=3, pady=2)
        self.number_entry = tk.Entry(form)
        self.number_entry.grid(row=1, column=1, pady=2)

        tk.Label(form, text="Address:").grid(row=2, column=0, sticky="e", padx=3, pady=2)
        self.address_entry = tk.Entry(form)
        self.address_entry.grid(row=2, column=1, pady=2)

        btn_frame = tk.Frame(self.win)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Add", command=self.add_contact).pack(side="left", padx=3)
        tk.Button(btn_frame, text="Update", command=self.update_contact).pack(side="left", padx=3)
        tk.Button(btn_frame, text="Delete", command=self.delete_contact).pack(side="left", padx=3)
        tk.Button(btn_frame, text="Clear Form", command=self.clear_form).pack(side="left", padx=3)

        self.listbox = tk.Listbox(self.win, width=45, height=12)
        self.listbox.pack(pady=10)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for name, (number, address) in self.contacts.items():
            self.listbox.insert(tk.END, f"{name} | {number} | {address}")

    def on_select(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return
        name = list(self.contacts.keys())[selection[0]]
        number, address = self.contacts[name]
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, name)
        self.number_entry.delete(0, tk.END)
        self.number_entry.insert(0, number)
        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(0, address)

    def add_contact(self):
        name = self.name_entry.get().strip()
        number_str = self.number_entry.get().strip()
        address = self.address_entry.get().strip()

        if not name or not number_str:
            messagebox.showerror("Invalid Input", "Name and number are required.")
            return
        try:
            number = int(number_str)
        except ValueError:
            messagebox.showerror("Invalid Input", "Number must be numeric.")
            return

        if name in self.contacts:
            overwrite = messagebox.askyesno(
                "Contact Exists", f"'{name}' already exists. Overwrite?"
            )
            if not overwrite:
                return

        self.contacts[name] = [number, address]
        self.refresh_list()
        self.clear_form()

    def update_contact(self):
        name = self.name_entry.get().strip()
        if name not in self.contacts:
            messagebox.showerror("Not Found", f"'{name}' not found in contacts.")
            return
        number_str = self.number_entry.get().strip()
        address = self.address_entry.get().strip()
        try:
            number = int(number_str)
        except ValueError:
            messagebox.showerror("Invalid Input", "Number must be numeric.")
            return
        self.contacts[name] = [number, address]
        self.refresh_list()
        self.clear_form()

    def delete_contact(self):
        name = self.name_entry.get().strip()
        if name not in self.contacts:
            messagebox.showerror("Not Found", f"'{name}' not found in contacts.")
            return
        del self.contacts[name]
        self.refresh_list()
        self.clear_form()

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.number_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


# ---------------- Calculator ----------------
class CalculatorWindow:
    def __init__(self, parent):
        self.win = tk.Toplevel(parent)
        self.win.title("Calculator")
        self.win.geometry("300x260")

        tk.Label(self.win, text="First number:").pack(pady=3)
        self.a_entry = tk.Entry(self.win)
        self.a_entry.pack(pady=3)

        tk.Label(self.win, text="Second number:").pack(pady=3)
        self.b_entry = tk.Entry(self.win)
        self.b_entry.pack(pady=3)

        btn_frame = tk.Frame(self.win)
        btn_frame.pack(pady=10)
        for op in ["+", "-", "*", "/"]:
            tk.Button(
                btn_frame, text=op, width=4, command=lambda o=op: self.calculate(o)
            ).pack(side="left", padx=3)

        self.result = tk.Label(self.win, text="", font=("Arial", 12, "bold"))
        self.result.pack(pady=15)

    def calculate(self, op):
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers.")
            return

        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        elif op == "*":
            res = a * b
        else:
            if b == 0:
                self.result.config(text="Error: division by zero")
                return
            res = a / b
        self.result.config(text=f"Result: {res}")


# ---------------- Main Application ----------------
class MiniToolkitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MINI TOOLKIT")
        self.root.geometry("300x420")

        tk.Label(self.root, text="MINI TOOLKIT", font=("Arial", 16, "bold")).pack(pady=15)

        buttons = [
            ("Multiplication Table", lambda: MultiplicationWindow(self.root)),
            ("Number Guessing Game", lambda: GuessingGameWindow(self.root)),
            ("Area & Perimeter Calculator", lambda: AreaPerimeterWindow(self.root)),
            ("To-Do List", lambda: ToDoListWindow(self.root)),
            ("Contact Book", lambda: ContactBookWindow(self.root)),
            ("Calculator", lambda: CalculatorWindow(self.root)),
        ]

        for text, cmd in buttons:
            tk.Button(self.root, text=text, width=25, command=cmd).pack(pady=6)

        tk.Button(self.root, text="Exit", width=25, command=self.root.quit, fg="red").pack(pady=15)


if __name__ == "__main__":
    root = tk.Tk()
    app = MiniToolkitApp(root)
    root.mainloop()