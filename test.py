
import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for, g
import _config


app = Flask(__name__)
app.config.from_object(_config)



a = sqlite3.connect(app.config['DATABASE_PATH'])


g.db = a
cur = g.db.execute('select name, due_date, priority, task_id from tasks')
for row in cur.fetchall():
    print row