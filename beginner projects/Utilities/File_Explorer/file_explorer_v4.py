'''
🗂️ Week 3 – Final Project
File Explorer Utility
Objective

Create a console-based File Explorer that allows a user to inspect, analyze, and search files inside a directory.

Functional Requirements
1. Directory Validation
Accept a directory path from the user.
Verify that the path exists.
Verify that the path is a directory.
Display an appropriate error if invalid.
2. File Listing

Display every file in the directory.

Ignore subdirectories.
Handle empty directories gracefully.
3. File Information

For every file, display:

File name
File extension
File size (bytes)
4. Directory Statistics

Generate a report containing:

Total number of files
Total size of all files
Largest file (name and size)
Smallest file (name and size)
Count of files by extension

Example:

Directory Report

Total Files : 14
Total Size  : 245831 Bytes

Largest File
-------------
movie.mp4
185423 Bytes

Smallest File
--------------
todo.txt
52 Bytes

Extension Summary
-----------------
py   : 5
txt  : 4
pdf  : 2
jpg  : 3
5. Search & Filter

Implement the following searches:

Search by extension

Example:

py

↓

Display all Python files.

Search by partial filename

Example:

report

↓

Matches:

report.pdf
report_final.docx
monthly_report.xlsx
Search by minimum size

Example:

5000

↓

Display every file whose size is at least 5000 bytes.
'''

import os 


class Utility:
    '''
    @Description : The utility class consists of methods which assist the file explorer class
    '''
    @staticmethod
    def validate_path(_path: str):
        '''
        @Description : The method allows the user to validate the path
        @inputs : path of the directory
        @returns : Boolean 
        '''
        if not os.path.exists(_path):
            raise ValueError("The provided path does not exist")
        
        if not os.path.isdir(_path) and os.path.isfile(_path):
            raise ValueError("The utility does not evaluate for files, provide a directory name")
        
        return True
    

    @staticmethod
    def check_for_empty_directory(_path):
        '''
        @Description : The method allows the user to check whether the directory is empty
        @inputs : path of the directory
        @returns : Boolean 
        '''
        if not os.listdir(_path):
            raise ValueError("The folder is empty")
        
        return True
    
    @staticmethod
    def check_files_present(_path):
        '''
        @Description : The method allows the user to check whether the directory is empty
        @inputs : path of the directory
        @returns : Boolean 
        '''
        for f in os.listdir(_path):
            if os.path.isfile(os.path.join(_path, f)):
                return True 
            
        raise ValueError("The current folder path has no files in it, rather folders")

        
class FileExplorer:
    '''
    @Description : the class contains methods for FileExplorer
    '''
    def __init__(self, _path: str):
        '''
        @Description : initializes the path argument if validation succeeds
        @inputs : directory path
        '''
        if Utility.validate_path(_path):
            self.path = _path 


    def get_files(self):
        '''
        @Description : obtaining the files in the directory
        @returns : list of all files in directory
        '''
        all_files = []

        if Utility.check_for_empty_directory(self.path) and Utility.check_files_present(self.path):
            for f in os.listdir(self.path):
                if os.path.isfile(os.path.join(self.path, f)):
                    all_files.append(f)

        if all_files:
            return all_files


    def get_file_info(self):
        '''
        @Description : obtaining the information about the files in the directory
        @returns : dictionary of the file information
        '''
        all_file_info = {}

        if Utility.check_for_empty_directory(self.path) and Utility.check_files_present(self.path):
            for f in os.listdir(self.path):
                if os.path.isfile(os.path.join(self.path, f)):
                    file_det =os.path.splitext(f)
                    all_file_info[f] = {
                        "filename" : file_det[0],
                        "file_ext" : file_det[1][1:],
                        "filesize" : os.path.getsize(os.path.join(self.path, f))
                    }

        if all_file_info:
            return all_file_info

    
    def get_file_dir_stats(self):
        '''
        @Descriptions : the method calculates the total number of files,
        size of all files,
        largest file size and name
        smallest file size and name
        count of file by extension
        @returns : dictionary of dictionary
        '''
        file_dir_stats = {}

        file_dir_stats["extensions"] = {}

        all_file_info = self.get_file_info()
        largest_file, smallest_file = float("-inf"), float("inf") 

        for file, info in all_file_info.items():
            file_dir_stats["total_files"] = file_dir_stats.get("total_files", 0) + 1
            file_dir_stats["total_size"] = file_dir_stats.get("total_size", 0) + info["filesize"]
            
            if info["filesize"] > largest_file:
                file_dir_stats["largest_file"] = {
                    "name" : file,
                    "size" : info["filesize"]
                }
                largest_file = info["filesize"]

            if info["filesize"] < smallest_file:
                file_dir_stats["smallest_file"] = {
                    "name" : file,
                    "size" : info["filesize"]
                }
                smallest_file = info["filesize"]
            

            file_ext = info["file_ext"]
            file_dir_stats["extensions"][file_ext] = file_dir_stats["extensions"].get(file_ext, 0) + 1

        return file_dir_stats
    

    def search_file(self, filename = None, ext = None, min_size = None):
        '''
        @Description : searches the file based on filename, extension, min_size
        @inputs : filename, ext, min_size
        @returns : list of all the files
        '''
        found_files = []

        all_file_info = self.get_file_info()
        
        if filename is None and ext is None and min_size is None:
            return self.get_files()
        
        for file, info in all_file_info.items():

            if filename is not None and filename in info['filename'] and file not in found_files:
                found_files.append(file)
                continue

            if ext is not None and ext == info['file_ext'] and file not in found_files:
                found_files.append(file)
                continue 

            if min_size is not None and info['filesize'] >= min_size and file not in found_files:
                found_files.append(file)

        if found_files:
            return found_files
        
        else:
            return []

def main():
    try:
        file_path = input("Enter the path of the file : ")
        Fex = FileExplorer(file_path)
        print(Fex.get_files())
        print()
        print(Fex.get_file_info())
        print()
        print(Fex.get_file_dir_stats())
        print(Fex.search_file(filename = "explo"))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()