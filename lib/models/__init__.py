import sqlite3

CONN = sqlite3.connect('flights_management_system.db')
CURSOR = CONN.cursor()