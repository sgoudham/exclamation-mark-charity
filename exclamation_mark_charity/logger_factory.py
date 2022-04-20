import logging

from exclamation_mark_charity.constants import LOG_FILE


class LoggerFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename=LOG_FILE, encoding="utf-8", mode="a")
        handler.setFormatter(
            logging.Formatter("[%(asctime)s] [%(levelname)8s] -> %(message)s (%(name)s:%(lineno)s)",
                              "%Y-%m-%d %H:%M:%S"))
        logger.addHandler(handler)
        return logger
