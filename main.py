from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

def calculate_working_hours(start_time, end_time, lunch_length):
    start_time = datetime.strptime(start_time, '%H:%M')
    end_time = datetime.strptime(end_time, '%H:%M')
    time_before_lunch = end_time - start_time - timedelta(minutes=lunch_length)
    hours_worked = time_before_lunch.seconds // 3600
    minutes_worked = (time_before_lunch.seconds // 60) % 60
    return hours_worked, minutes_worked

@app.route('/', methods=['GET', 'POST'])
def index():
    hours_worked = None
    minutes_worked = None

    if request.method == 'POST':
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        lunch_length = int(request.form['lunch_length'])
        hours_worked, minutes_worked = calculate_working_hours(start_time, end_time, lunch_length)

    return render_template('index.html', hours_worked=hours_worked, minutes_worked=minutes_worked)

if __name__ == '__main__':
    app.run(debug=True)
