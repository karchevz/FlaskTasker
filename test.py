import _config
from functools import wraps

from flask import Flask, flash, redirect, render_template, request, session, url_for, g, Response

from forms import AddTaskForm

from flask_sqlalchemy import SQLAlchemy

from models import Task

app = Flask(__name__)
app.config.from_object(_config)
db = SQLAlchemy(app)

new_task = Task("Gogo", '04/08/2016', '7', '5')

db.session.add(new_task)
db.session.commit()
