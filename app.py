from http.client import REQUEST_TIMEOUT
from urllib import request
from flask import Flask
import time

app = Flask(__name__)
app.config['TIMEOUT'] = 30

@app.route('/home')
def home():
    """
    This was to basically display the request timeout functionality.
    However for production usecases, i would consider the following:
    1. Implementing distributed tracing to track all the requests served by the servers.
    2. Implementing logging on the servers to have better visibility on what is happening.
    """
    time.sleep(40)
    return 'My name is Melvin Kimathi and I love Backend and Site Reliability Engineering.'

if __name__ == '__main__':
    app.run(debug=False, port=5000, threaded=True)