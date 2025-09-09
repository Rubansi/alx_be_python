monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
rate = 0.05
time = 12
projected_savings = monthly_savings * time + (monthly_savings * time * rate ) 

print(f"Projected savings after one year, with interest, is: {projected_savings}")