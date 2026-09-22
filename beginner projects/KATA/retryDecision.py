'''
project : final decision while attempting to connect to a system
'''

def retry_decision(connection_attempt: list[str]):
    '''
    @Description: the function checks for connection abort
    @Author: Shristhi N Akkalkot
    @inputs: list of outcome of each connection attempt
    @returns: a report 
    '''
    positive = ["success"]

    if not connection_attempt:
        return {}

    retry_count, attempt = (0, 0)

    for con in connection_attempt:
        if con in positive:
            attempt += 1
            retry_count = 0
            break
        elif retry_count < 3 and con not in positive:
            attempt += 1
            retry_count += 1
        elif retry_count == 3:
            break

    decision = "completed" if retry_count == 0 else ("aborted" if retry_count == 3 else "retry")

    return {
        "decision" : decision,
        "attempts" : attempt,
        "failures" : retry_count
    }

results = [
    "timeout",
    "connection_error"
]

print(retry_decision(results))



        
        
        


        

    