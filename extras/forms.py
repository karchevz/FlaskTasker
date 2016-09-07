# project/forms.py


from wtforms import Form, StringField, DateField, IntegerField,\
    SelectField, PasswordField, validators
from wtforms.validators import DataRequired, Length, EqualTo

class AddTaskForm(Form):
    task_id = IntegerField()
    name = StringField('Task Name', [validators.DataRequired()])
    due_date = DateField('Date Due(yyyy-mm-dd)', [validators.DataRequired()])
    priority = SelectField('Priority', [validators.DataRequired()], choices=[('1','1'),('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'), ('8','8'), ('9','9'), ('10','10')])
    status = IntegerField('Status')

class RegisterForm(Form):
    name = StringField('Username', [validators.Length(min=6, max=25)])
    email = StringField('Email', [validators.DataRequired(),validators.Email(), validators.Length(min=6, max=40)])
    password = PasswordField ('Password', [validators.DataRequired(), validators.Length(min=6, max=40)])
    confirm = PasswordField('Repeat Password', [validators.DataRequired(),validators.EqualTo('password', message='Passwords must match.')])

class LoginForm(Form):
    name = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

