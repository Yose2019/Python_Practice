# the student module holds the student class 
# the student class consists of the fields as follows - name, marks, age, gender id, subject and marks ( two subjects as of now)
# the data members have the sollowing data types - id, name, gender - string class 
# the subjects marks relation would be of dictionary and the subject is string and the marks is integer 
# age is int 

'''
name -> name of student
id -> id of student
gender -> gender of student
age -> age of student 
subjct1 -> the first subject 
mark_s1 -> marks of subject 1 
subject2 -> the second subject
mark_s2 -> marks of subject 2
'''

class student:
    def __init__(self, id, name, age, gender, subject1, mark_s1, subject2, mark_s2):
        self.id = id 
        self.name = name
        self.age = age
        self.gender = gender 
        self.subject1 = subject1 
        self.subject2 = subject2 
        self.mark_s1 = mark_s1
        self.mark_s2 = mark_s2 