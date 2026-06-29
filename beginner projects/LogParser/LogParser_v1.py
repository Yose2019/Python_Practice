'''
This is the version 1 of the log parser
'''

class Log_Parser:
    '''
    @Description:
    The program takes a log file as an input and returns the number of lines an other things
    1.Open sample_log.txt
    2.Read every line
    3.Keep counters for:
    4.total number of lines
        .number of INFO
        .number of WARNING
        .number of ERROR
    5.Print the final counts
    '''
    def __init__(self, filepath):
        '''
        The initialization process
        '''
        self.filepath = filepath
        self.line_count = 0
        self.info_count = 0
        self.warning_count = 0
        self.error_count = 0


    def count_attributes(self):
        '''
        The function counts the number of lines 
        Number of lines with info, warning and error in them 
        '''
        with open(self.filepath, 'r') as f:
            for line in f.readlines():
                self.line_count += 1

                if "INFO" in line:
                    self.info_count += 1
                elif "WARNING" in line:
                    self.warning_count += 1
                elif "ERROR" in line:
                    self.error_count += 1 

        return self.line_count, self.info_count, self.warning_count, self.error_count
    
obj = Log_Parser(r"D:\practice\beginner projects\LogParser\sample_log.txt")

line_count, info_count, warning_count, error_count = obj.count_attributes()
print(f"The number of lines is : {line_count}")
print(f"The number of warnings is : {warning_count}")
print(f"The number of errors is : {error_count}")
print(f"The number of infos is : {info_count}")

