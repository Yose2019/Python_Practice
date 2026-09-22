'''
this function requires to group words based on their first letter
'''

def group_words(word_list):
    if not word_list:
        return {}

    word_groups = {}

    for word in word_list:
        if word:
            word_groups.setdefault(word.lower()[0], []).append(word)

    return word_groups



test_cases = test_cases = [
    [],
    [""],
    ["apple"],
    ["apple", "ant", "banana", "ball", "cat"],
    ["Apple", "ant", "BANANA", "Ball", "cat"],
    ["dog", "", "deer", "cat", "", "camel"],
    ["Zebra", "zoo", "apple", "Ant"],
]

for case in test_cases:
    print(group_words(case))
    