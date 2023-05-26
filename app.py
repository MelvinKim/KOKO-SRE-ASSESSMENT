from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return 'My name is Melvin Kimathi and I love Backend and Site Reliability Engineering.'

if __name__ == '__main__':
    app.run(debug=True) #TODO: change debug=False, when deploying to prod