from tkinter import *


def calculate_commission():
    qty = float(quantity.get())
    percentage = float(commission_per.get())
    gross = float(gross_sales.get())
    labor_rate = float(labor_charge.get())
    commission = percentage/100 * gross
    net_amount = gross - (commission + qty * labor_rate)
    commission_amount.config(text=commission)
    net_sales.config(text=net_amount)


window = Tk()
window.title("Commission Calculator")
window.config(padx=25, pady=25)

# Entry for Quantity
quantity = Entry()
quantity.grid(column=1, row=0)

# Label for unit
unit = Label(text="Units")
unit.grid(column=2, row=0)

# Entry for gross amount
gross_sales = Entry()
gross_sales.grid(column=1, row=1)

# Label for gross sales
gross_label = Label(text="Gross Amount")
gross_label.grid(column=2, row=1)

# Commission % Entry
commission_per = Entry()
commission_per.grid(column=1, row=2)

# Commission % label
label_per = Label(text="Commission %")
label_per.grid(column=2, row=2)

# Labor charge per unit
labor_charge = Entry()
labor_charge.grid(column=1, row=3)

# Label for labor charge
labor_label = Label(text="Per Unit Labor Charge")
labor_label.grid(column=2, row=3)

# Commission Calculated
commission_amount = Label(text=0)
commission_amount.grid(column=1, row=4)

# Commission Label
commission_label = Label(text="Commission")
commission_label.grid(column=2, row=4)

# Label for net amount
net_sales = Label(text=0)
net_sales.grid(column=1, row=5)

# Label for net sales
net_label = Label(text="Net Amount")
net_label.grid(column=2, row=5)

# Calculate button
calculate_button = Button(text="Calculate", command=calculate_commission)
calculate_button.grid(column=1, row=6)

window.mainloop()
