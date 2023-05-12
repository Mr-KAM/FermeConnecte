<<<<<<< HEAD

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS






=======
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import flask_login
import flask_admin
import flask_wtf
from flask_assets import Environment, Bundle
from models import db
from deta import Deta
>>>>>>> 34c6ea91287c606392330f1a79bd8bde05d08852


from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

<<<<<<< HEAD


@app.route("/", methods=["GET", 'POST'])
=======
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('scss/style.scss', filters='pyscss', output='css/style.css')
assets.register('scss_all', scss)


db.app = app
db.init_app(app)

@app.route('/')
def index():
    return render_template('splash.html', data="kambou Anicet")

@app.route("/home", methods=["GET", 'POST'])
>>>>>>> 34c6ea91287c606392330f1a79bd8bde05d08852
def home():
    """
    Home page route
    """
    if request.method == 'POST':
        message = request.form['message']
        return jsonify(your_message=message)
    return render_template("index.html")

@app.route("/hello", methods=["GET"])
def hello():
    """
    Hello route
    """
    return 'hello'

@app.route('/message', methods=['POST'])
def message():
    """
    Message route
    """
    message = request.json.get("message")
    return jsonify(your_message=message)

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True, host="0.0.0.0")

    
=======
    app.run(debug=True, host="0.0.0.0")
>>>>>>> 34c6ea91287c606392330f1a79bd8bde05d08852
