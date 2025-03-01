# Employee Management System
import json
employees = []

print("Press 1 to add employee")
print("Press 2 to Exit the program")
option = int(input("Enter 1 or 2: "))

if option == 1:
    
    while True:
        number =(input("Employee Number: "))
        name = input("Employee Name: ")
        
        # salary =eval(input("Employee Salary: "))
        salary =(input("Employee Salary: "))
                 
        try:
                    float_number = float(salary)
                    print(float_number)
        except ValueError:
                    print("The string cannot be converted to a float.")
                    continue    
    
        address = input("Employee Address: ")
        
        married = input("Employee Married? (True/False): ").capitalize()
          #while married not in ["True", "False"]:
        if married not in ["True" ,"False"]:
         print("Invalid input. Please enter 'True' or 'False'.")
         continue
    

        employee = {
            "Employee Number": number,
            "Employee Name": name,
            "Employee Salary": salary,
            "Employee Address": address,
            "Employee Married": married
        }

        employees.append(employee)

        enter = input("Would you like to add another employee? Enter yes or y to continue, or no or n to exit. ").lower()
        if enter not in ['yes', 'y']:
            break 
elif option == 2:
    print("Exiting the program.")
else:
    print("Invalid choice. Enter either 1 or 2.")

print(employees)

with open("employee_data.json","w",encoding="utf-8") as file:
   for text in employees:
      file.write(json.dumps(text,indent=4))
                