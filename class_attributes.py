class student:
    def __init__(self, name, std, roll_no):
        self.nm = name
        self.std = std
        self.rl_no = roll_no
         
    def getData(self):
        print("Student name: ", self.nm)
        print("Standard: ", self.std)
        print("Roll number: ", self.rl_no)
         
    def setData(self, name, std, roll_no):
        self.nm = name
        self.std = std
        self.rl_no = roll_no
         
     
stud = student("Om", "4th", 9)
stud.getData()
print() # to print a new line in between
stud_1 = student("Hari", "5th", 14) 
stud_1.getData()

#output
Student name:  Om
Standard:  4th
Roll number:  9
 
Student name:  Hari
Standard:  5th
Roll number:  14


# syntax to access the instance attributes
object = class_name(parameter1 = value_!, parameter2 = value_2, .., parameter_N = value_N)
object.parameter_1
object.parameter_2
.
.
object.parameter_N

# Example
class Rectangle:
    def __init__(self,  length, width):
        self.side_1 = length
        self.side_2 = width
         
    def area(self):
        a = self.side_1*self.side_2 
        print("Area of the rectangle is: ", a)
         
rect = Rectangle(45.0, 56.98)
 
# printing the type of object
print(type(rect)) 
 
 # accessing the values through object
print(rect.side_1)
print(rect.side_2)

# output
<class '__main__.Rectangle'>
45.0
56.98

# Accessing Class Methods And Other Instance Attributes
# Syntax:

class_name.variable_1
class_name.variable_2
.
.
class_name.variable_N

# Example 3

class student:
    school = "Universal Public School"
    batch = "2020-2021"
 
    def __init__(self, name, std, roll_no):
        self.nm = name
        self.std = std
        self.rl_no = roll_no
         
    def getData(self):
        print("Student name: ", self.nm)
        print("Standard: ", self.std)
        print("Roll number: ", self.rl_no)
         
    def setData(self, name, std, roll_no):
        self.nm = name
        self.std = std
        self.rl_no = roll_no
         
  
print("The school name is: ", student.school) 
print("The batch year is: ", student.batch, "\n")
    
stud = student("Om", "4th", 9)
stud.getData()
print() # to print a new line in between
stud_1 = student("Hari", "5th", 14) 
stud_1.getData()

# Output
The school name is:  Universal Public School
The batch year is:  2020-2021
 
Student name:  Om
Standard:  4th
Roll number:  9
 
Student name:  Hari
Standard:  5th
Roll number:  14
  
# Example (during runtime):
class Employee:
     
    # class attributes
    COMPANY = ""
    BRANCH = ""
 
    def __init__(self, name, designation, ID):
        self.name = name
        self.designation = designation
        self.id = ID
         
    def getData(self):
        print(self.name)
        print(self.designation)
        print(self.id)
        print()
         
    def setData(self, name, desig, ID):
        self.name = name
        self.designation = desig
        self.id = ID
 
def main():
    Employee.COMPANY = input("Enter the company name: ")
    Employee.BRANCH = input("Enter the branch: ")
    print()
     
    print("...The employee details are...")
    print("The company name is: ", Employee.COMPANY)
    print("The company branch is at: ", Employee.BRANCH)
     
    emp_1 = Employee("Varun", "Tirpathi", 1001)
    emp_2 = Employee("Dhanush", "Reddy", 1002)
    emp_3 = Employee("Neha", "Singh", 1003)
     
    emp_1.getData()
    emp_2.getData()
    emp_3.getData()
    
main()

#output:
Enter the company name: Microsoft
Enter the branch: Bengaluru
 
...The employee details are...      
The company name is:  Microsoft     
The company branch is at:  Bengaluru
Varun
Tirpathi
1001
 
Dhanush
Reddy
1002
 
Neha
Singh
1003
