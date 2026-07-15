'''
the file explorer version 1 wouold list all the files in the folder

Note to self : certain APIs of the os not understood very well 
Refine in phase 2
'''

import os


class FileExplorer:
    '''
    @Description : the class contains the methods for functionality
    '''
    def __init__(self, folderpath: str):
        self.folderpath = folderpath 

    
    def validate_filepath(self):
        if not os.path.exists(self.folderpath):
            return False
        return True
        
    
    def list_files(self):
        if not self.validate_filepath():
            print("The path is invalid")
            return

        if not os.listdir(self.folderpath):
            print("The folder is empty")
            return
        
        for file in os.listdir(self.folderpath):
            if os.path.isfile(file):
                print(file)
            else:
                continue 


def main():
    _path = input("Enter the filepath : ")
    fex = FileExplorer(_path)
    fex.list_files()

if __name__ == "__main__":
    main()