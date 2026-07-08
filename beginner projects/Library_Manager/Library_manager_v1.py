'''
This is phase 1 of the Library manager app
'''

def main():
    '''
    @Description : The main menu of the application which interacts with the user
    '''
    print("Welcome to Library Manager Application")
    while True:
        print("PERSONAL LIBRARY MANAGER".center(50, "="))
        print("Please select the choice, enter the number present along with the choice \n\n")
        print("1. Add Book\n2. View Books\n3. Search Book\n4. Remove Book\n5. Exit\n\n")
        
        choice = input("Enter your choice : ")

        if (not choice.isdecimal()) or int(choice) not in range(1, 6):
            print("Invalid choice. Please try again.\n\n")
            continue

        else:
            choice = int(choice)
            if choice == 1:
                print("Add Book selected")
            elif choice == 2:
                print("View Books selected")
            elif choice == 3:
                print("search Book selected")
            elif choice == 4:
                print("Remove Book selected")
            elif choice == 5:
                print("Thankyou for using personal library manager")
                break 


if __name__ == "__main__":
    main()


        