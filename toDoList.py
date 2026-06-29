# creating a simple to-do list using python
# the to-do list consists of the following features
# a user-interface to perform a specific function
# the functions include simple login, display, add, delete, exit/logout

from datetime import date, datetime

# ---create a global variable---
taskID = 0
todolist = {'id':[], 'task':[], 'date':[], 'time':[]}

# ---ADD TO THE LIST---
def addToList():
    global taskID 
    taskID += 1
    print("Enter the task:")
    task = input()
    dt = date.today()
    tm = datetime.now().strftime("%H:%M:%S")
    todolist['id'].append(taskID)
    todolist['task'].append(task)
    todolist['date'].append(dt)
    todolist['time'].append(tm)

# ---DISPLAY THE LIST---
def displayList():
    print("Task id".center(20,'-'),'\t',"Task".center(15,'-'),'\t','Date'.center(15,'-'),'\t',"Time".center(15,'-'))
    for i in range(len(todolist['id'])):
        print(f"{todolist['id'][i]}\t{todolist['task'][i]}\t{todolist['date'][i]}\t{todolist['time'][i]}")

# ---DELETE THE TASK---
def deleteTask():
    displayList()
    idDel = int(input("Enter the id of the task to be removed:"))
    ind = todolist['id'].index(idDel)
    # del todolist['id'][ind]
    todolist['id'].remove(idDel)
    del todolist['task'][ind];del todolist['date'][ind];del todolist['time'][ind];
    for i in range(len(todolist['id'])):
        if todolist['id'][i] < idDel:
            continue
        else:
            todolist['id'][i] -= 1
    print("\nThe list after modifiction is as follows:\n")
    displayList()


# ---USER-INTERFACE---
while True:
    print("Welcome user, select the operation you want to perform")
    print("Use your username to login")

    username = input("Enter the username:")

    while True:
        print("Select the action which you want to perform by entering the code in the bracket:")
        print("1.add task(a)  2.delete task(dt)  3.display list(d)  4.quit(q)")
        cmd = input()
        cmd = cmd.lower()

        if cmd == 'a':
            addToList()
        elif cmd == 'dt':
            deleteTask()
        elif cmd == 'd':
            displayList()
        elif cmd == 'q':
            exit()
        else:
            print("Enter a valid command")
            break



