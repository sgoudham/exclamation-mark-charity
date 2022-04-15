import sqlite3
import sys
from abc import ABC, abstractmethod
from sqlite3 import Connection

from exclamation_mark_charity import DB_FILE, LOGGER


class DatabaseInterface(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def create(self):
        pass


class Sqlite(DatabaseInterface):
    def __init__(self):
        self.conn: Connection = self.connect()

    def connect(self) -> Connection:
        LOGGER.info(f"Connecting to {DB_FILE}...")

        try:
            conn = sqlite3.connect(DB_FILE)
            conn.execute("PRAGMA foreign_keys = ON;")
        except sqlite3.Error as err:
            LOGGER.error(err)
            sys.exit(err)

        LOGGER.info(f"Connection to {DB_FILE} successful!")

        return conn

    def create(self):
        pass

    def insert(self):
        pass
