'''
Longest consecutive integer - find the longest substring with consecutive numbers
'''

def longest_consecutive_streak(number_list: list):
    '''
    @definition: the function gives the longest streak of consecutive numbers
    '''

    if not number_list:
        return []
    
    start = 0
    sublists = []

    for ind in range(1, len(number_list)):
        if number_list[ind] == number_list[ind - 1] + 1:
            continue
        else: 
            if ind - start > len(sublists):
                sublists = number_list[start: ind]
            start = ind

    if len(number_list) - start > len(sublists): 
        sublists = number_list[start:]

    return sublists


test_cases = [
    # Empty / single element
    [],
    [42],

    # Basic cases
    [1, 2, 3, 7, 8, 10],
    [5, 6, 10, 11, 12, 20],

    # Entire list is consecutive
    [1, 2, 3, 4, 5],
    [-3, -2, -1, 0, 1],

    # No consecutive numbers
    [1, 5, 10, 20],
    [10, 7, 3, 1],

    # Tie cases — first streak should win
    [1, 2, 3, 10, 11, 12],
    [5, 6, 20, 21],

    # Duplicates break the streak
    [1, 2, 2, 3, 4],
    [1, 1, 2, 3],
    [5, 6, 6, 7, 8],

    # Negative numbers
    [-5, -4, -3, 0, 1, 2],
    [-10, -9, -7, -6, -5],

    # Multiple streaks
    [1, 2, 5, 6, 7, 10, 11],
    [100, 101, 102, 5, 6, 20],

    # Long streak at the end
    [10, 20, 30, 4, 5, 6, 7],

    # Long streak at the beginning
    [1, 2, 3, 4, 10, 20],

    # Unordered input — preserve original order
    [3, 1, 2, 7, 8, 9],
    [10, 11, 5, 6, 7, 1],

    # Slightly nasty cases
    [1, 2, 4, 5, 6, 10, 11, 13, 14, 15, 16],
    [-3, -2, -2, -1, 0, 2, 3, 5, 5, 6],

    # Tie involving single elements
    [5, 10, 20, 30],
]

for i in test_cases:
    print(longest_consecutive_streak(i))

    
    