import logging
from threading import Event
from four_character import tcp

class Report:
    def __init__(self):
        self.total_numbers = 0
        self.last_total_numbers = 0
        self.last_duplicated_numbers = 0
        self.digits = {}

    def add_digit(self, digit):
        self.total_numbers += 1
        self.last_total_numbers += 1
        if digit not in self.digits.keys():
            self.digits[digit] = 1
        else:
            self.digits[digit] +=1
            self.last_duplicated_numbers +=1


    def reset(self):
        self.last_total_numbers = 0
        self.last_duplicated_numbers = 0
        self.digits = {}

MSG_TERMINATE = "terminate"

class FourCharacterAnalyzer:
    def __init__(self, host, port, stop: Event, report: Report):
        self._stop = stop
        self._report = report
        self._host = host
        self._port = port
    def run(self, data: str):
        logging.info(f'decode={data}')
        if data == MSG_TERMINATE:
            self._stop.set()
            tcp.run_client(self._host, self._port, "")
        if len(data) != 9:
            return
        if not data.isdigit():
            return
        self._report.add_digit(data)
