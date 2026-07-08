'''
The phase 3 of the library manager is here
'''
from datetime import datetime

class Utilities:
    '''
    This assists the functionality of the library manager
    '''
    @staticmethod
    def fetch_bookinfo_to_add():
        '''
        @Description : This will prompt the user for the (correct) info of the book 
        @returns : title, author, publication_year, genre
        '''
        book_info = {}

        book_author = book_title = book_genre = publication_year = ""

        print("Book Info required".center(50, "="))
        while True:    
            book_title = input("Enter the book title : ")
            if book_title.strip() == "":
                print("Information entered cannot be invalid or an empty string - redo the process")
                continue
            break

        while True:
            book_author = input("Enter the name of the book author : ")
            if book_author.strip() == "":
                print("Information entered cannot be invalid or an empty string - redo the process")
                continue
            break

        while True:
            publication_year = input("Enter the year of publication : ")
            if not publication_year.isdecimal():
                print("Publication year has to be an numbers only")
                continue
            elif int(publication_year) < 0 or int(publication_year) > datetime.now().year:
                print("invalid publication year info, please verify")
                continue
            break 

        while True:
            book_genre = input("Enter the genre of the book : ")
            if book_genre.strip() == "":
                print("Information entered cannot be invalid or an empty string - redo the process")
                continue
            break

        return book_title.title(), book_author.title(), publication_year, book_genre.title()
    
    def formatted_output(book_collection):
        print("THIS IS THE COLLECTION".center(50, "="))
        print()
        for title, info in book_collection.items():
            print(f"BOOK : {title}".center(50, "="))
            for key, value in info.items():
                print(f"Book {key}".ljust(30) + ":" f"{value}".rjust(30))
            print()


class LibraryFunctions:
    '''
    These are the main function performing the task
    '''
    library_collection = {}

    def add_book(self):
        book_title, book_author, publication_year, book_genre = Utilities.fetch_bookinfo_to_add()

        book_info = {
            "title" : book_title,
            "author" : book_author,
            "published year" : publication_year,
            "genre" : book_genre
        }
        if self.library_collection.get(book_title, None) is not None and book_info == self.library_collection[book_title]:
            print("The book already exists in the collection")
        else:
            self.library_collection[book_title] = book_info
            print("Book added successfully")
        
        return


    def view_books(self):
        if len(self.library_collection) == 0:
            print("Colllection is empty, add books to the library")
            return 
        Utilities.formatted_output(self.library_collection) 


def main():
    '''
    @Description : this is the user interface which interacts with the user
    '''
    library_functions = LibraryFunctions()

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
                library_functions.add_book()
            elif choice == 2:
                library_functions.view_books()
            elif choice == 3:
                print("search Book selected")
            elif choice == 4:
                print("Remove Book selected")
            elif choice == 5:
                print("Thankyou for using personal library manager")
                break 


if __name__ == "__main__":
    main()