# 💼 Employee Payroll System Using Python

## 📌 Project Overview

The **Employee Payroll System** is a console-based Python application designed to manage employee information and calculate employee salaries efficiently.

It allows users to add employees, calculate salaries, generate payslips, search employee records, and save payroll information using file handling.

This project demonstrates **Object-Oriented Programming (OOP)** concepts, mathematical calculations, data structures, and file handling in Python.

## 🚀 Features

- **Add Employees:** Add new employees with their name, unique employee ID, and basic salary.
- **Calculate Salary:** Calculate gross and net salary using HRA, DA, and PF.
- **Generate Payslips:** Generate detailed salary slips containing employee information and salary breakdown.
- **Search Employees:** Search for employees using their unique employee ID.
- **Save Payroll Data:** Save employee information and payroll records for future use.
- **Duplicate Prevention:** Prevent adding employees with duplicate employee IDs.
- **Salary Breakdown:** Display basic salary, HRA, DA, PF, gross salary, and net salary.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Programming Paradigm:** Object-Oriented Programming (OOP)
- **Data Structures:** Python Lists
- **File Handling:** Reading and writing employee records
- **Interface:** Command-Line Interface (CLI)
- **Modules:** `datetime` for payslip date and time

## 🧠 OOP Concepts Implemented

| Concept | Implementation |
|---|---|
| Classes and Objects | Employee objects represent individual employees |
| Encapsulation | Employee information and salary calculations are organized inside classes |
| Abstraction | Salary calculation details are handled through methods |
| Inheritance | Can be added to support different employee types |
| Polymorphism | Can be added to implement different salary calculation methods |

## 🏗️ Classes Used

### 1. Employee Class

The `Employee` class represents an employee and stores their personal and salary information.

**Attributes:**
- `employee_name`
- `employee_id`
- `employee_basic_salay`

**Methods:**
- `__init__()` – Initializes employee information.
- `display()` – Displays employee details.
- `salary()` – Calculates employee salary components.

### 2. Employee_Payroll_System Class

The `Employee_Payroll_System` class manages employee records and payroll operations.

**Responsibilities:**
- Add new employees.
- Prevent duplicate employee IDs.
- Search employee records.
- Calculate salaries.
- Generate payslips.
- Save employee payroll information.

## 📂 Project Structure

```text
Employee-Payroll-System/
│
├── employee_payroll.py
├── employee.txt
├── payslips/
└── README.md
```

*This is a suggested structure. Actual filenames and payslip storage depend on the implementation.*

## ⚙️ Installation and Setup

**Step 1: Clone the repository**

```bash
git clone https://github.com/USERNAME/Employee-Payroll-System.git
```

**Step 2: Navigate to the project folder**

```bash
cd Employee-Payroll-System
```

**Step 3: Run the application**

```bash
python employee_payroll.py
```

Replace `USERNAME` with your GitHub username and use your actual Python filename.

No external Python libraries are required.

## 💻 Example Program Menu

```text
====== Employee Payroll System ======

1. Add Employee
2. Display Employees
3. Search Employee
4. Calculate Salary
5. Generate Payslip
6. Save Payroll Data
7. Exit

Enter Your Choice:
```

*The menu above is illustrative and should be adjusted to match the final code.*

## 💰 Salary Calculation

The payroll system calculates employee salaries using the following components:

| Component | Calculation |
|---|---|
| Basic Salary | Employee's base salary |
| HRA (House Rent Allowance) | 20% of Basic Salary |
| DA (Dearness Allowance) | 10% of Basic Salary |
| PF (Provident Fund) | 12% of Basic Salary |
| Gross Salary | Basic Salary + HRA + DA |
| Net Salary | Gross Salary − PF |

### Salary Formulas

```python
HRA = 0.20 * basic_salary
DA = 0.10 * basic_salary
PF = 0.12 * basic_salary

Gross_Salary = basic_salary + HRA + DA
Net_Salary = Gross_Salary - PF
```

## 📄 Example Employee Payslip

```text
========================================
           EMPLOYEE PAYSLIP
========================================

Employee Name  : Rahul
Employee ID    : EMP101
Basic Salary   : 30000.00

----------------------------------------
Salary Breakdown
----------------------------------------

HRA (20%)      : 6000.00
DA (10%)       : 3000.00
PF (12%)       : 3600.00

Gross Salary   : 39000.00
Net Salary     : 35400.00

========================================
```

## 💾 File Storage

The application can store employee payroll information in a text file.

Example records:

```text
EMP101,Rahul,30000.0
EMP102,Priya,40000.0
EMP103,Aman,35000.0
```

Each record contains:

`Employee_ID,Employee_Name,Basic_Salary`

Employee information is managed using Python objects and lists.

## 🔄 How the Application Works

1. The user starts the Employee Payroll System.
2. The application displays the available payroll operations.
3. The user adds employees by entering their name, ID, and basic salary.
4. Employee records are stored as objects of the `Employee` class.
5. The system calculates HRA, DA, PF, gross salary, and net salary.
6. The user can search for employees using their employee ID.
7. Payslips are generated using employee information and calculated salary components.
8. Employee records can be saved for future use.

## 📚 Python Concepts Practiced

- Classes and Objects
- Object-Oriented Programming
- Constructors (`__init__`)
- Instance Attributes and Methods
- Encapsulation
- Lists and Loops
- Conditional Statements
- Exception Handling
- Mathematical Calculations
- File Handling
- String Formatting
- Date and Time Handling
- Input Validation

## 🎯 Learning Objectives

- Apply Python OOP concepts in a practical payroll project.
- Understand employee record management.
- Implement salary calculation using HRA, DA, and PF.
- Generate employee payslips.
- Manage multiple employees using Python lists.
- Practice file handling for payroll records.
- Improve Python programming and problem-solving skills.

## 🔮 Future Enhancements

- Integrate SQLite or MySQL for employee data storage.
- Develop a graphical user interface using Tkinter.
- Generate PDF payslips.
- Add employee attendance tracking.
- Calculate bonuses and overtime payments.
- Implement tax deductions.
- Support different employee categories.
- Generate monthly payroll reports.

## ⭐ Support

If you find this project helpful, consider giving the repository a star ⭐ on GitHub.
