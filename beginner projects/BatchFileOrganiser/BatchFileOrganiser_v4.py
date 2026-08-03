'''
This is the phase 4 of batch file organiser 
Trying to rebuild the utility from scratch
Not trying to over do the things
Creating one class and not messing the classes 
Ensuring to create a tool class only if a utility is used repeatedly and by closely all methods

Functions required: 
* to segregate which file goes where 
* to create the folders if not exist
* move files to the created folders

-> add reports to everything
'''
import os, shutil
import pprint

class Tools:
    '''
    @Description: Consists of methods which are repeatedly used by the BatchFileOrganiser class
    '''
    @staticmethod
    def valid_path(fpath):
        '''
        @Description: validates the path whether it is right or not
        '''
        # three validations are needed - whethere exists
        if not os.path.exists(fpath):
            raise ValueError("Path does not exist")

        # validate of folder
        if not os.path.isdir(fpath):
            raise ValueError("Path does not belong to a directory")

        # validate if empty
        if not os.listdir(fpath):
            raise ValueError("Directory is empty")

        # validate whether there are files inside it 
        file_exists = False
        for f in os.listdir(fpath):
            if os.path.isfile(os.path.join(fpath, f)):
                file_exists = True

        if not file_exists:
            raise ValueError("No files present inside the given path")

        return True


    @staticmethod
    def get_subfolders_and_files(fpath):
        '''
        @Description: gives all subfolders and files as a list
        @returns: list of subfolders and files
        '''
        # if the method is called then folder is validated, no need to revalidate
        content_list = os.listdir(fpath)

        subfolders, files = ([], [])

        for f in content_list:
            comp_path = os.path.join(fpath, f)
            if os.path.isdir(comp_path):
                subfolders.append(f)

            elif os.path.isfile(comp_path):
                files.append(f)

        return subfolders, files

       
class BatchFileOrganiser:
    '''
    @Description : contains methods which perform different actions on the file organisers
    '''
    mapping = {
        "txt" : "TEXT_files",
        "mp3" : "AUDIO_files",
        "aac" : "AUDIO_files",
        "wav" : "AUDIO_files",
        "mp4" : "VIDEO_files",
        "jpg" : "PHOTOS",
        "png" : "PHOTOS",
        "gif" : "PHOTOS",
        "pdf" : "PDF_files",
        "docx" : "DOCUMENTS",
        "py" : "PYTHON_files",
        "oth" : "OTHERS",
        "" : "NO_EXTENSION_files"
    }

    def __init__(self, fpath):
        '''
        @Description: Initializes the arguments
        '''
        if Tools.valid_path(fpath): # this will use a tool utility as it needs validations
            self.path = fpath
            self.subfolder, self.files = Tools.get_subfolders_and_files(fpath)


    def map_destination_folder(self):
        '''
        @Description: segregate the files onto the dstination folder
        @returns: report as a dictionary
        '''
        file_segregation = {}

        if self.files: #precaution to prevent checking if no files are present
            for file in self.files:
                ext = os.path.splitext(file)[1][1:].lower()

                if self.mapping.get(ext, 0) != 0:
                    folder = self.mapping[ext]

                else:
                    folder = self.mapping["oth"]

                file_segregation.setdefault(folder, []).append(file)

        return file_segregation


    def create_required_directories(self):
        '''
        @Description: create the driectories if not created already
        '''
        dir_status = {}
        dir_status["status"] = {}
        dir_to_be_created = self.map_destination_folder().keys()

        for dir in dir_to_be_created:
            if self.subfolder and (dir in self.subfolder):
                dir_status[dir] = "Present"
                dir_status["status"]["exist"] = dir_status["status"].get("exist", 0) + 1 
                continue 

            else:
                os.mkdir(os.path.join(self.path, dir))
                dir_status[dir] = "Created"
                dir_status["status"]["created"] = dir_status["status"].get("created", 0) + 1

        return dir_status


    def add_files_into_folders(self):
        '''
        Description: add the files into respective folders now
        Use the shutil module to move between source and destination
        '''
        # run the create_required_directories from within to avoid any conflicts
        created_directories = self.create_required_directories()

        file_folders = self.map_destination_folder()

        placement_report = {} 
        placement_report["directory_creation_status"] = created_directories

        for folder, files in file_folders.items():
            destination = os.path.join(self.path, folder)

            for file in files:
                source = os.path.join(self.path, file)
                placement_report["total_files"] = placement_report.get("total_files", 0) + 1

                if file in os.listdir(destination):
                    placement_report.setdefault("skipped_files", []).append(file)
                    placement_report["skipped_files_count"] = placement_report.get("skipped_files_count", 0) + 1
                    continue

                try:
                    shutil.move(source, destination)
                    placement_report.setdefault("file_moved", []).append(file)
                    placement_report["moved_files_count"] = placement_report.get("moved_files_count", 0) + 1
                except Exception as e:
                    placement_report.setdefault("failed_to_move", []).append(file)
                    placement_report.setdefault("failure_reasons", []).append(str(e))
                    placement_report["failed_files_count"] = placement_report.get("failed_files_count", 0) + 1

        return placement_report

    def organise(self):
        return self.add_files_into_folders()
    


def main():
    try:
        fpath = input("Enter the path of the folder : ")
        Bfo = BatchFileOrganiser(fpath)
        pprint.pprint(Bfo.organise())

        
    except Exception as e:
        print(e)
        

if __name__ == "__main__":
    main()

            

            




        






    

