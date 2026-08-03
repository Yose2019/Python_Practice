'''
The following module is phase 1 of the Batch File Organiser project
This will take my downloads folder, analyse it and give me which one should the file be mapped to
The path is : C:\\Users\\Admin\\Downloads (standard windows folder path)
'''
import os

class Tools:
    '''
    @Description: The class contains tools which assist the Batch
        File Organiser class
    '''

    @staticmethod
    def validate_path_exists(_path):
        '''
        @Description: Validates whether the path exists or not
        @inputs: path of the file or directory
        @returns: Boolean
        '''
        if not os.path.exists(_path):
            raise ValueError("Invalid path")
        return True
    

    @staticmethod
    def files_present(_path):
        '''
        @Description: Validates whether the files(atleast one file is present) are present at the immediate level
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
        @Description: identifies all the files at the immediate level in the downloads folder
        @inputs: path of the directory
        @returns: list of files
        '''
        if not Tools.files_present(_path):
            raise ValueError("The folder does not contain any files at the immeidate level")
        
        all_files = []

        for f in os.listdir(_path):
            if os.path.isfile(os.path.join(_path, f)):
                all_files.append(f)

        return all_files
    

class BatchFileOrganiser:
    '''
    @Description: The class consists of method which assist in Batch file organising
    '''
    #defining a rough mapping of all the file extensions needed to segregate
    mapping = {
        "pdf" : "PDF",
        "mp3" : "AUDIO",
        "wav" : "AUDIO",
        "mp4" : "VIDEO",
        "py" : "PYTHON",
        "txt" : "TEXT",
        "zip" : "ZIP",
        "doc" : "DOCUMENTS",
        "jpg" : "IMAGES",
        "png" : "IMAGES",
        "gif" : "IMAGES",
        "webp" : "IMAGES",
        "oth" : "OTHERS"
    }

    def __init__(self, _path):
        '''
        @Description: the method initilaises the argument
        @inputs: the path of the folder
        '''
        
        if Tools.validate_path_exists(_path):
            self.path = _path

    
    def segregate_file_location(self):
        '''
        @Description: the method takes up the path initialised and then segregates it 
                    into which folder to be put
        @returns: it returns a dictionary
        NOTE : phase 1 would not get into sub-folders
        '''
        all_files = Tools.get_all_files(self.path)

        files_list = {}

        for file in all_files:
            ext = os.path.splitext(file)[1][1:]

            if self.mapping.get(ext, 0) != 0:
                folder = self.mapping[ext]

            else:
                folder = self.mapping["oth"]

            files_list.setdefault(folder, []).append(file)

        return files_list
    

try:
    bfo = BatchFileOrganiser(r"C:\Users\Admin\Downloads")
    print(bfo.segregate_file_location())
except Exception as e:
    print(e)


            







