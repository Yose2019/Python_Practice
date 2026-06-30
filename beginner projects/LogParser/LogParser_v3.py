'''
This is phase 3 of Log Parser project
'''

class LogParser:
    '''
    @Description : The class parses the log and processes it to give desired result
    '''
    def __init__(self, filepath: str):
        '''
        Initialization of parameters
        '''
        self.filepath = filepath 

    
    def analyse_log(self, log_category: str = "INFO"):
        '''
        @Description : The function analyses the log and gives the output
        @returns : dictionary
        @inputs : log_category 
        '''
        log_info = {}

        with open(self.filepath, 'r') as log_file:
            for line in log_file:
                if len(line.split()) > 3:
                    log_line_data = line.split(maxsplit=3)
                    if log_line_data[2] == log_category:
                        log_message = log_line_data[3].strip()
                        log_info[log_message] = log_info.get(log_message, 0) + 1
            
        return log_info
    

    def maximum_log_message(self, log_category: str = "INFO"):
        '''
        @Description : The function returns the log message which has occured maximum number of times
        @returns : dictionary
        @inputs : log_category 
        '''
        log_messages = {}

        all_log_messages = self.analyse_log(log_category=log_category)

        if not all_log_messages:
            return log_messages

        # wanted to do the execution manually
        maximum = 0
        for value in all_log_messages.values():
            if value > maximum :
                maximum = value 

        for message, occurence in all_log_messages.items():
            if occurence == maximum:
                log_messages[message] = occurence 

        return log_messages

    
obj = LogParser(r"D:\practice\beginner projects\LogParser\sample_log.txt")
print("The maximum occured messages are:")
logs = obj.maximum_log_message(log_category="ERROR")

for k, v in logs.items():
    print(f"{k} ({v} times)")




            
