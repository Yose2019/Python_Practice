'''
The program analyzes the logs
'''

import pprint

class LogAnalyzer:
    '''
    @Description: The class consists a bunch of fucntions which split the work of the log analyzer
    @Author: Shristhi N Akkalkot
    '''
    def __init__(self, logfile: list[str]):
        '''
        @Description: the init method to initialise parameters
        @Author: Shristhi N Akkalkot
        @inputs: list of strings containing logs
        @returns: None
        '''
        if not logfile:
            raise ValueError("EMPTY LOG")
        self.logs = logfile

    def analyse_log_events(self):
        '''
        @Description: analyse the log events
        @Author: Shristhi N Akkalkot
        @inputs: None
        @returns: returns a dictionary of the event infomation in the log
        '''
        log_event_info = {}

        for log in self.logs:
            if not log:
                continue
            log_level = log.split(":")[0].strip()
            log_event_info[log_level] = log_event_info.get(log_level, 0) + 1

        return log_event_info

    def find_maximum_occuring_error(self):
        '''
        @Description: analyse the log events and find the maximum occuring error
        @Author: Shristhi N Akkalkot
        @inputs: None
        @returns: return the error which occurs maximum number of times
        '''
        error_info = {}

        for log in self.logs:
            if log:
                log_line = log.split(":") 
                if log_line[0].strip() == "ERROR":
                    error_info[log_line[1].strip()] = error_info.get(log_line[1].strip(), 0) + 1
            else:
                continue

        if not error_info:
            return ""
        else:
            max_count, error_mes_max = 0, ""
            for mes, count in error_info.items():
                if count > max_count:
                    max_count = count
                    error_mes_max = mes

            return error_mes_max

    def generate_report(self):
        '''
        @Description: analyse the logs and generate report
        @Author: Shristhi N Akkalkot
        @inputs: None
        @returns: return the report
        '''
        report = {}

        total_events = 0
        for value in self.analyse_log_events().values():
            total_events += value

        report["total_events"] = total_events
        report.update(self.analyse_log_events())
        report["maximum_error_occured"] = self.find_maximum_occuring_error()

        return report


def main():
    events = [
    "INFO: Device initialized",
    "ERROR: Timeout occurred",
    "WARNING: Temperature high",
    "ERROR: Connection lost",
    "INFO: Namespace created",
    "ERROR: Timeout occurred",
    "",
    "WARNING: Temperature high",
    "ERROR: Timeout occurred",
    "INFO: Device ready",
    "ERROR: Connection lost"
    ]
    obj = LogAnalyzer(events)
    pprint.pprint(obj.generate_report())

if __name__ == "__main__":
    main()






