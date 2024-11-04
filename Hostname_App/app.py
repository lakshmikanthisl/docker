from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/')
def get_hostname():
    # Fetch the hostname of the container
    hostname = socket.gethostname()
    # Return the hostname as JSON response
    return jsonify(hostname=hostname)

if __name__ == '__main__':
    # Run the app on port 80, accessible to all IPs (0.0.0.0)
    app.run(host='0.0.0.0', port=80)

