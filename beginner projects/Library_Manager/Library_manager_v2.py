'''
This is phase 2 of the library manager application with the integration of the add book functionality
'''
from datetime import datetime


class ExecuteBookFunctions:
    '''
    This will accept the user input, validate in real time, and then pass it to storage 
    '''

    @staticmethod
    def prompt_and_validate_add():
        '''
        The function is used to prompt the user to enter input and validate the same
        '''
        book_title, book_author, book_genre = (" ", " ", " ")
        book_publication_year = 0

        while len(book_title.strip()) == 0:
            book_title = input("Enter the title of the book : ")
            if len(book_title.strip()) != 0 :
                break
            else:
                print("Title of the book cannot be an empty string") 
                
        while len(book_author.strip()) == 0:
            book_author = input("Enter the author of the book : ")
            if len(book_author.strip()) != 0 :
                break
            else:
                print("Author of the book cannot be an empty string") 
            
        while book_publication_year == 0:
            book_publication_year = int(input("Enter the year of publication :  "))
            if book_publication_year != 0 and book_publication_year > 0 and book_publication_year <= datetime.now().year:
                break
            else:
                book_publication_year = 0
                print("Publication year needs to be rechecked...")

        while len(book_genre.strip()) == 0:
                book_genre = input("Enter the genre of the book : ")
                if len(book_genre.strip()) != 0 :
                    break
                else:
                    print("Genre of the book cannot be an empty string")

        bookfunction = BookFunctions()
        bookfunction.add_book(book_title, book_author, book_publication_year, book_genre)


class BookFunctions:
    '''
    @Description : The class holds the functionality of the library manager 
    '''
    library_entries = {} # a dictionary whose keys would be title and value would be info as ditionary

    def add_book(self, book_title, book_author, book_publishing_year, book_genre):
        if self.library_entries.get(book_title) is None:
            book_info = {}
            book_info["title"] = book_title
            book_info["author"] = book_author
            book_info["published"] = book_publishing_year
            book_info["genre"] = book_genre
            self.library_entries[book_title] = book_info
            return
        
        else:
            print("The book is already present")
            return
            

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
                ExecuteBookFunctions.prompt_and_validate_add()
                print("Book added successfully")
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
