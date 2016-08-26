# project/db_create.py

import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

    # get a cursor object used to execute SQL command
    c = connection.cursor()

    # create the talbe
    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL,
              status INTEGER NOT NULL)""")

    # insert dummy data into the table
    c.execute('INSERT INTO tasks (name, due_date, priority, status) VALUES("Finish the tutorial", 03/25/2016, 10, 1)')

    # add some more data
    c.execute('INSERT INTO tasks (name, due_date, priority, status) VALUES("Finish the second course", 03/26/2016, 5, 1)')