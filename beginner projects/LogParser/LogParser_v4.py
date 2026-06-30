'''
The program is the version 4 of log parser
'''

class LogParser:
    '''
    @Description : The present version of the log parser deals with numerical value
    '''
    def __init__(self, filepath: str):
        '''
        @Description : initializes the paramaters
        @inputs : the path of the log file
        '''
        self.filepath = filepath 

    
    def extract_temperature_values(self):
        '''
        @Description : Extracts the temperatures from the log file text
        @returns : list of values of tempratures
        '''
        possible_values = []
        with open(self.filepath, 'r') as log_file:
            for line in log_file:
                if "Temperature" in line:
                    line_elements = line.split()
                    for value in line_elements:
                        if value[:-1].isdecimal():
                            possible_values.append(float(value[:-1]))

        return possible_values
    

    def return_temperature_variation(self):
        temperature_values = self.extract_temperature_values()
        if temperature_values == []:
            return 0, 0, 0
        
        maximum_teperature, minimum_temperature, average_temperature = (temperature_values[0], temperature_values[0], 0)

        total_temperature, count = (0, 0)

        # doing it manually intentionally to know the procedure in core
        for value in temperature_values:
            if value > maximum_teperature:
                maximum_teperature = value
            if value < minimum_temperature:
                minimum_temperature = value
            total_temperature += value 
            count += 1

        average_temperature = round(total_temperature/count, 2)
        return maximum_teperature, minimum_temperature, average_temperature
    

obj = LogParser(r"D:\practice\beginner projects\LogParser\sample_log_phase4.txt")
max_temp, min_temp, avg_temp = obj.return_temperature_variation()
print(f"Maximum temperature is : {max_temp}\nMinimum temperature is : {min_temp}\nAverage temparture is : {avg_temp}")
        
                

