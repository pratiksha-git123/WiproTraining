from oops_concept.employeedetails import EmployeeDetails

#driver code
#create object for employee details class
eno  = int(input("Emp no: "))
name = input("Emp name: ")
bp = float(input("Emp basic_pay: "))
employee = EmployeeDetails(empno = eno, empname = name, basicpay = bp)
print("Employee no: ", employee.empno)
print("Employee name: ", employee.empname)
print("Basic Pay: ", employee.basicpay)
print("salary: ", employee.calculate_netsal())
