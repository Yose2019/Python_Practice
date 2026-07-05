'''
This module is phase 4 of the expense analyser project
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

    
    def categorical_expense(self, requirement: str = "overall"):
        '''
        @Description : the function returns the category with the expense in total along with the count
        @returns : Dictionary 
        '''
        categorical_expense_cnt = {}
        total_expense, total_transactions = 0, 0
        
        with open(self.filepath, 'r') as file:
            for line in file:
                elements = line.split()
                if len(elements) >= 2 and elements[-1].isdecimal():
                    category, expense = " ".join(elements[:-1]), int(elements[-1])
                    total_expense += expense
                    total_transactions += 1
                    expense_list = categorical_expense_cnt.get(category, [0] * 2)
                    categorical_expense_cnt[category] = [expense_list[0] + expense,
                                                         expense_list[1] + 1]

        if requirement == "overall":
            return total_expense, total_transactions

        elif requirement == "categorical":  
            return categorical_expense_cnt
        
        else:
            return 0


    def average_categorical_expense(self, requirement: str = "overall"):
        '''
        @Description : the function returns the average of each category
        @returns : Dictionary 
        '''
        avg_categorical_expense = {}
        if requirement == "categorical":
            categorical_expense_with_count = self.categorical_expense(requirement = requirement)

            if not categorical_expense_with_count:
                return {}
            
            for k, v in categorical_expense_with_count.items():
                avg_categorical_expense[k] = round((v[0] / v[1]), 2)

            return avg_categorical_expense
        
        elif requirement == "overall":
            total_expense, total_transaction = self.categorical_expense(requirement=requirement)
            return round(total_expense/total_transaction, 2)

        else:
            raise ValueError("Requirement not catered")
    


try:
    obj = ExpenseAnalyzer(r"D:\practice\beginner projects\ExpenseAnalyzer\expenses.txt")


    for k, v in obj.average_categorical_expense(requirement = "categorical").items():
        print(f"Category is :{k} and average amount is : {v}")

    avg = obj.average_categorical_expense(requirement = "overall")
    print(f"Average expense per transaction is : {avg}")

except ValueError:
    print("An exception")

