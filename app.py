import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import json, os
from datetime import datetime
import matplotlib.pyplot as plt

DATA_FILE = "transactions.json"
BUDGET_FILE = "budget.json"
CATBUDGET_FILE = "category_budgets.json"
CONFIG_FILE = "app_config.json"

def load_json(filename, default):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except:
            return default
    return default

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def get_month():
    return datetime.now().strftime("%Y-%m")

class App(tb.Window):
    def __init__(self):
        super().__init__(themename="cosmo")
        self.title("Personal Finance Tracker")
        self.geometry("420x700")
        self.resizable(False, False)

        # Load data
        self.transactions = load_json(DATA_FILE, [])
        self.budget = load_json(BUDGET_FILE, {"monthly": 0})
        self.catbudgets = load_json(CATBUDGET_FILE, {})
        self.config = load_json(CONFIG_FILE, {"last_month": get_month(), "rollover": 0, "theme": "cosmo"})

        # Handle monthly rollover/reset
        self.check_monthly_reset()

        # Categories
        self.categories = ["Food", "Transport", "Bills", "Shopping", "Health", "Income", "Other"]

        # Style reference

        self.current_frame = None
        self.show_main_menu()

    def check_monthly_reset(self):
        now_month = get_month()
        if self.config.get("last_month") != now_month:
            # Compute savings rollover (income - expenses for last month)
            total_income = sum(float(t["amount"]) for t in self.transactions if t["category"] == "Income")
            total_expense = sum(float(t["amount"]) for t in self.transactions if t["category"] != "Income")
            rollover = total_income - total_expense
            self.config["rollover"] = max(0, rollover)
            self.transactions = []
            self.config["last_month"] = now_month
            save_json(DATA_FILE, self.transactions)
            save_json(CONFIG_FILE, self.config)

    def show_main_menu(self):
        if self.current_frame: self.current_frame.destroy()
        self.current_frame = MainMenu(self)
        self.current_frame.pack(fill="both", expand=True)

    def toggle_theme(self):
        current = self.style.theme.name
        if current == "cosmo":
            self.style.theme_use("superhero")
            self.config["theme"] = "superhero"
        else:
            self.style.theme_use("cosmo")
            self.config["theme"] = "cosmo"
        save_json(CONFIG_FILE, self.config)

class MainMenu(ttk.Frame):
    def __init__(self, app):
        super().__init__(app, padding=15)
        self.app = app
        ttk.Label(self, text="Personal Finance Tracker", font=("Segoe UI", 20, "bold")).pack(pady=14)
        btn_style = {"bootstyle": "success-outline", "width": 24, "padding": 10}
        ttk.Button(self, text="Set Monthly Budget", command=self.set_budget, **btn_style).pack(pady=10)
        ttk.Button(self, text="Set Category Budgets", command=self.set_cat_budget, **btn_style).pack(pady=10)
        ttk.Button(self, text="Add Transaction", command=self.add_txn, **btn_style).pack(pady=10)
        ttk.Button(self, text="View Transactions", command=self.view_txns, **btn_style).pack(pady=10)
        ttk.Button(self, text="Summary", command=self.summary, **btn_style).pack(pady=10)
        ttk.Button(self, text="Toggle Dark Mode", command=app.toggle_theme, **btn_style).pack(pady=10)
        ttk.Button(self, text="Search Transactions", command=self.search_txn, **btn_style).pack(pady=10)
        ttk.Label(self, text=f"Rollover Savings: ₹{self.app.config.get('rollover',0):,.2f}", font=("Segoe UI", 12, "italic")).pack(pady=6)
    def set_budget(self):
        SetBudgetWindow(self.app)
    def set_cat_budget(self):
        SetCatBudgetWindow(self.app)
    def add_txn(self):
        AddTransactionWindow(self.app)
    def view_txns(self):
        ViewTransactionsWindow(self.app)
    def summary(self):
        SummaryWindow(self.app)
    def search_txn(self):
        SearchWindow(self.app)

class SetBudgetWindow(tk.Toplevel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.title("Set Monthly Budget")
        self.geometry("320x180")
        self.resizable(False, False)
        ttk.Label(self, text="Set Monthly Budget (₹)", font=("Segoe UI", 15, "bold")).pack(pady=18)
        self.var = tk.StringVar(value=str(self.app.budget.get("monthly", "")))
        ttk.Entry(self, textvariable=self.var, font=("Segoe UI", 15), width=18, justify="center").pack(pady=10)
        ttk.Button(self, text="Save", command=self.save, bootstyle="success").pack(pady=13)
    def save(self):
        try:
            val = float(self.var.get())
            self.app.budget["monthly"] = val
            save_json(BUDGET_FILE, self.app.budget)
            tb.toast("Monthly budget updated!", title="Success", duration=1100)
            self.destroy()
        except:
            tb.toast("Invalid value", duration=1300, bootstyle="danger")

class SetCatBudgetWindow(tk.Toplevel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.title("Set Category Budgets")
        self.geometry("350x420")
        self.resizable(False, False)
        ttk.Label(self, text="Set Budgets for Categories", font=("Segoe UI", 14, "bold")).pack(pady=10)
        self.entries = {}
        for i, cat in enumerate(self.app.categories):
            ttk.Label(self, text=f"{cat} (₹)").pack()
            var = tk.StringVar(value=str(self.app.catbudgets.get(cat, "")))
            entry = ttk.Entry(self, textvariable=var, width=18)
            entry.pack(pady=2)
            self.entries[cat] = var
        ttk.Button(self, text="Save", command=self.save, bootstyle="success").pack(pady=18)
    def save(self):
        for cat, var in self.entries.items():
            try:
                val = float(var.get())
                self.app.catbudgets[cat] = val
            except:
                self.app.catbudgets[cat] = 0
        save_json(CATBUDGET_FILE, self.app.catbudgets)
        tb.toast("Category budgets updated!", title="Success", duration=1100)
        self.destroy()

class AddTransactionWindow(tk.Toplevel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.title("Add Transaction")
        self.geometry("350x400")
        self.resizable(False, False)
        ttk.Label(self, text="Add Transaction", font=("Segoe UI", 15, "bold")).pack(pady=12)
        form = ttk.Frame(self)
        form.pack(pady=4)
        ttk.Label(form, text="Amount (₹):").grid(row=0, column=0, sticky="e", padx=8, pady=8)
        ttk.Label(form, text="Category:").grid(row=1, column=0, sticky="e", padx=8, pady=8)
        ttk.Label(form, text="Note:").grid(row=2, column=0, sticky="e", padx=8, pady=8)
        ttk.Label(form, text="Date:").grid(row=3, column=0, sticky="e", padx=8, pady=8)

        self.amount_var = tk.StringVar()
        self.category_var = tk.StringVar()
        self.note_var = tk.StringVar()
        self.date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))

        ttk.Entry(form, textvariable=self.amount_var, width=16).grid(row=0, column=1)
        ttk.Combobox(form, textvariable=self.category_var, values=self.app.categories, state="readonly", width=14).grid(row=1, column=1)
        ttk.Entry(form, textvariable=self.note_var, width=16).grid(row=2, column=1)
        ttk.Entry(form, textvariable=self.date_var, width=16).grid(row=3, column=1)

        ttk.Button(self, text="Save", command=self.save_txn, bootstyle="success").pack(pady=15)
    def save_txn(self):
        try:
            amt = float(self.amount_var.get())
            cat = self.category_var.get()
            note = self.note_var.get()
            date = self.date_var.get()
            if not (amt and cat and date): raise ValueError
        except:
            tb.toast("Enter valid values!", duration=1600, bootstyle="danger")
            return
        txn = {"amount": amt, "category": cat, "note": note, "date": date}
        self.app.transactions.append(txn)
        save_json(DATA_FILE, self.app.transactions)
        # Alert if category budget exceeded (skip Income)
        if cat != "Income":
            spent = sum(float(t["amount"]) for t in self.app.transactions if t["category"] == cat and t["category"] != "Income")
            budget = self.app.catbudgets.get(cat, 0)
            if budget and spent > budget:
                tb.toast(f"⚠️ {cat} budget exceeded!", duration=1800, bootstyle="warning")
        tb.toast("Transaction saved!", duration=1100, bootstyle="success")
        self.destroy()

class ViewTransactionsWindow(tk.Toplevel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.title("Transactions")
        self.geometry("530x420")
        self.resizable(False, False)
        ttk.Label(self, text="Transactions", font=("Segoe UI", 15, "bold")).pack(pady=10)
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(self, textvariable=self.search_var, width=28)
        search_entry.pack()
        search_entry.bind("<KeyRelease>", lambda e: self.refresh_list())
        self.tree = ttk.Treeview(self, columns=("Amount", "Category", "Note", "Date"), show="headings", height=13)
        for col in ("Amount", "Category", "Note", "Date"):
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=110 if col!="Note" else 160)
        self.tree.pack(pady=6)
        btns = ttk.Frame(self)
        btns.pack()
        ttk.Button(btns, text="Edit", command=self.edit_selected, width=9, bootstyle="info-outline").grid(row=0, column=0, padx=3)
        ttk.Button(btns, text="Delete", command=self.delete_selected, width=9, bootstyle="danger-outline").grid(row=0, column=1, padx=3)
        ttk.Button(btns, text="Export CSV", command=self.export_csv, width=11).grid(row=0, column=2, padx=3)
        self.refresh_list()
    def refresh_list(self):
        keyword = self.search_var.get().lower()
        data = self.app.transactions
        if keyword:
            data = [t for t in data if keyword in str(t["amount"]).lower() or keyword in t["category"].lower() or keyword in t["note"].lower() or keyword in t["date"]]
        self.tree.delete(*self.tree.get_children())
        for idx, t in enumerate(data):
            self.tree.insert("", "end", iid=idx, values=(t["amount"], t["category"], t["note"], t["date"]))
        self.filtered = data
    def edit_selected(self):
        item = self.tree.focus()
        if not item: return
        idx = int(item)
        txn = self.filtered[idx]
        EditTransactionWindow(self.app, txn, self.refresh_list)
    def delete_selected(self):
        item = self.tree.focus()
        if not item: return
        idx = int(item)
        txn = self.filtered[idx]
        self.app.transactions.remove(txn)
        save_json(DATA_FILE, self.app.transactions)
        self.refresh_list()
        tb.toast("Transaction deleted.", duration=1100, bootstyle="danger")
    def export_csv(self):
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Export as CSV")
        if not filename: return
        try:
            import csv
            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Amount", "Category", "Note", "Date"])
                for t in self.filtered:
                    writer.writerow([t["amount"], t["category"], t["note"], t["date"]])
            tb.toast("Exported to CSV.", duration=1200)
        except Exception as e:
            tb.toast(f"Failed to export: {e}", duration=2200, bootstyle="danger")

class EditTransactionWindow(tk.Toplevel):
    def __init__(self, app, txn, callback):
        super().__init__()
        self.app = app
        self.txn = txn
        self.callback = callback
        self.title("Edit Transaction")
        self.geometry("350x290")
        ttk.Label(self, text="Edit Transaction", font=("Segoe UI", 15, "bold")).pack(pady=10)
        form = ttk.Frame(self)
        form.pack(pady=5)
        self.amount_var = tk.StringVar(value=str(txn["amount"]))
        self.category_var = tk.StringVar(value=txn["category"])
        self.note_var = tk.StringVar(value=txn["note"])
        self.date_var = tk.StringVar(value=txn["date"])
        ttk.Label(form, text="Amount:").grid(row=0, column=0, sticky="e", padx=8, pady=8)
        ttk.Entry(form, textvariable=self.amount_var, width=15).grid(row=0, column=1)
        ttk.Label(form, text="Category:").grid(row=1, column=0, sticky="e", padx=8, pady=8)
        ttk.Combobox(form, textvariable=self.category_var, values=self.app.categories, state="readonly", width=13).grid(row=1, column=1)
        ttk.Label(form, text="Note:").grid(row=2, column=0, sticky="e", padx=8, pady=8)
        ttk.Entry(form, textvariable=self.note_var, width=15).grid(row=2, column=1)
        ttk.Label(form, text="Date:").grid(row=3, column=0, sticky="e", padx=8, pady=8)
        ttk.Entry(form, textvariable=self.date_var, width=15).grid(row=3, column=1)
        ttk.Button(self, text="Save", command=self.save, bootstyle="success").pack(pady=13)
    def save(self):
        try:
            self.txn["amount"] = float(self.amount_var.get())
            self.txn["category"] = self.category_var.get()
            self.txn["note"] = self.note_var.get()
            self.txn["date"] = self.date_var.get()
            save_json(DATA_FILE, self.app.transactions)
            self.callback()
            self.destroy()
            tb.toast("Transaction updated!", duration=1100, bootstyle="success")
        except:
            tb.toast("Invalid value(s).", duration=1800, bootstyle="danger")

class SummaryWindow(tk.Toplevel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.title("Monthly Summary")
        self.geometry("390x390")
        self.resizable(False, False)
        ttk.Label(self, text="Monthly Summary", font=("Segoe UI", 16, "bold")).pack(pady=11)
        income = sum(float(t["amount"]) for t in self.app.transactions if t["category"] == "Income")
        expense = sum(float(t["amount"]) for t in self.app.transactions if t["category"] != "Income")
        savings = income - expense
        ttk.Label(self, text=f"Total Income: ₹{income:.2f}").pack()
        ttk.Label(self, text=f"Total Expenses: ₹{expense:.2f}").pack()
        ttk.Label(self, text=f"Savings: ₹{savings:.2f}").pack()
        ttk.Label(self, text="Category Budgets & Spent:", font=("Segoe UI", 12, "underline")).pack(pady=10)
        for cat in self.app.catbudgets:
            spent = sum(float(t["amount"]) for t in self.app.transactions if t["category"] == cat and t["category"] != "Income")
            budget = self.app.catbudgets[cat]
            ttk.Label(self, text=f"{cat}: ₹{spent:.2f} / ₹{budget:.2f}").pack()
        ttk.Button(self, text="Show Pie Chart", command=self.show_pie_chart, bootstyle="info").pack(pady=15)
    def show_pie_chart(self):
        from collections import Counter
        cats = [t['category'] for t in self.app.transactions if t['category'] != "Income"]
        if not cats:
            tb.toast("No expenses to plot.", duration=1400, bootstyle="warning")
            return
        cat_totals = Counter()
        for t in self.app.transactions:
            if t['category'] != "Income":
                cat_totals[t['category']] += float(t['amount'])
        plt.figure(figsize=(5,5))
        plt.pie(cat_totals.values(), labels=cat_totals.keys(), autopct='%1.1f%%', startangle=90)
        plt.title('Expense Distribution')
        plt.show()

class SearchWindow(tk.Toplevel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.title("Search Transactions")
        self.geometry("530x400")
        self.resizable(False, False)
        ttk.Label(self, text="Search Transactions", font=("Segoe UI", 15, "bold")).pack(pady=10)
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(self, textvariable=self.search_var, width=26)
        search_entry.pack()
        search_entry.bind("<KeyRelease>", lambda e: self.refresh_list())
        self.tree = ttk.Treeview(self, columns=("Amount", "Category", "Note", "Date"), show="headings", height=13)
        for col in ("Amount", "Category", "Note", "Date"):
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=110 if col!="Note" else 160)
        self.tree.pack(pady=6)
        self.refresh_list()
    def refresh_list(self):
        keyword = self.search_var.get().lower()
        data = self.app.transactions
        if keyword:
            data = [t for t in data if keyword in str(t["amount"]).lower() or keyword in t["category"].lower() or keyword in t["note"].lower() or keyword in t["date"]]
        self.tree.delete(*self.tree.get_children())
        for idx, t in enumerate(data):
            self.tree.insert("", "end", iid=idx, values=(t["amount"], t["category"], t["note"], t["date"]))

if __name__ == "__main__":
    App().mainloop()
