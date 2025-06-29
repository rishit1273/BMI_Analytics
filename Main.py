import tkinter as tk
from tkinter import ttk, messagebox
from credentials import Calculate_bmi, Bmi_category
from analytics import export_to_csv
import os
import csv
from collections import Counter

users = []


def append_to_csv(user_data, filename="users_bmidata.csv"):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=user_data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(user_data)


def update_analytics_display():
    if not users:
        analytics_text.config(state='normal')
        analytics_text.delete(1.0, tk.END)
        analytics_text.insert(tk.END, "No data available.")
        analytics_text.config(state='disabled')
        return

    bmis = [u["BMI"] for u in users]
    categories = [u["Category"] for u in users]
    counter = Counter(categories)

    output = []
    output.append(f"Total Users: {len(users)}")
    output.append(f"Average BMI: {round(sum(bmis)/len(bmis), 2)}")
    output.append(f"Highest BMI: {max(bmis)}")
    output.append(f"Lowest BMI: {min(bmis)}")
    output.append("\nBMI Categories:")
    for cat, count in counter.items():
        percent = (count / len(users)) * 100
        output.append(f" - {cat}: {count} user(s) ({percent:.2f}%)")

    analytics_text.config(state='normal')
    analytics_text.delete(1.0, tk.END)
    analytics_text.insert(tk.END, "\n".join(output))
    analytics_text.config(state='disabled')


def calculate_and_store():
    try:
        name = name_entry.get().strip()
        age = age_entry.get().strip()
        scale = unit_var.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if not name or not age:
            raise ValueError("Name and Age required")
        if scale == "kg/m" and height > 3:
            height = height / 100

        bmi = Calculate_bmi(weight, height, scale)
        if bmi is None:
            raise ValueError("Invalid unit")

        category = Bmi_category(bmi)
        bmi_rounded = round(bmi, 2)

        result_label.config(text=f"{name}'s BMI is {bmi_rounded} ({category})")

        user_data = {
            "Name": name,
            "Age": age,
            "Unit": scale,
            "Weight": weight,
            "Height": round(height, 2),
            "BMI": bmi_rounded,
            "Category": category
        }

        users.append(user_data)
        append_to_csv(user_data)
        update_analytics_display()
        clear_fields()

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))


def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    unit_combo.current(0)


root = tk.Tk()
root.title("BMI Calculator with Analytics")
root.geometry("420x500")
root.resizable(False, False)


tk.Label(root, text="Name:").grid(row=0, column=0, pady=5, sticky='e')
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0, pady=5, sticky='e')
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

tk.Label(root, text="Unit:").grid(row=2, column=0, pady=5, sticky='e')
unit_var = tk.StringVar()
unit_combo = ttk.Combobox(root, textvariable=unit_var, values=["kg/m", "lb/in"], state="readonly")
unit_combo.grid(row=2, column=1)
unit_combo.current(0)

tk.Label(root, text="Weight (kg/lb):").grid(row=3, column=0, pady=5, sticky='e')
weight_entry = tk.Entry(root)
weight_entry.grid(row=3, column=1)

tk.Label(root, text="Height (m or cm/in):").grid(row=4, column=0, pady=5, sticky='e')
height_entry = tk.Entry(root)
height_entry.grid(row=4, column=1)


result_label = tk.Label(root, text="Your BMI result will appear here", font=("Arial", 10, "bold"), fg="blue")
result_label.grid(row=5, column=0, columnspan=2, pady=5, sticky="we")


tk.Button(root, text="Calculate BMI", command=calculate_and_store).grid(row=6, column=0, columnspan=2, pady=10)


tk.Label(root, text="BMI Analytics:", font=("Arial", 10, "bold")).grid(row=7, column=0, columnspan=2)
analytics_text = tk.Text(root, height=10, width=50, state='disabled', wrap='word')
analytics_text.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

name_entry.focus()

root.mainloop()
