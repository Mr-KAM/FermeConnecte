from flask import Flask, jsonify, request
from deta import Deta


import app

deta = Deta('a07fcpbdkca_EvyweBBgz1ShmkBr1bfHGaK32bUmrTWF') 
db = deta.Base('Utilisateurs') 





{
        "nom": str,
        "prenom": str,
        "email": str,
        "tel": int,
}



@app.route('/users', methods=["POST"])
def create_user():
    nom = request.json.get("nom")
    prenom= request.json.get("prenom")
    email = request.json.get("email")
    contact = request.json.get("contact")
    
    user = db.put({
        "nom": nom,
        "prenom": prenom,
        "email": email,
        "contact": contact,
    })

    return jsonify(user, 201)


@app.route("/users/<key>")
def get_user(key):
    user = db.get(key)
    return user if user else jsonify({"error": "Not found"}, 404)

@app.route("/users/<key>", methods=["PUT"])
def update_user(key):
    user = db.put(request.json, key)
    return user


@app.route("/users/<key>", methods=["DELETE"])
def delete_user(key):
    db.delete(key)
    return jsonify({"status": "ok"}, 200)







@app.route('/produits', methods=["POST"])
def create_products():
    titre = request.json.get("titre")
    description = request.json.get("description")
    prix = request.json.get("prix")
    disponibilite = request.json.get("disponibilite")
    
    produit = db.put({
        "titre": titre,
        "description": description,
        "prix": prix,
        "disponibilite":disponibilite
    })
    return jsonify(produit, 201)








