from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Heroku boilerplate</h1>'


'''
This is taken care of by gunicorn
if __name__ == "__main__":
    app.run(threaded=True, port=5000)
'''
