'''
This is phase 3 of the project
Objective

Analyze all files in a given directory and generate a summary report.

Your program should determine:
Total number of files.
Total size of all files combined.
Largest file (name and size).
Smallest file (name and size).
Number of files for each file extension (e.g., .txt, .py, .pdf).
Requirements
Consider files only (ignore subdirectories).
If the directory contains no files, display an appropriate message.
Present the results in a clean, readable report.
'''

import os 

class Utility:
    '''
    @Description : holds the tools which will help in file explorer methods
    '''
    @staticmethod
    def validate_path(_path: str):
        '''
        @Description : validates whether the path for the file is valid or not
        '''
        if os.path.exists(_path):
            return True
        else:
            return False
        

    @staticmethod
    def validate_dir_not_empty(_path:str):
        '''
        @Desription : the function validates whether the directory is empty
        '''
        if not os.listdir(_path):
            return False
        return True

class FileExplorer:
    '''
    @Description : The file explorer consists of methods which help in exploring the file structure
    '''
    def __init__(self, _path: str):
        '''
        @Description : the path initializes the filepath/folderpath 
        '''
        if Utility.validate_path(_path):
            self.fpath = _path
        else:
            raise ValueError("The path does not exist")
        

    def get_all_files(self):
        '''
        @Description : this will simply return the list of all the file names
        @returns list of all files
        '''
        all_files = []

        if Utility.validate_dir_not_empty(self.fpath):
            for file in os.listdir(self.fpath):
                if os.path.isfile(os.path.join(self.fpath, file)):
                    all_files.append(file)

            return all_files
        
        if not all_files:
            raise ValueError("The folder is empty")


    def get_all_files_info(self):
        '''
        @Description : the method gives the information about the folder
        @returns : dictionary of dictionary
        '''
        all_files_info = {}

        if Utility.validate_dir_not_empty(self.fpath):
            for file in os.listdir(self.fpath):
                if os.path.isfile(os.path.join(self.fpath, file)):
                    fileDetails = os.path.splitext(file)
                    all_files_info[file] = {
                        "filename" : fileDetails[0],
                        "fileExt" : fileDetails[1][1:],
                        "filesize" : os.path.getsize(os.path.join(self.fpath, file))
                    }
            return all_files_info
        
        if not all_files_info:
            raise ValueError("the folder is empty")
        
    
    def get_dir_report(self):
        '''
        @Description : the method should determin the following things
        Total number of files.
        Total size of all files combined.
        Largest file (name and size).
        Smallest file (name and size).
        Number of files for each file extension (e.g., .txt, .py, .pdf).
        '''
        dir_report = {}

        if Utility.validate_dir_not_empty(self.fpath):
            max_size, min_size = float("-inf"), float("inf")
            dir_report["extensions_info"] = {}

            for file in os.listdir(self.fpath):
                if os.path.isfile(os.path.join(self.fpath, file)):
                    file_extension = os.path.splitext(file)[1][1:]

                    dir_report["total_files"] = dir_report.get("total_files", 0) + 1
                    file_size = os.path.getsize(os.path.join(self.fpath, file))
                    dir_report["total_size"] = dir_report.get("total_size", 0) + file_size

                    if file_size > max_size:
                        max_size = file_size
                        dir_report["largest_file"] = {
                            "name" : file,
                            "size" : file_size
                        }

                    if file_size < min_size:
                        min_size = file_size
                        dir_report["smallest_file"] = {
                            "name" : file,
                            "size" : file_size
                        }
                    
                    dir_report["extensions_info"][file_extension] = dir_report["extensions_info"].get(file_extension, 0) + 1

            return dir_report
        
        if not dir_report:
            raise ValueError("the folder is empty")
     

filepath = input("enter folder path : ")
Fex = FileExplorer(filepath)
print(Fex.get_all_files_info())
print(Fex.get_all_files())
print(Fex.get_dir_report())





