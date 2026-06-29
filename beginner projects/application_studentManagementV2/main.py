# the module is the actual UI which interacts with the user 
# now in the version 2, there are two kinds of user, one would be the admin who would add the subjects to the subject catalogue 
# the other class of users would be others 
# each will have a password - simple as of now
# the formalizing or sophisticating of these things would be done in latr versions of the application

from studentOperations import studentOperations
from subjectList import subjectList

s = studentOperations()

while True:
    user = input("Verify user identity : \n1.Admin(A)\n2.Other(O)\nEnter the type : ").upper()
    userPassword = input("Enter the password : ")
    if user == 'A' and userPassword == 'admin':
        sl = subjectList()
        while True:
            print("Please select an operation to perform : ")
            print("1. Add\n2. Delete\n3. Edit\n4. View\n 5. User Menu")
            op = input()
            if op == '1':
                subId = input("Enter the subject Id : ")
                sub = input("Enter the subject name : ")
                sl.addSubject(subId, sub)

            elif op == '2':
                choice = input("Enter 'I' for the subject to be deleted by id else enter 'S' to be deleted bysubject name : ").upper()
                sl.deleteSubject(choice)

            elif op == '3':
                subId = input("Enter the subject Id to be edited: ")
                sub = input("Enter the subject name : ")
                sl.editSubject(subId, sub)

            elif op == '4':
                sl.viewSubjectList()

            elif op == '5':
                print("Redirecting to the user menu.....")
                break

            else:
                print("Invalid operation id")  

            print("~~~~".center(70, ':'))

    elif user == 'O' and userPassword == 'other' : 
        while True:
            print("Please select an operation to perform : ")
            print("1. Add\n2. Delete\n3. Edit\n4. View\n5.Report \n6. Exit")
            op = input()
            # op stands for operation
            if op == '1':
                id = input("Enter the student id : ")
                name = input("Enter the student name : ")
                age = int(input("Enter the student's age : "))
                gender = input("Enter the student's gender : ")
                print("These are the subjects being offered : ")
                s.viewSubjects()
                subjectId1 = input("Enter the id first subject selected : ")
                mark_s1 = int(input(f"Enter the marks of {subjectId1} : "))
                subjectId2 = input("Enter the id second subject selected : ")
                mark_s2 = int(input(f"Enter the marks of {subjectId2} : "))
                s.add(id, name, age, gender, subjectId1, mark_s1, subjectId2, mark_s2)

            elif op == '2':
                id = input("Enter the student id : ")
                s.delete(id)

            elif op == '3':
                id = input("Enter the student id : ")
                s.edit(id)

            elif op == '4':
                ch = input("Do you want to view all the data(A) or individual singled out(I) : ").upper()
                s.view(ch)

            elif op == '5':
                id = input("Enter the student id : ")
                s.report(id)

            elif op == '6':
                s.exit()

            else :
                print("Invalid choice") 

            print("~~~~".center(70, ':'))
    
    else:
        print("Invalid user id/password")


