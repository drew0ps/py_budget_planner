import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.title("Budget Planner App")
window.minsize(500, 300)
fontstyle = ("Arial", 16)

incomes = ["Salary", "Rental property", "Interest", "Other income"]
income_entries = {}

expenses = [
    "Taxes",
    "Rent",
    "Insurances",
    "Groceries",
    "Restaurant",
    "Telecom",
    "Commuting",
    "Other",
]
expense_entries = {}


def calculate_total():
    global salary_box, other_income_box
    total_cash_in = 0
    total_cash_out = 0
    for i in income_entries:
        try:
            total_cash_in += int(income_entries[i].get())
        except ValueError:
            total_cash_in += 0
    for i in expense_entries:
        try:
            total_cash_out += int(expense_entries[i].get())
        except ValueError:
            total_cash_out += 0
    total_income.configure(text=f"Total income: {total_cash_in}")
    total_expenses.configure(text=f"Total expense: {total_cash_out}")
    leftover.configure(text=f"Leftover: {total_cash_in - total_cash_out}")


title = customtkinter.CTkLabel(
    window, text="Budget Planner App", width=60, font=("Arial", 26, "bold")
)
title.grid(row=0, column=0, pady=10, padx=10, columnspan=2)


for index, income_source in enumerate(incomes):
    label = customtkinter.CTkLabel(
        window, text=income_source, width=60, font=fontstyle, justify="left"
    )
    label.grid(row=1 + index, column=0, pady=10, padx=10)
    entry = customtkinter.CTkEntry(window)
    entry.grid(row=1 + index, column=1)
    income_entries[income_source] = entry
    line = index + 1


for index, expense in enumerate(expenses):
    label = customtkinter.CTkLabel(
        window, text=expense, width=60, font=fontstyle, justify="left"
    )
    label.grid(row=1 + index + line, column=0, pady=10, padx=10)
    entry = customtkinter.CTkEntry(window)
    entry.grid(row=1 + index + line, column=1)
    expense_entries[expense] = entry
    line = line + index + 1


calculate = customtkinter.CTkButton(
    window, width=360, text="Calculate", command=calculate_total
)
calculate.grid(row=line + 1, column=0, pady=10, padx=10, columnspan=2)

total_income = customtkinter.CTkLabel(
    window, justify="left", width=60, font=fontstyle, text_color="green"
)
total_income.grid(row=line + 2, column=0)
total_income.configure(text="Total Income:")

total_expenses = customtkinter.CTkLabel(
    window, width=60, font=fontstyle, justify="left", text_color="red"
)
total_expenses.grid(row=line + 3, column=0)
total_expenses.configure(text="Total expenses:")

leftover = customtkinter.CTkLabel(window, width=60, font=fontstyle, text_color="green")
leftover.grid(row=line + 4, column=0)
leftover.configure(text=f"Leftover: ")


window.mainloop()
