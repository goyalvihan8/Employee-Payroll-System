from datetime import datetime
from abc import ABC,abstractmethod
import csv
import os
import math

# ==========================================================
# 1. ABSTRACT BASE CLASS
# ==========================================================

class Employee(ABC):
    
    def __init__(self,employee_name,employee_id,employee_basic_salary):

        # Encapsulation - Private Attributes
        self.__employee_name=employee_name
        self.__employee_id=employee_id
        self.__employee_basic_salary=employee_basic_salary

    # ---------------- DISPLAY ----------------  
    
    def display(self): 
        print("Employee Name:",self.__employee_name)
        print("Employee Id:",self.__employee_id)
        print("Employee Basic Salary:",self.__employee_basic_salary)

        
    def salary(self):
        HRA=0.2*self.__employee_basic_salary 
        DA=0.1*self.__employee_basic_salary
        Gross_Salary=self.__employee_basic_salary + HRA + DA 
        PF = .12*self.__employee_basic_salary
        Net_Salary = Gross_Salary-PF
        return Net_Salary,HRA,DA,Gross_Salary,PF

    # ---------------- GETTERS ----------------
        
    def get_employee_name(self):
        return self.__employee_name
    def get_employee_id(self):
        return self.__employee_id
    def get_employee_basic_salary(self):
        return self.__employee_basic_salary
        
    # ---------------- SETTER ----------------
        
    def set_employee_basic_salary(self,employee_basic_salary):
        self.__employee_basic_salary=employee_basic_salary

    # Abstraction   
    @abstractmethod
    def employee_department(self):
        pass

# ==========================================================
# 2. DERIVED CLASS - INHERITANCE
# ==========================================================    
class Department(Employee):
    def employee_department(self):
        return "HR Department"

# ==========================================================
# 3.  EMPLOYEE PAYROLL SYSTEMCLASS
# ==========================================================        
class Employee_Payroll_System: 
    
    def __init__(self):
        self.employees=[]

    # ------------------------------------------------------
    # CREATE EMPLOYEE
    # ------------------------------------------------------    
    def add_employee(self): 
        employee_name=input("Enter The Name Of The Employee:")
        employee_id=input("Enter The Employee Id:")

        # Check duplicate Employee Id
        for employee in self.employees:
            
            if employee.get_employee_id()==employee_id:
                print("Employee Id Already Exist...")
                return
                
        try:
            
            employee_basic_salary=float(input("Enter The Basic Salary Of The Employee:"))
            
            if employee_basic_salary <=0:
                print("Salary Must Be Greater Than Zero..")
                return
                
        except ValueError:
            
            print("Invalid Salary..")
            return

        # Create object of derived class
        employee =Department(
            employee_name,
            employee_id,
            employee_basic_salary)
        
        self.employees.append(employee)
        
        print("Employee Added Successfully...")

    # ------------------------------------------------------
    # CALCULATE SALARY
    # ------------------------------------------------------
    def calculate_salary(self): 
        
        employee_id=input("Enter The Employee Id:")
        
        for employee in self.employees:
            
            if employee.get_employee_id()==employee_id:
                
                Net_Salary,HRA,DA,Gross_Salary,PF = employee.salary()
                print("Net Salary:",Net_Salary)
                return
                
        print("Employee Not Found..")

    # ------------------------------------------------------
    # GENERATE PAYSLIP
    # ------------------------------------------------------    
    def generate_payslip(self):
        
        employee_id=input("Enter The Employee Id:")
        
        for employee in self.employees:
            
            if employee.get_employee_id()==employee_id:
                
                print("\n======= Employee Payslip ======")
                print("Employee Id  : ",employee.get_employee_id())
                print("Employee Name : ",employee.get_employee_name())
                now = datetime.now()
                print("Month : ", now.strftime("%B"))
                print("Year  : " ,now.year)
                print("\n")
                print("Basic Salary : ",employee.get_employee_basic_salary())
                Net_Salary,HRA,DA,Gross_Salary,PF = employee.salary()
                print("HRA (20%) : ",HRA)
                print("DA (10%) : ",DA)
                print("---------------------")
                print("----------")
                print("Gross Salary : ",Gross_Salary)
                print("\n")
                print("PF Deduction (12%) : ",PF)
                print("---------------------")
                print("----------")
                print("Net Salary : ",Net_Salary)
                print("\n")
                print("=====================")
                print("=========")
                return
                
        print("Employee Not Found..")

    # ------------------------------------------------------
    # SEARCH EMPLOYEE
    # ------------------------------------------------------
    def search_employee(self):
        
        employee_id=input("Enter The Employee Id:")
        
        for employee in self.employees:
            
            if employee.get_employee_id()==employee_id:
                
                print("Employee Found..")
                employee.display()
                return
                
        print("Employee Not Found..")

    # ------------------------------------------------------
    # SAVE RECORD TO FILE
    # ------------------------------------------------------   
    def save_payroll(self):
        
        try:
            
            with open("employee.csv",'w') as em:
                
                em.write("Name,ID,Basic Salary,HRA,DA,Gross Salary,PF,Net Salary\n")
                
                for employee in self.employees:
                    
                    Net_Salary, HRA, DA, Gross_Salary, PF = employee.salary()
                    em.write(employee.get_employee_name() + "," +
                        employee.get_employee_id() + "," + 
                        str(employee.get_employee_basic_salary()) + "," + 
                        str(HRA) + "," +
                        str(DA) + "," +
                        str(Gross_Salary) + "," +
                        str(PF) + "," +
                        str(Net_Salary) + "\n")
                    
            print("Payroll Saved....")
            
        except OSError:
            
            print("Error While Saving File...")

    # ------------------------------------------------------
    # LOAD RECORD FROM FILE
    # ------------------------------------------------------        
   
    def load_payroll(self):
    
        try:
            with open("employee.csv", "r", newline="") as em:
    
                reader = csv.reader(em)
    
                # Skip CSV header
                next(reader, None)
    
                for data in reader:
    
                    if len(data) != 8:
                        continue
    
                    employee_name = data[0].strip()
                    employee_id = data[1].strip()
    
                    if not employee_name or not employee_id:
                        continue
    
                    # Check duplicate employee ID
                    if any(
                        employee.get_employee_id() == employee_id
                        for employee in self.employees
                    ):
                        continue
    
                    try:
                        employee_basic_salary = float(data[2])
    
                        if not math.isfinite(employee_basic_salary):
                            continue
    
                        if employee_basic_salary <= 0:
                            continue
    
                    except ValueError:
                        continue
    
                    employee = Department(
                        employee_name,
                        employee_id,
                        employee_basic_salary
                    )
    
                    self.employees.append(employee)
    
            print("Previous Data Loaded Successfully...")
    
        except FileNotFoundError:
            print("No Previous Record Found.")
    
        except (OSError, csv.Error):
            print("Error While Reading File...")

        
                    
                



      
system=Employee_Payroll_System()

system.load_payroll()

while True:
    
    print("\n===== Employee Payroll System =====")
    print("1. Add Employee")
    print("2. Calculate Salary")
    print("3. Generate Payslip")
    print("4. Search Employee")
    print("5. Save Payroll Data")
    print("6. Exit")
    
    choice=input("Enter Your Choice:")
    
    if choice=="1":
        system.add_employee()
        
    elif choice=="2":
        system.calculate_salary()
        
    elif choice=="3":
        system.generate_payslip()
        
    elif choice=="4":
        system.search_employee()
        
    elif choice=="5":
        system.save_payroll()
        
    elif choice=="6":
        system.save_payroll()  
        print("Exit Program...")
        break
        
    else:
        print("Invalid Input")

                
                
                
