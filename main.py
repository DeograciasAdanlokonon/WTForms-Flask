from flask import Flask, render_template, redirect, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SelectField, TimeField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open = TimeField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close = TimeField('Closing Time e.g. 5.30PM', validators=[DataRequired()])
    coffee = SelectField('Coffe Rating', choices=[('☕️', '☕️'), ('☕️☕️', '☕️☕️'), ('☕️☕️☕️', '☕️☕️☕️'), ('☕️☕️☕️☕️', '☕️☕️☕️☕️'),
                                                 ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️')], validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating', choices=[('✘', '✘'), ('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'),
                                                        ('💪💪💪💪', '💪💪💪💪'), ('💪💪💪💪💪', '💪💪💪💪💪')], validators=[DataRequired()])
    power = SelectField('Power Socket Availability', choices=[('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'),
                                                              ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')], validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


# @app.route('/add', methods=['GET', 'POST'])
# def add_cafe():
#     form = CafeForm()
#
#     if form.validate_on_submit():
#         cafe_name = form.cafe.data
#         location = form.location.data
#         open_time = form.open.data
#         close_time = form.close.data
#         coffe_rate = form.coffee.data
#         wifi_rate = form.wifi.data
#         power_rate = form.power.data
#
#         # Make the form write a new row into cafe-data.csv
#         # with if form.validate_on_submit()
#         with open('cafe-data.csv', 'a', encoding='utf-8') as csv_file:
#             csv_file.write(f"\n{cafe_name}, {location}, {open_time}, {close_time}, "
#                            f"{coffe_rate}, {wifi_rate}, {power_rate}")
#
#             return redirect('cafes')
#
#     return render_template('add.html', form=form)


@app.route('/cafes', methods=['GET', 'POST'])
def cafes():
    form = CafeForm()

    if form.validate_on_submit():
        cafe_name = form.cafe.data
        location = form.location.data
        open_time = form.open.data
        close_time = form.close.data
        coffe_rate = form.coffee.data
        wifi_rate = form.wifi.data
        power_rate = form.power.data

        # Make the form write a new row into cafe-data.csv
        # with if form.validate_on_submit()
        with open('cafe-data.csv', 'a', encoding='utf-8') as csv_file:
            csv_file.write(f"\n{cafe_name}, {location}, {open_time}, {close_time}, "
                           f"{coffe_rate}, {wifi_rate}, {power_rate}")

            flash('Data successfully inserted', 'success')  # send a success message
            return redirect('cafes')

    # Here we read cafe-data.csv and get all rows inside to display
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    return render_template('cafes.html', cafes=list_of_rows, form=form)


if __name__ == '__main__':
    app.run(debug=True)
