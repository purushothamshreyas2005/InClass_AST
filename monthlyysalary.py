basic_salary = float(input("Enter the basic salary: "))

hra = 0.20 * basic_salary
da = 0.10 * basic_salary
total_salary = basic_salary + hra + da
tax = 0.05 * total_salary
net_salary = total_salary - tax

print("\n--- Salary Details ---")
print(f"Basic Salary : {basic_salary:.2f}")
print(f"HRA          : {hra:.2f}")
print(f"DA           : {da:.2f}")
print(f"Total Salary : {total_salary:.2f}")
print(f"Tax (5%)     : {tax:.2f}")
print(f"Net Salary   : {net_salary:.2f}")
