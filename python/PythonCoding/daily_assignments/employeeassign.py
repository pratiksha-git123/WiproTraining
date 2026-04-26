class Employee:

    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    def get_emp_id(self):
        return self.__emp_id
    def get_name(self):
        return self.__name
    def get_salary(self):
        return self.__salary

    def set_name(self, name):
        self.__name = name
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Invalid Salary.")

    def display(self):
        print("\n--- Employee Details ---")
        print("ID: ", self.__emp_id)
        print("Name: ", self.__name)
        print("Salary: ", self.__salary)

    def give_hike(self, percent):
        if percent > 0:
            hike = self.__salary * percent / 100
            self.__salary += hike
            print(f"Salary increased by {percent}%")
        else:
            print("Invalid percentage.")