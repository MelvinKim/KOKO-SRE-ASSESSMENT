from http.client import REQUEST_TIMEOUT
from urllib import request
from flask import Flask, json
import time

app = Flask(__name__)
app.config['TIMEOUT'] = 30

@app.route('/home')
def home():
    """
    This was to basically demonstrate the request timeout functionality.
    However for production usecases, i would consider the following:
    1. Implementing distributed tracing to track all the requests served by the servers.
    2. Implementing logging on the servers to have better visibility on what is happening.
    """
    time.sleep(40)
    data = "My name is Melvin Kimathi and I love Backend and Site Reliability Engineering."
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(debug=False, port=5000, threaded=True)