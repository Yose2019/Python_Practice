'''
the module consists of phase 2 of the project
the folders need to created for the extension

AUTHOR : SHRISTHI N AKKALKOT

Template under class and methods defined :

@Description: 
@inputs: 
@returns: 
'''

import os

class Tools:
    '''
    @Description: The class consists of methods which assist the BatchFileOrganiser class
    '''
    @staticmethod
    def validate_path(_path):
        '''
        @Description: the method validates whether a path is valid or not
        @inputs: path of the file or directory
        @returns: Boolean
        '''
        if not os.path.exists(_path):
            raise ValueError("Invalid path")
        
        return True


    @staticmethod
    def directory_not_empty(_path):
        '''
        @Description: the method validates whether a path is a directory and it is empty 
        @inputs: path of the file or directory
        @returns: Boolean
        '''
        if not os.listdir(_path):
            raise ValueError("The folder is empty")
        
        return True
    

    @staticmethod
    def files_present(_path):
        '''
        @Description: the method checks whether any files are present at the immediate level of the directory 
        @inputs: path of the file or directory
        @returns: Boolean
        '''
        for f in os.listdir(_path):
            if os.path.isfile(os.path.join(_path, f)):
                return True
            if os.path.isdir(os.path.join(_path, f)):
                continue

        return False
    

    @staticmethod
    def get_all_files(_path):
        '''
        @Description: the method returns all the files in the directory if any present 
        @inputs: path of the file or directory
        @returns: List
        '''
        files = []

        if Tools.files_present(_path):
            for file in os.listdir(_path):
                files.append(file)

        else:
            raise ValueError("No files present within this folder")
            
        return files
    

    @staticmethod
    def path_is_a_file(_path):
        '''
        @Description: the method checks whether the path is a file which is given by the user 
        @inputs: path of the file or directory
        @returns: Boolean
        '''
        if Tools.validate_path(_path) and os.path.isdir(_path):
            return False
        
        elif os.path.isfile(_path):
            return True 
        
    
    # @staticmethod
    # def get_all_folders(_path):
    #     '''
    #     @Description: the method gives all the subfolders 
    #     @inputs: None
    #     @returns: list
    #     '''
    #     dirs = []
    #     for f in os.listdir(_path):
    #         if os.path.isdir(os.path.join(_path, f)):
    #             dirs.append(f)

    #     return dirs


    # TODO : plan this later, not needed for now
    # @staticmethod
    # def handle_file_path(_path, mapping):
    #     pass
    

class BatchFileOragniser:
    '''
    @Description: The class consists of methods which assist in the Batch File Organising
    '''

    mapping = {
        "pdf" : "PDF",
        "doc" : "DOCUMENTS",
        "jpg" : "IMAGES",
        "png" : "IMAGES",
        "webp" : "IMAGES",
        "mp3" : "AUDIO",
        "wav" : "AUDIO",
        "mp4" : "VIDEO",
        "oth" : "OTHERS",
        "pptx" : "PRESENTATIONS",
        "" : "NO_EXT"
    }


    def __init__(self, _path):
        '''
        @Description: the method initialises the arguments 
        @inputs: path of the file or directory
        @returns: None
        '''
        if Tools.path_is_a_file(_path):
            raise ValueError("The given class does not handle file paths yet")

        if Tools.validate_path(_path) and Tools.directory_not_empty(_path):
            self.path = _path 

        else:
            raise ValueError("The path is not valid for operation")
        

    def segregate_file_destination(self):
        '''
        @Description: the method gives the information on the prospective parent folder 
        @inputs: None
        @returns: dictionary
        '''
        files = Tools.get_all_files(self.path)

        folder_mapped_files = {}

        for file in files:
            ext = os.path.splitext(file)[1][1:]

            if ext == "":
                folder = self.mapping[""]

            if self.mapping.get(ext, 0) == 0:
                folder = self.mapping["oth"]

            else:
                folder = self.mapping[ext]

            folder_mapped_files.setdefault(folder, []).append(file)

        return folder_mapped_files
    

    def create_req_directories(self):
        '''
        @Description: the method gives the information on the prospective parent folder 
        @inputs: None
        @returns: dictionary
        '''
        status_dictionary = {}

        directories = self.mapping.values()

        for directory in directories:
            if os.path.exists(os.path.join(self.path, directory)):
                status_dictionary[directory] = "present"
            else:
                os.mkdir(os.path.join(self.path, directory))
                status_dictionary[directory] = "created"

        return status_dictionary

    
def main():
    try:
        bfo = BatchFileOragniser(r"C:\Users\Admin\Downloads")
        print(bfo.segregate_file_destination())
        print(bfo.create_req_directories())
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

        





