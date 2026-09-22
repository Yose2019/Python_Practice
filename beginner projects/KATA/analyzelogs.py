'''
the function analyses logs and returns the count of each error message
'''
import pprint

def analyze_logs(log: list):
    '''
    the main function which analyses the logs 
    '''
    if not log:
        return {}

    analysed_logs = {}

    for message in log:
        message = message.split(":")[0]
        analysed_logs[message] = analysed_logs.get(message, 0) + 1

    return analysed_logs

def main():
    logs = [
    "INFO: Server started",
    "ERROR: Database connection failed",
    "INFO: User logged in",
    "WARNING: Disk space low",
    "ERROR: Timeout occurred",
    "INFO: Request completed",
    ]
    pprint.pprint(analyze_logs(logs))

if __name__ == "__main__":
    main()
