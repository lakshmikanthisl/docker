from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def display_all_timezones():
    # Get the current time in all timezones
    times_in_timezones = {}
    for timezone in pytz.all_timezones:
        tz = pytz.timezone(timezone)
        time_in_tz = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
        times_in_timezones[timezone] = time_in_tz
    
    # Return the time zones with current times as JSON
    return jsonify(times_in_timezones)

if __name__ == '__main__':
    # Run the app on port 80, accessible to all IPs (0.0.0.0)
    app.run(host='0.0.0.0', port=80)

