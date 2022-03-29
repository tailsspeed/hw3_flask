from app import myobj
from app.forms import Form
from flask import render_template, flash

#declared globally in routes.py
name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]

@myobj.route('/')
def home():
    return render_template('home.html', name = name, city_names = city_names)

@myobj.route('/test')
def test():
    form = Form()
    if form.validate_on_submit():
        flash(f'{form.cityname.data}')
    return render_template('city.html', form = form)
