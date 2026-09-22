# the program gives a simple function which will help to group the files based on the extensions

import os, pprint

def group_by(directory):
    '''
    @author : Shristhi N Akkalkot
    @inputs : path of the directory
    @returns : dictionary
    '''
    #doing the checks first 
    if not os.path.exists(directory):
        raise ValueError("INVALID PATH")

    if os.path.isfile(directory):
        return {os.path.splitext(directory)[-1].split(".")[-1] : [directory]}

    if os.path.isdir(directory):
        if not os.listdir(directory):
            raise ValueError("Empty directory, no files found within")
        # loop though them
        files = os.listdir(directory)

        file_groups = {}

        for file in files:
            if os.path.isfile(os.path.join(directory, file)):
                ext = os.path.splitext(file)[-1].split(".")[-1]
                file_groups.setdefault(ext, []).append(file) if ext != "" else file_groups.setdefault("No_ext", []).append(file)

        return file_groups


def main():
    _path = input("Enter the directory path : ")
    groups = group_by(_path)

    if groups:
        pprint.pprint(groups)


if __name__ == "__main__":
    main()


        

