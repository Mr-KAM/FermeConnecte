from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import flask_login
import flask_admin
import flask_wtf
from flask_assets import Environment, Bundle
from deta import Deta



from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

assets = Environment(app)
assets.url = app.static_url_path
#scss = Bundle('scss/style.scss', filters='pyscss', output='css/style.css')
#assets.register('scss_all', scss)

deta = Deta('a07fcpbdkca_EvyweBBgz1ShmkBr1bfHGaK32bUmrTWF') 
db_U = deta.Base('Utilisateurs') 
db_P = deta.Base('Produits') 
#db.app = app
#db.init_app(app)


@app.route('/users', methods=["POST"])
def create_user():
    nom = request.json.get("nom")
    prenom= request.json.get("prenom")
    email = request.json.get("email")
    contact = request.json.get("contact")
    
    user = db_U.put({
        "nom": nom,
        "prenom": prenom,
        "email": email,
        "contact": contact,
    })

    return jsonify(user, 201)


@app.route("/users/<key>")
def get_user(key):
    user = db_U.get(key)
    return user if user else jsonify({"error": "Not found"}, 404)

@app.route("/users/<key>", methods=["PUT"])
def update_user(key):
    user = db_U.put(request.json, key)
    return user


@app.route("/users/<key>", methods=["DELETE"])
def delete_user(key):
    db_U.delete(key)
    return jsonify({"status": "ok"}, 200)







@app.route('/produits', methods=["POST"])
def create_products():
    titre = request.json.get("titre")
    description = request.json.get("description")
    prix = request.json.get("prix")
    disponibilite = request.json.get("disponibilite")
    
    produit = db_P.put({
        "titre": titre,
        "description": description,
        "prix": prix,
        "disponibilite":disponibilite
    })
    return jsonify(produit, 201)


@app.route('/')
def index():
    return render_template('splash.html')




@app.route("/home", methods=["GET", 'POST'])
def home():
    """
    Home page route
    """
    if request.method == 'POST':
        message = request.form['message']
        return jsonify(your_message=message)
    return render_template("index.html")


#Connexion
@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html', methods=['GET', 'POST'])


#Créer un compte
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    return render_template('signup.html', methods=['GET', 'POST'])


#Base
@app.route("/base")
def base():
    return render_template('base.html', methods=['GET', 'POST'])


#Panier
@app.route("/panier", methods=['GET', 'POST'])
def panier():
    return render_template('panier.html')



#Modifier le profil
@app.route("/settings", methods=['GET', 'POST'])
def settings():
    return render_template('settings.html')




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
