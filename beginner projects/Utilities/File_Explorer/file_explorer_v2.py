'''
the file explorer version 2 wouold list all the files in the folder, and print information about the file
this phase we are printing the name, extenstion and size of the file

Note to self : certain APIs of the os not understood very well 
Refinment requested and required in phase 2
'''
import os

class FileExplorerUtilities:
    '''
    @Description : The class holds utilities which are used by the FileExplorer Class
    '''

    def validate_directory(self, directory):
        if not os.path.exists(directory):
            return False
        return True
    
    def print_files(self, directory, file_list):
        for file in file_list:
            if os.path.isfile(os.path.join(directory, file)):
                print(file)

    def all_files_list(self, directory):
        return os.listdir(directory)
    

    def print_file_information(self, directory, file_list):
        for file in file_list:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                print("=" * 20)
                file_name_and_ext = os.path.splitext(file)
                print(f"File name : {file_name_and_ext[0]}\nFile extension : {file_name_and_ext[1][1:]}\nFile size : {os.path.getsize(file_path)} Bytes")
                


class FileExplorer:
    '''
    @Description : The class has methods which help in extracting information in a directory or file
    '''
    def __init__(self, directory: str):
        '''
        @Description : initializes the directory name, but only if valid
        @inputs : directory name
        '''
        self.utility_object = FileExplorerUtilities()
        if self.utility_object.validate_directory(directory):
            self.directory = directory
        else:
            print("The directory is not valid")
            return


    def list_files(self):
        all_files = self.utility_object.all_files_list(self.directory)

        if not all_files:
            print("Directory is empty")
        
        self.utility_object.print_files(self.directory, all_files)

    
    def get_file_info(self):
        all_files = self.utility_object.all_files_list(self.directory)

        if not all_files:
            print("Directory is empty")

        self.utility_object.print_file_information(self.directory, all_files)

directory = input("Enter the directory path:")
Fex = FileExplorer(directory)
Fex.list_files()
Fex.get_file_info()
         
    

