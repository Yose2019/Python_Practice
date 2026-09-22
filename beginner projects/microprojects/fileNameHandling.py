'''
This handles improper filename
'''

def file_name_handler(file_name: str):
    file_names = {}

    if not file_name:
        return {}

    file_ele = file_name.split(".")
    print(file_ele)
    file_ext = file_ele.pop()

    for index, name in enumerate(file_ele):
        name = name.strip()
        name = name.strip("#@()*&!?")
        if " " in name:
            name = "_".join(name.split())
        name = "_".join(name.split("@#$%^!><?:"))

        name = name.lower()
        file_ele[index] = name


    file_ele = "_".join(file_ele)

    file_modified_name = file_ele + "." + file_ext

    return {file_name: file_modified_name}


files = ["My File!!.txt",
"hello   world.py",
"TEST_FILE!!.pdf",
"vacation photo  2025.jpg"]

for file in files:
    print(file_name_handler(file))




    

        




