# the class holds the subject
# this will have a subject id and associated subject
# the functions in this class would be add subject
# find the subject based on id 

# for adding, the segregation can be made later on that only administrator can access these things
# while the other kind of user can access specific things 

# adding serialization and deserialization to this similar to the studentOperations file
# Serialize converts the data into a json file -> dump 
# Desrialize gets the data from json to a python object -> load 
# use th json module and os module for the same  

import os, json


def serializeData(subjectData):
    filepath = os.path.join(os.getcwd(), r"beginner projects\application_studentManagementV3\subject_data.json")

    if os.path.exists(filepath):
        with open(filepath, 'w') as f:
            json.dump(subjectData, f, indent = 4)
    else:
        open(r"D:\practice\beginner projects\application_studentManagementV3\subject_data.json", 'w')


def deserializeData():
    filepath = os.path.join(os.getcwd(), r"beginner projects\application_studentManagementV3\subject_data.json")

    if os.path.exists(filepath): 
        if os.path.getsize(filepath) == 0:
            return {}
        
        with open(filepath, 'r') as f:
            data = json.load(f)


        return data  
    
    else:
        return {}

class subjectList :
    subjectList = deserializeData()



    # the add, edit and delete in the future are privileges of administrator only and not regular user 
    def addSubject(self, subId, sub):
        if self.subjectList.get(subId, 0) != 0 or sub in self.subjectList.values():
            print("Subject already present")
            return 
        self.subjectList[subId] = sub

    def editSubject(self, subId, sub):
        # the function edits the subject id and the subject
        # approach is to remove the old subId if it exists

        if self.subjectList.get(subId, 0) != 0 and (sub in self.subjectList.values()) :
            print("Sub Id and Subject are mapped already")
            return
         
        elif self.subjectList.get(subId, 0) != 0 :
            self.subjectList[subId] = sub # changing the value is easy 

        # the above conditio if key exists and value needs to be updated 
        # if the opposite needs to be done, that is key needs to be changed if the value exists 
        elif sub in self.subjectList.values():
            # here the id needs to changed
            # to do this pop the older the subId
            oldId = next(k for k, v in self.subjectList.items() if v == sub)
            subject = self.subjectList.pop(oldId) # this returns the subject
            self.subjectList[subId] = subject 

        else:
            print("The subject is not present")

        self.viewSubjectList()

    def deleteSubject(self, choice) :
        if choice == 'I':
            id = input("Enter the subject Id to be deleted : ")
            if self.subjectList.get(id, 0) != 0:
                del self.subjectList[id]
            else:
                print("Invalid Id")
        elif choice == 'S':
            sub = input("Enter the subject to be deleted : ")
            if sub in self.subjectList.values():
                id = next(k for k, v in self.subjectList.items() if v == sub)
                del self.subjectList[id] 
            else:
                print("Subject not present")
        else:
            print("Invalid choice")

    def findSubject(self, id):
        if self.subjectList.get(id, 0) != 0:
            return self.subjectList[id]
        else:
            print("Invaid Id : subject not present")

    def viewSubjectList(self):
        print("=" * 60)
        for subId, sub in self.subjectList.items():
            print(subId.ljust(10) + ":" + sub.rjust(20))
        print("=" * 60)

    def allSubjectsCode(self):
        codeList = []
        for code in self.subjectList.keys():
            codeList.append(code)

        return codeList


    def saveData(self):
        serializeData(self.subjectList)


        
