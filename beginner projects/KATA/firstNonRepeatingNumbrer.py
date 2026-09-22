'''
the program finds the first non-repeating number

Note: return None if that scenario does not exist
'''

def non_repeating_number(numbers):
    '''
    First non-repeating number is returned
    '''

    if not numbers:
        return None


    non_repeating_numbers = {}

    for num in numbers:
        non_repeating_numbers[num] = non_repeating_numbers.get(num, 0) + 1

    for num, times in non_repeating_numbers.items():
        if times == 1:
            return num

    return None


tests = [[],
[1],
[1, 1],
[1, 2, 1],
[1, 2, 2, 3, 3],
[4, 5, 1, 2, 0, 4, 1, 2]]

for test in tests:
    print(non_repeating_number(test))