'''
The module is phase 2 of the Expense analyser project
This gives the total expense in each category
'''

class ExpenseAnalyser:
    '''
    @Description : The class consists of methods which assist in tracking expenses
    '''
    def __init__(self, filename: str):
        '''
        @Description : The method initializes the parameters
        @inputs : path of the file
        '''
        self.filename = filename


    def calculate_total_expense_categorically(self):
        '''
        @Description : calculates the total expense for each category
        @returns : Dictionary
        '''
        expenses = {}

        with open(self.filename, 'r') as file:
            for line in file:
                # programming considering all possibilities 
                elements = line.split()
                if len(elements) >= 2 and elements[-1].isdecimal():
                    category, expense = " ".join(elements[:-1]), int(elements[-1])
                    expenses[category] = expenses.get(category, 0) + expense

        return expenses 
    
obj = ExpenseAnalyser(r"D:\practice\beginner projects\ExpenseAnalyzer\expenses.txt")
print(obj.calculate_total_expense_categorically())