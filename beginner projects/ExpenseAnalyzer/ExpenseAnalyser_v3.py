'''
This module is phase 3 of the expense analyser project
'''

class ExpenseAnalyzer:
    '''
    @Description : The class consists of useful methods required for expense analysis
    '''
    def __init__(self, filepath: str):
        '''
        @Description : this initializes the parameters
        @inputs : path of the file
        '''
        self.filepath = filepath

    
    def categorical_expense(self):
        '''
        @Description : the function returns the category with the maximum expense in total
        @returns : Dictionary 
        '''
        category_expense = {}

        with open(self.filepath, 'r') as file:
            for line in file:
                elements = line.split()
                if len(elements) >= 2 and elements[-1].isdecimal():
                    category, expense = " ".join(elements[:-1]), float(elements[-1])
                    category_expense[category] = category_expense.get(category, 0) + expense

        return category_expense


    def maximum_expense_category(self):
        '''
        @Description : the function returns the category with the maximum expense in total
        @returns : Dictionary 
        '''
        category_expense = self.categorical_expense()
        if not category_expense:
            return {}
        
        maximum_spent_category = {}

        maximum_spent = float("-inf")

        for exp in category_expense.values():
            if exp > maximum_spent:
                maximum_spent = exp 

        for category, exp in category_expense.items():
            if exp == maximum_spent:
                maximum_spent_category[category] = exp 

        return maximum_spent_category
    

obj = ExpenseAnalyzer(r"D:\practice\beginner projects\ExpenseAnalyzer\expenses.txt")
for k, v in obj.maximum_expense_category().items():
    print(f"Category is :{k} and amount is : {v}")


