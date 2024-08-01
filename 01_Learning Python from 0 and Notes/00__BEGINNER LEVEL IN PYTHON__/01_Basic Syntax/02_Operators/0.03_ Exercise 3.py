print("Welcome, Admin!")

employee_name = input("Enter the employee's name: ")
current_salary = float(input("Enter the employee's current salary: "))
salary_increase_percent = float(input("Enter the percentage increase in salary (in %): "))

# Calculate the new salary after the increase
salary_increase_decimal = salary_increase_percent / 100
new_salary = current_salary * (1 + salary_increase_decimal)

print(f"The new salary for employee {employee_name} is: {new_salary}")


