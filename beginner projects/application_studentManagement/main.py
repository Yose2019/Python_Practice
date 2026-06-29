# the module is the actual UI which interacts with the user 

from studentOperations import studentOperations

s = studentOperations()
while True:
    print("Please select an operation to perform : ")
    print("1. Add\n2. Delete\n3. Edit\n4. View\n5.Report \n6. Exit")
    op = int(input()) 
    # op stands for operation
    if op == 1:
        id = input("Enter the student id : ")
        name = input("Enter the student name : ")
        age = int(input("Enter the student's age : "))
        gender = input("Enter the student's gender : ")
        subject1 = input("Enter the first subject selected : ")
        mark_s1 = int(input(f"Enter the marks of {subject1} : "))
        subject2 = input("Enter the second subject selected : ")
        mark_s2 = int(input(f"Enter the marks of {subject2} : "))
        s.add(id, name, age, gender, subject1, mark_s1, subject2, mark_s2)

    elif op == 2:
        id = input("Enter the student id : ")
        s.delete(id)

    elif op == 3:
        id = input("Enter the student id : ")
        s.edit(id)

    elif op == 4:
        ch = input("Do you want to view all the data(A) or individual singled out(I) : ").upper()
        s.view(ch)

    elif op == 5:
        id = input("Enter the student id : ")
        s.report(id)

    elif op == 6:
        s.exit()

    else :
        print("Invalid choice") 


