'''
The module is phase 1 of expense analyser
'''

class ExpenseAnalyzer:
    '''
    @Description: The class consists of methods to perform operations on the expenses
    '''
    def __init__(self, filepath: str):
        '''
        @Description : Initializes the arguments
        @inputs : path of the text file
        '''
        self.filepath = filepath

    
    def calculate_total_expense(self):
        '''
        @Description : The method calculates the total expense 
        @returns : total expense
        '''
        total_expense = 0
        with open(self.filepath, 'r') as file:
            for line in file:
                elements = line.split()
                if len(elements) >= 2:
                    if elements[-1].isdecimal():
                        total_expense += float(elements[-1])

        return total_expense
    
obj = ExpenseAnalyzer(r"D:\practice\beginner projects\ExpenseAnalyzer\expenses.txt")
print(obj.calculate_total_expense())