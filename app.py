from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import flask_login
import flask_admin
import flask_wtf
from flask_assets import Environment, Bundle
from models import db
from deta import Deta


from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

assets = Environment(app)
assets.url = app.static_url_path
#scss = Bundle('scss/style.scss', filters='pyscss', output='css/style.css')
#assets.register('scss_all', scss)


db.app = app
db.init_app(app)

@app.route('/')
def index():
    return render_template('splash.html', data="kambou Anicet")

@app.route("/home", methods=["GET", 'POST'])
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

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html', methods=['GET', 'POST'])

@app.route("/base")
def base():
    return render_template('base.html', methods=['GET', 'POST'])

@app.route("/panier", methods=['GET', 'POST'])
def panier():
    return render_template('panier.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    return render_template('signup.html', methods=['GET', 'POST'])

@app.route("/settings", methods=['GET', 'POST'])
def settings():
    return render_template('settings.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
