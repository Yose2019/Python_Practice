'''
This is the Log Parser version 2 
'''

class LogParser:
    '''
    @Description: The log parser version 2 returns the parsed log 
    Objective is to get the lines which have the status as error 
    '''

    def __init__(self, filepath: str):
        '''
        initializes the attributes 
        '''
        self.filepath = filepath

    
    def get_error_lines(self):
        '''
        The function opens the text file, parses through it
        And gets the lines which are causing error
        '''
        with open(self.filepath, 'r') as f:
            errors = []
            for line in f:
                # analyse whether the line has error or not
                if len(line.split()) >= 3:
                    if line.split()[2] == "ERROR":
                        errors.append(line.strip())

            return errors

        
obj = LogParser(r"D:\practice\beginner projects\LogParser\sample_log.txt")

print("The errors found are as follows:")
for error in obj.get_error_lines():
    print(error)
