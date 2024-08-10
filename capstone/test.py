import tkinter as tk
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BudgetTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Simple Budget Tracker")
        self.geometry("800x600")
        self.configure(bg="white")

        # Data storage
        self.income = 0
        self.expenses = []

        # Setup GUI
        self.setup_gui()

    def setup_gui(self):
        # Income Entry
        self.income_label = ctk.CTkLabel(self, text="Enter Income:")
        self.income_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.income_entry = ctk.CTkEntry(self)
        self.income_entry.grid(row=0, column=1, padx=10, pady=10)
        self.add_income_button = ctk.CTkButton(self, text="Add Income", command=self.add_income)
        self.add_income_button.grid(row=0, column=2, padx=10, pady=10)

        # Expense Entry
        self.expense_label = ctk.CTkLabel(self, text="Enter Expense:")
        self.expense_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.expense_entry = ctk.CTkEntry(self)
        self.expense_entry.grid(row=1, column=1, padx=10, pady=10)
        self.category_label = ctk.CTkLabel(self, text="Category:")
        self.category_label.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.category_entry = ctk.CTkEntry(self)
        self.category_entry.grid(row=1, column=3, padx=10, pady=10)
        self.add_expense_button = ctk.CTkButton(self, text="Add Expense", command=self.add_expense)
        self.add_expense_button.grid(row=1, column=4, padx=10, pady=10)

        # Balance Display
        self.balance_label = ctk.CTkLabel(self, text="Balance: $0")
        self.balance_label.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="w")

        # Visualization Button
        self.visualize_button = ctk.CTkButton(self, text="Visualize Expenses", command=self.visualize_expenses)
        self.visualize_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

    def add_income(self):
        try:
            income = float(self.income_entry.get())
            self.income += income
            self.update_balance()
        except ValueError:
            print("Invalid input for income. Please enter a number.")

    def add_expense(self):
        try:
            expense = float(self.expense_entry.get())
            category = self.category_entry.get()
            self.expenses.append((expense, category))
            self.update_balance()
        except ValueError:
            print("Invalid input for expense. Please enter a number.")

    def update_balance(self):
        total_expenses = sum(expense for expense, category in self.expenses)
        balance = self.income - total_expenses
        self.balance_label.configure(text=f"Balance: ${balance:.2f}")

    def visualize_expenses(self):
        categories = [category for expense, category in self.expenses]
        amounts = [expense for expense, category in self.expenses]

        fig, ax = plt.subplots()
        ax.pie(amounts, labels=categories, autopct='%1.1f%%')
        ax.set_title("Expenses by Category")

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=4, column=0, columnspan=5, pady=20)

if __name__ == "__main__":
    app = BudgetTrackerApp()
    app.mainloop()
