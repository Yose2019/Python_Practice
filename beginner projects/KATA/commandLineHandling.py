'''
to build the command line tool history generator 
-- first, keep a list of all unique commands - they are case sensitive
'''
import pprint

def command_line_utility(commands: list[str]):
    '''
    flow -> first is checking whether the command has occured for first time or not 
    '''
    if not commands: # save the efforts
        return {}

    unique_commands = [] # this will hold cleaned commands
    command_occurence = [] # this will hold the first occurence
    duplicate_command = 0
    

    for cmd in commands:
        if cmd.strip() and cmd.strip() not in unique_commands: # this means it is first occurence and not empty
            unique_commands.append(cmd.strip())
            command_occurence.append(cmd)
        else:
            if cmd.strip():
                duplicate_command += 1

    return {
        "cleaned_commands" : command_occurence,
        "original_command_count" : len(commands),
        "cleaned_command_count": len(unique_commands),
        "duplicate_command_count": duplicate_command
    }


commands = [
    "     git status    ",
    "  git status  ",
    "python test.py",
    "GIT STATUS",
    " ",
    "pytest",
    "python test.py  ",
    "git pull",
    "pytest",
    "   git pull   ",
    "",
    "GIT PULL"
]
pprint.pprint(command_line_utility(commands))





