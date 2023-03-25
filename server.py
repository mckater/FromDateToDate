from flask import Flask, redirect, url_for, render_template, session
from flask_wtf import FlaskForm
from wtforms.fields import DateField, TimeField, DateTimeField, SelectField
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '#$%^&*'


class InfoForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    starttime = TimeField('Start Time', format='%H:%M', validators=(validators.DataRequired(),))
    enddate = DateField('End Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    endtime = SelectField(choices=(range(25)))
    submit = SubmitField('Submit')


@app.route('/', methods=['GET','POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        st = form.startdate.data
        session['startdate'] = datetime(day=st.day, month=st.month, year=st.year, hour=form.starttime.data.hour)
        en = form.enddate.data
        session['enddate'] = datetime(day=en.day, month=en.month, year=en.year, hour=int(form.endtime.data))

        return redirect('date')
    return render_template('index.html', form=form)


@app.route('/date', methods=['GET','POST'])
def date():
    startdate = session['startdate']
    enddate = session['enddate']
    return render_template('date.html')


if __name__ == '__main__':
    app.run(debug=True)