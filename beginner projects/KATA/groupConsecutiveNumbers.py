'''
The program groups lists of consecutive numbers
'''

def group_consecutive_numbers(number_list):
    '''
    The function does what it is supposed to do
    '''
    group = []

    if not number_list:
        return group

    subgroup = []

    for idx in range(len(number_list) - 1):
        if number_list[idx] == number_list[idx + 1] - 1:
            subgroup.append(number_list[idx])
        else:
            subgroup.append(number_list[idx])
            group.append(subgroup)
            subgroup = []

    if subgroup:
        if number_list[-1] - 1 == subgroup[-1]:
            subgroup.append(number_list[-1])
            group.append(subgroup)
        else:
            group.append(subgroup)
            group.append([number_list[-1]])



    # start, end = 0, 0
    # for idx in range(len(number_list) - 1):
    #     if number_list[idx] == number_list[idx + 1] - 1:
    #         end += 1
    #     else:
    #         end += 1
    #         group.append(number_list[start:end])
    #         start = end 

    # group.append(number_list[start:])
    return group


test_cases = [
    # Basic
    [1, 2, 3, 7, 8, 10, 11, 12],
    [5, 6, 10, 11, 12, 20],

    # Empty / single
    [],
    [42],

    # Everything consecutive
    [1, 2, 3, 4, 5],
    [-3, -2, -1, 0, 1],

    # Nothing consecutive
    [1, 5, 10, 20],
    [10, 7, 3, 1],

    # Duplicates
    [1, 2, 2, 3],
    [1, 1, 2, 3],
    [1, 2, 3, 3, 4],
    [5, 5, 5],

    # Negative numbers
    [-5, -4, -3, 0, 1, 2],
    [-10, -9, -7, -6, -5],

    # Mixed gaps
    [1, 2, 5, 6, 10, 11, 12, 20],
    [100, 101, 105, 106, 107, 110],

    # Unordered input — important!
    [3, 1, 2, 7, 6, 8],
    [10, 11, 5, 6, 7, 1],

    # A slightly nasty one
    [1, 2, 4, 5, 6, 10, 11, 13, 14, 15, 16],

    # Another nasty one
    [-3, -2, -2, -1, 0, 2, 3, 5, 5, 6],
]
for case in test_cases:
    print(group_consecutive_numbers(case))


