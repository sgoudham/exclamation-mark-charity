import sqlite3
import sys
from contextlib import closing
from sqlite3 import Connection

from exclamation_mark_charity.constants import DB_FILE
from exclamation_mark_charity.logger_factory import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


class Database:
    def __init__(self):
        pass

    @staticmethod
    def __connect() -> Connection:
        logger.info(f"Connecting to {DB_FILE}...")

        try:
            conn = sqlite3.connect(DB_FILE)
            conn.execute("PRAGMA foreign_keys = ON;")
        except sqlite3.Error as err:
            logger.critical(err)
            sys.exit(err)

        logger.info(f"Connection to '{DB_FILE}' Successful!")
        return conn

    @staticmethod
    def create_tournament(name: str) -> (bool, int):
        sql = '''INSERT INTO Tournament (name) VALUES (?)'''
        tournament_id = -1

        try:
            with closing(Database.__connect()) as conn:
                with conn:
                    with closing(conn.cursor()) as cur:
                        cur.execute(sql, [name])
                        tournament_id = cur.lastrowid
        except sqlite3.Error as err:
            logger.error(err)
            return False, tournament_id

        return True, tournament_id

    def insert(self):
        pass
