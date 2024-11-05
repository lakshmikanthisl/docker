from flask import Flask, render_template, request
from datetime import datetime
import pytz

app = Flask(__name__)

# Generate a list of time zones from pytz
timezones = pytz.all_timezones

@app.route('/', methods=['GET', 'POST'])
def home():
    # Default timezone
    selected_timezone = "UTC"
    current_time = datetime.now(pytz.timezone(selected_timezone)).strftime('%Y-%m-%d %H:%M:%S')
    
    # If form is submitted, get the selected timezone
    if request.method == 'POST':
        selected_timezone = request.form.get("timezone")
        current_time = datetime.now(pytz.timezone(selected_timezone)).strftime('%Y-%m-%d %H:%M:%S')
    
    return render_template('index.html', timezones=timezones, current_time=current_time, selected_timezone=selected_timezone)

if __name__ == '__main__':
    # Run the app on port 80, accessible to all IPs (0.0.0.0)
    app.run(host='0.0.0.0', port=80)

