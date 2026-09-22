# this will find files with duplicate file names but whose extension is different 
# the filenames are case sensitive

import os, pprint

def return_file_name(filename: str):
    # the function returns only the name of the file
    # this is case sensitive

    if "." in filename:
        elements = filename.split(".")
        return elements[0]

    else:
        return filename


def find_duplicate_files(directory: str):
    # check for the validation of the directory given
    if not os.path.isdir(directory):
        raise ValueError("Invalid path, expcted a valid directory path")

    if not os.listdir(directory):
        raise ValueError("Directory is empty")

    files = os.listdir(directory)

    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            duplicate_file_dict.setdefault(return_file_name(file), []).append(file)

        # else: # for later recursive thoughts
        #     return find_duplicate_files(file, duplicate_file_dict)

    duplicate_file_dict = {filename : files for filename, files in duplicate_file_dict.items() if len(files) > 1}

    return duplicate_file_dict


def main():
    _path = input("Enter the filepath : ")
    duplicate_files = find_duplicate_files(_path)
    if not duplicate_files:
        print("No duplicate files present")

    else:
        pprint.pprint(duplicate_files)


if __name__ == "__main__":
    main()
