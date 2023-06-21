# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from urllib.parse import urlparse, urljoin
import os

# 〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜
# [0] [Importation des modules et packages]
# 〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜
from deta import *  # pip install deta
from jinja2 import *  # pip install jinja2"
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    jsonify,
    session,
)  # pip install flask

from mailer import Mailer  # pip install quick-mailer
from flask_login import (
    LoginManager,
    UserMixin,
    login_required,
    login_user,
    logout_user,
    current_user,
)  # pip install flask-login
from pushbullet import Pushbullet  # pip install pushbullet

from _database import *
from _forms import *
from _validation import *
from _declaration import *

# --------------------------- {Module de chiffrage} ----------------------------------------


# 〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜
# [1] [Configuration de Deta et initialisation des bases de données]
# 〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜
# ================ {initialisation du projet} ===============

# print(os.environ)
from dotenv import load_dotenv

load_dotenv()
# ================Deta config
cle_ferme_connecte = os.environ["cle_ferme_connecte"]
deta = Deta(cle_ferme_connecte)
# =================Pushbullet config
push_key = os.environ["push_key"]
pb = Pushbullet(push_key)
# ================ {Base de données} ===============

users = deta.Base("users")
commandes = deta.Base("commandes")
paniers = deta.Base("paniers")
produits=deta.Base("produits")
notifications = deta.Base("notifications")


# ================ {drive} ===============
users_pp = deta.Drive("pp")
produit_img=deta.Drive("produit")
# ================ {Variables} ==================


app = Flask(__name__)


app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
mail = Mailer(
    email=os.environ["centrale_email"], password=os.environ["centrale_email_password"]
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = "Connectez-vous pour accéder à cette page."
# 〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜
# [2] [definition des fonctions ]
# 〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ("http", "https") and ref_url.netloc == test_url.netloc


def get_redirect_target():
    for target in request.values.get("next"), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return target


def redirect_back(endpoint, **values):
    target = request.form["next"]
    if not target or not is_safe_url(target):
        target = url_for(endpoint, **values)
    return redirect(target)


class dict_to_user(UserMixin):
    def __init__(self, data):
        for key, value in data.items():
            self.__dict__[key] = value

    def get_id(self):
        return self.key

@app.context_processor
def utility_processor():
    def extract_part(valeur,len):
        # print(valeur)
        return valeur[0:len]
    return dict(extract_part=extract_part)

@app.context_processor
def utility_processor():
    def format_image(key):
        try:
            file_name=[fichier for fichier in produit_img.list()["name"] if fichier.split(".")[0]==key][0]
            file_data=get_file(produit_img,file_name)
            file_extension=file_name.split(".")[-1]
            return f"data:image/{file_extension};base64,{file_data}"
        except:
            return "static/img/logo.png"
    return dict(format_image=format_image)

@login_manager.user_loader
def load_user(user_id):
    data = users.get(user_id)
    user = dict_to_user(data)
    return user


@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("accueil"))
    else:
        return render_template("index.html")


@app.route("/carousel/")
def carousel():
    if current_user.is_authenticated:
        return redirect(url_for("accueil"))
    else:
        return render_template("carousel.html")


@app.route("/signup/", methods=["POST", "GET"])
def signup():
    print(get_all(users))
    if request.method == "POST":
        user = utilisateur()
        user.nom = request.form["nom"]
        user.prenoms = request.form["prenoms"]
        user.naissance = request.form["naissance"]
        user.npiece = request.form["npiece"]
        user.piece = request.form["piece"]
        user.tel = request.form["tel"]
        user.key = user.tel
        user.email = request.form["email"]
        user.password = request.form["password"]
        passwordconfirm = request.form["passwordconfirm"]
        user.pp = str(user.tel) + ".png"
        user.validate = False
        if user_exist(users, user.tel):
            return render_template(
                "signup.html",
                message="user-exist",
            )
        elif not get_user(users, user.tel) and passwordconfirm != user.password:
            return render_template(
                "signup.html",
                message="passe-confirm-error",
            )
        elif (
            not user_exist(users, user.tel)
            and passwordconfirm == user.password
            and passwordconfirm != ""
        ):
            if request.files["pp"]:
                file_data = request.files.get("pp")
                print(file_data)
                file_ext = file_data.filename.split(".")[-1]
                user.pp = str(user.tel) + "." + file_ext
                save_file(users_pp, user.pp, file_data)

            else:
                file_data = open("static/img/profile-default.png", "rb")
                file_name = str(user.tel) + ".png"
                save_file(users_pp, file_name, file_data.readlines())
                file_data.close()

            user.validate = gen_validation_code()
            message = validation_message(user.validate)
            objet = "VALIDATION DE MAIL POUR FERME CONNECTEES"
            destination = user.email
            result = add_user(users, user)
            print("reponse d'ajout utilisateur:", result)
            if not result:
                return render_template(
                    "signup.html",
                    message="erreur",
                )
            else:
                send_mail(mail, objet, message, destination)
                return redirect(url_for("validation", key=user.key, mode=1))
        else:
            return render_template(
                "signup.html",
                message="passe-vide",
            )
    else:
        if current_user.is_authenticated:
            return redirect(url_for("accueil"))
        else:
            return render_template("signup.html", message="")


@app.route("/validation/<key>/<mode>", methods=["POST", "GET"])
def validation(key, mode):
    print(get_all(users))
    user = get_user(users, key)
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for("accueil"))
        else:
            if user:
                print(key)
                if int(mode) == 1:
                    print(user)
                    print("par mail")
                    # print(user.validate)
                    return render_template(
                        "validation.html", message="1", mode=mode, key=key
                    )
                else:
                    code = get_user(users, key)["validate"]
                    number = key
                    print(key)
                    sendSms(pb, number, code)
                    return render_template(
                        "validation.html", message="", mode=mode, key=key
                    )
            else:
                return render_template("session_error.html")
    else:
        code = str(
            str(request.form["n1"])
            + str(request.form["n2"])
            + str(request.form["n3"])
            + str(request.form["n4"])
            + str(request.form["n5"])
            + str(request.form["n6"])
        )
        print(code)
        confirmation = validate_user(users, key, code)
        if confirmation:
            return redirect(url_for("login"))
        else:
            return render_template(
                "validation.html", message="bad-code", mode=mode, key=key
            )


@app.route("/login/", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("accueil"))
    if request.method == "POST":
        input_key = request.form["key"]
        if input_key == "":
            return render_template("login.html", message="login-error")
        else:
            print(f"Tentative de connexion de : {input_key}")
            input_password = request.form["password"]
            user = get_user(users, input_key)
        if user and pass_correct(input_password, user["password"]) and user["validate"]:
            print("======Login user added successfully")
            print(user)
            remember = request.form["remember"]
            login_user(load_user(input_key), remember=remember)
            next = request.args.get("next")
            if not is_safe_url(next):
                return abort(400)
            print(current_user)
            return redirect(next or url_for("accueil"))
        elif (
            user
            and pass_correct(input_password, user["password"])
            and not user["validate"]
        ):
            return redirect(url_for("validation", key=input_key))
        else:
            return render_template("login.html", message="login-error")
    return render_template("login.html", message="")


@app.route("/accueil", methods=["POST", "GET"])
@login_required
def accueil():
    declar = declarations()
    list_produits=get_all(produits)
    try:
        pp_name=current_user.pp
        pp_data=users_pp.get(pp_name).read()
        pp_extension=pp_name.split('.')[-1]
        image_source="static/img/pp/"+pp_name
        # print(image_source)
        with open(image_source,"wb") as a:
            a.write(pp_data)
        # pp_file=open(image_source,"w")
        pp_src=image_source
    except:
        pp_src="static/img/profile-default.png"
    # print(pp_src)
    list_keys=[key["key"] for key in list_produits]
    print("Liste des clés: ",list_keys)
    # for key in list_keys:
        # file_name=[fichier for fichier in product_img.list() if fichier.split(".")[0]==key][0]
        # print(file_name)
    print("Liste des images de produits:", produit_img.list())
    # print(list_produits)
    return render_template("accueil.html", produits=list_produits, pp_src=pp_src)


@app.route("/declaration/")
@login_required
def declaration():
    declar = declarations()
    return render_template("declaration.html", declarations=declar)


# Afficher le panier

@app.route('/panier/')
@login_required
def panier():
    return render_template('panier.html')


@app.route("/details/<key>",methods=["POST","GET"])
@login_required
def details(key):
    produit=get_data(produits,key)
    print("Detail produit: ")
    print("==================")
    print(produit)
    return render_template('details.html',produit=produit)


@app.route("/settings")
@login_required
def settings():
    return render_template("settings.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")
