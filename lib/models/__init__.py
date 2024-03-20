import sqlite3

CONN = sqlite3.connect('flights.db')
CURSOR = CONN.cursor()