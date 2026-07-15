'''
The phase 6 of the library manager is here
This includes the functionalities add, view, search and delete
'''
from datetime import datetime
import os

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
            book_title = input("Enter the book title : ").strip()
            if book_title == "":
                print("Information entered cannot be invalid or an empty string - redo the process")
                continue
            break

        while True:
            book_author = input("Enter the name of the book author : ").strip()
            if book_author == "":
                print("Information entered cannot be invalid or an empty string - redo the process")
                continue
            break

        while True:
            publication_year = input("Enter the year of publication : ").strip()
            if not publication_year.isdecimal():
                print("Publication year has to be an numbers only")
                continue
            elif int(publication_year) < 0 or int(publication_year) > datetime.now().year:
                print("invalid publication year info, please verify")
                continue
            break 

        while True:
            book_genre = input("Enter the genre of the book : ").strip()
            if book_genre == "":
                print("Information entered cannot be invalid or an empty string - redo the process")
                continue
            break

        return book_title.title(), book_author.title(), publication_year, book_genre.title()
    
    @staticmethod
    def formatted_output(book_collection):
        print("THIS IS THE COLLECTION".center(50, "="))
        print()
        for title, info in book_collection.items():
            print(f"BOOK : {title}".center(50, "="))
            for key, value in info.items():
                print(f"Book {key}".ljust(30) + ":" f"{value}".rjust(30))
            print()

    @staticmethod
    def print_book_info(book):
        for key, value in book.items():
            print(f"{key}".ljust(30) + ":" + f"{value}".rjust(40))
        return

    @staticmethod # hardcoding the filename as of now
    def save_data(library_infomation, file_path = None):
        if file_path is None:
            file_path = r"D:\practice\beginner projects\Library_Manager\LibraryManager.txt"

        if not library_infomation:
            return 
        
        
        with open(file_path, 'w') as f:
            for value in library_infomation.values():
                title, author, published_year, genre = value["title"].strip(), value["author"].strip(), value["published year"].strip(), value["genre"].strip()
                write_line = f"{title},{author},{published_year},{genre}\n"
                f.write(write_line)

        return 
                
    @staticmethod
    def get_saved_data(file_path = None):
        if file_path is None:
            file_path = r"D:\practice\beginner projects\Library_Manager\LibraryManager.txt"
        else:
            file_path = file_path

        if not os.path.exists(file_path):
            with open(r"D:\practice\beginner projects\Library_Manager\LibraryManager.txt", 'w') as f:
                print("file opened")

        if not os.path.getsize(file_path):
            return {}
        
        key_list = []
        library_data = {}
        with open(file_path, 'r') as f:
            for line in f:
                elements = line.split(",")
                print(elements)
                key_list.append(elements[0])
 
        with open(file_path, 'r') as f:
            key = 0           
            for line in f:
                print(line)
                book_info = line.split(",")
                print(book_info)
                library_data[key_list[key]] = {
                    "title" : book_info[0],
                    "author" : book_info[1],
                    "published year" : book_info[2],
                    "genre" : book_info[3]
                }
                key += 1

        return library_data

class LibraryFunctions:
    '''
    These are the main function performing the task
    '''
    library_collection = Utilities.get_saved_data()

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
        elif self.library_collection.get(book_title, None) is not None and book_info != self.library_collection[book_title]:
            step = input("Book is present, would you like to edit it : (y/n)").lower()
            if step == 'y':
                self.library_collection[book_title.title()] = book_info
            elif step == 'n':
                return
            else:
                print("invalid choice entered")
                return
        else:
            self.library_collection[book_title] = book_info
            print("Book added successfully")
        
        return


    def view_books(self):
        if not self.library_collection:
            print("Colllection is empty, add books to the library")
            return 
        Utilities.formatted_output(self.library_collection) 


    def search_book(self, book_title = None):
        if not self.library_collection:
            print("Collection is empty, add book information")
            return False
        
        if book_title is None:
            book_title = input("Enter the title of book to be searched : ").strip().title()

        if book_title not in self.library_collection.keys():
            print("Book not found")
            return False
        else:
            print("Book found".center(50, "="))
            Utilities.print_book_info(self.library_collection[book_title])
            return True
        
    def delete_book(self):
        if not self.library_collection:
            print("No books in the library, add books to proceed")
            return
        book_title = input("Enter the title of the book you want to deal with : ").strip().title()
        if not self.search_book(book_title = book_title):
            return 
        option = input("Do you want to delete the book(y/n) : ").lower()
        if option == 'y':
            del self.library_collection[book_title]
            print("book deleted successfully")
        elif option == 'n':
            print("Book deletion process aborted")
        else:
            print("Invalid option selected")
        
        return
        

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
                library_functions.search_book()
            elif choice == 4:
                library_functions.delete_book()
            elif choice == 5:
                Utilities.save_data(library_functions.library_collection)
                print("Thankyou for using personal library manager")
                break 


if __name__ == "__main__":
    main()