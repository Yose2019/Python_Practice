# the module consists of the operations which can be done on a student
# the class is studentOperations 
# the methods include - add, delete, edit, view, report, exit 
# the students would be part of a dictionary where in the id would be the key as it would be unique 
# the value in the key value pair is the student object 

import sys 
from student import student

class studentOperations :
    students = {}

    def add(self, id, name, age, gender, subject1, mark_s1, subject2, mark_s2):
        # check if there is no student who already exists in the class 
        if self.students.get(id, 0) != 0:
            print("The id already exists - view, report, edit are possible")
            return 
        else:
            self.students[id] = student(id, name, age, gender, subject1, mark_s1, subject2, mark_s2) 
            print(f"{id} : {name} - added succesfully!!")
            return      

    def delete(self, id):
        # delete using id 
        # check whether exists or not before deleting
        # use the del command 
        if len(self.students) == 0:
            print("No students to perform operaion")
            return 
        if self.students.get(id, 0) == 0:
            print(f"Student id : {id} does not exist")
            return
        else:
            del self.students[id]

    def edit(self, id):
        # based on the user choice editing occurs 
        # using the id , check whether id exists or not 
        if len(self.students) == 0:
            print("No students to perform operaion")
            return 
        if self.students.get(id, 0) == 0:
            print(f"Student id : {id} does not exist")
            return 
        ch = input("Would you like to edit the name : y/n :").lower()
        if ch == 'y':
            self.students[id].name = input("Enter the changed name : ")
        ch = input("Would you like to edit the age : y/n :").lower()
        if ch == 'y':
            self.students[id].age = input("Enter the changed age : ")
        ch = input("Would you like to edit the gender : y/n :").lower()
        if ch == 'y':
           self.students[id].gender = input("Enter the changed gender : ")
        ch = input("Would you like to edit the subject 1 : y/n :").lower()
        if ch == 'y':
            self.students[id].subject1 = input("Enter the changed subject 1 : ")
        ch = input("Would you like to edit the marks of subject 1 : y/n :")
        if ch == 'y':
            self.students[id].mark_s1 = input("Enter the changed marks of subject 1 : ")
        ch = input("Would you like to edit the subject 2 : y/n :").lower()
        if ch == 'y':
            self.students[id].subject2 = input("Enter the changed subject 2 : ")
        ch = input("Would you like to edit the marks of subject 2 : y/n :").lower()
        if ch == 'y':
           self.students[id].mark_s2 = input("Enter the changed marks of subject 2 : ")

    def view(self, choice):
        # give choice to user to view all the students or a specific one 
        if len(self.students) == 0:
            print("No students to perform operaion")
            return
        if choice == 'A':
            for id in self.students.keys():
                print("Id".ljust(50) + f" : {self.students[id].id}")
                print("Name".ljust(50) + f" : {self.students[id].name}")
                print("Age".ljust(50) + f" : {self.students[id].age}")
                print("Gender".ljust(50) + f" : {self.students[id].gender}")
                print("Marks".center(65, '-'))
                print(self.students[id].subject1.ljust(20) + f" : {self.students[id].mark_s1}")
                print(self.students[id].subject2.ljust(20) + f" : {self.students[id].mark_s2}")
                print("*" * 70)
        elif choice == 'I':
            id = input("Enter the id to be viewed : ")
            if id not in self.students.keys():
                print(f"Student id : {id} does not exist")
                return
            else:
                print("Id".ljust(50) + f" : {self.students[id].id}")
                print("Name".ljust(50) + f" : {self.students[id].name}")
                print("Age".ljust(50) + f" : {self.students[id].age}")
                print("Gender".ljust(50) + f" : {self.students[id].gender}")
                print("Marks".center(65, '-'))
                print(self.students[id].subject1.ljust(20) + f" : {self.students[id].mark_s1}")
                print(self.students[id].subject2.ljust(20) + f" : {self.students[id].mark_s2}")
                
                
    def report(self, id):
        if len(self.students) == 0:
            print("No students to perform operaion")
            return
        if self.students.get(id, 0) == 0:
            print(f"Student id : {id} does not exist")
            return
        else:
            print("Id".ljust(50) + f" : {self.students[id].id}")
            print("Name".ljust(50) + f" : {self.students[id].name}")
            print("Marks".center(65))
            print(self.students[id].subject1.ljust(20) + f" : {self.students[id].mark_s1}")
            print(self.students[id].subject2.ljust(20) + f" : {self.students[id].mark_s2}")
            percentage = (self.students[id].mark_s1 + self.students[id].mark_s2) / 200 * 100
            print(f"Percentage is : {percentage:2f}")
            if percentage >= 35 :
                print("PASS".center(70))
            else:
                print("FAIL".center(70))

    def exit(self):
        sys.exit()