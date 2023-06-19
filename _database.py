# -*- coding: utf-8 -*-

# 〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜
# [0] [Importation des modules]
# 〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜
from __future__ import unicode_literals

# from deta import *

# # import bcrypt
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

# 〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜
# [1] [Creation des fonctions pour l'ajout d'utilisateur ]
# 〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜


def add_user(db, user):
    """
    Pour ajouter un utilisateur à ajouter un utilisateur
    arguments:
        db: deta base
        user: objet utilisateur
    return: True si ajouter sinon False 

    """
    
    hashed = generate_password_hash(user.password)
    print("===========================")
    try:
        db.put(
            {
                "key": user.tel,
                "pp": user.pp,
                "nom": user.nom,
                "prenoms": user.prenoms,
                "naissance": user.naissance,
                "piece": user.piece,
                "npiece": user.npiece,
                "tel": user.tel,
                "email": user.email,
                "password": hashed,
                "validate": user.validate,
            },
            expire_in=600,
        )
        print("-------User enregistré")
        return True
    except:
        print("++++ user pas enrégistré")
        return False


def save_file(drive_name, file_name, file_data):
    try:
        drive_name.put(file_name, data=file_data)
        print("-------Image user sauvegardé")
        return True
    except:
        drive_name.put(file_name, path="static/img/profile-default.png")
        print("++++ erreur sauvegarde image")
        return False


def get_user(db, key):
    user = db.get(key)
    return user if user else False


def user_exist(db, key):
    user = db.get(key)
    return True if user else False


def update_user(db, key, new_data, expire_in):
    user = db.put(new_data, key, expire_in=expire_in)
    return user


def delete_user(db, key):
    db.delete(key)
    return jsonify({"status": "ok"}, 200)


def pass_correct(passeword, hashed):
    result = check_password_hash(hashed, passeword)
    return result


def authentification(key, passeword):
    if get_user(key):
        if pass_correct(passeword, get_user(key).password):
            return True
        else:
            return False
    else:
        return None


# Manipulation de données===================================================================================

def get_all(db):
    print("-----telechargement de base de donnée")
    try:
        data=db.fetch().items
        return data
    except: return None

def get_data(db, key):
    data = db.get(key)
    return data if data else None

def delete_data(db, key):
    db.delete(key)
    return jsonify({"status": "ok"}, 200)

def add_data(db,data):
    try:
        db.put(data)
        return True
    except: return False

def data_exist(db, key):
    data = db.get(key)
    return True if data else False

def add_file(drive_name, file_name, path):
    try:
        drive_name.put(file_name, path=path)
        print("-------Image user sauvegardé")
        return True
    except:
        drive_name.put(file_name, path="static/img/profile-default.png")
        print("++++ erreur sauvegarde image")
        return False

def get_file(drive_name, file):
    file = drive_name.get(file_name)
    return file.read() if file else False
# 〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜
# [3] [Creation des objets pour la base de données ]
# 〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜


class utilisateur:
    def __init__(self):
        self.key = ""
        self.pp = ""
        self.nom = ""
        self.prenoms = ""
        self.naissance = ""
        self.piece = ""
        self.npiece = ""
        self.tel = ""
        self.email = ""
        self.passeword = ""
        self.validate = False
        
    def data(self):
        return {
            "key":self.key,
        }


class db_produit:
    def __init__(self):
        pass
    def data(self):
        return {
            "key":self.key,
        }

class db_panier:
    def __init__(self):
        pass
    def data(self):
        return {
            "key":self.key,
        }
        
class db_commande:
    def __init__(self):
        pass
    def data(self):
        return {
            "key":self.key,
        }



