from flask import Flask
import datetime as dt
app = Flask(__name__)


@app.route('/')
def hello():
    time = dt.datetime.now()
    return str(time)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
