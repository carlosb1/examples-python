import time
import logging
from enum import Enum
from threading import  Thread, Event

from tap import Tap

from four_character.tcp import run_server, run_client
from four_character.domain import Report, FourCharacterAnalyzer


def background_task(stop: Event, report: Report):
    while not stop.is_set():
        time.sleep(10)
        logging.info("Checking report")
        report.reset()



class SimpleArgumentParser(Tap):
    mode: str
    message: str = ""
    host: str = "localhost"
    port: int = 1111


class Mode(str, Enum):
    client = 'client'
    server = 'server'


def main():
    logging.basicConfig(level=logging.INFO)
    args = SimpleArgumentParser().parse_args()

    if args.mode == Mode.client:
        message = ''
        # FIXME necessary fix to load parameter
        dic_args = args.as_dict()
        if 'message' in dic_args.keys():
            message = dic_args['message']
        run_client(args.host, args.port, message)
    elif args.mode == Mode.server:
        stop = Event()
        stop.clear()
        report = Report()
        four_character_analyzer = FourCharacterAnalyzer(args.host, args.port, stop, report)

        bg_task = Thread(target=background_task, args=(stop, report, ))
        bg_task.start()

        run_server(args.host, args.port, stop, four_character_analyzer)
        logging.info("Waiting to close background task")
        bg_task.join()


if  __name__ == '__main__':
    main()
