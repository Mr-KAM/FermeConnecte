from flask import Flask, jsonify, request
from deta import Deta


import app
token_v1="a0svny8no8f_hqjDe1RXi4VMPDUWWTpPsygx4A3XW2k4"

deta = Deta(token_v1)

# Creation des bases de données de la collection ferme_connecte
users = deta.Base("users")
produits = deta.Base("produits")
commandes = deta.Base("commandes")
paniers = deta.Base("paniers")
notifications = deta.Base("notifications")

# Creation des drives de la collection ferme_connecte

pp_drive = deta.Drive("pp")
produits_drive = deta.Drive("produit")

# print(users.fetch().items)



utilisateur1=homme("Binate","email@gmail.com","123456789")
print(utilisateur1.nom_prenoms)
print("Ancienne taille: ")
utilisateur1.ecrire_taille()
utilisateur1.modifier_taille(500)
utilisateur1.masse=200

print(f"nouvelle taille: {utilisateur1.taille}")

# {
#     "nom": str,
#     "prenom": str,
#     "email": str,
#     "tel": int,
# }


# @app.route("/users", methods=["POST"])
# def create_user():
#     nom = request.json.get("nom")
#     prenom = request.json.get("prenom")
#     email = request.json.get("email")
#     contact = request.json.get("contact")

#     user = db.put(
#         {
#             "nom": nom,
#             "prenom": prenom,
#             "email": email,
#             "contact": contact,
#         }
#     )

#     return jsonify(user, 201)


# @app.route("/users/<key>")
# def get_user(key):
#     user = db.get(key)
#     return user if user else jsonify({"error": "Not found"}, 404)


# @app.route("/users/<key>", methods=["PUT"])
# def update_user(key):
#     user = db.put(request.json, key)
#     return user


# @app.route("/users/<key>", methods=["DELETE"])
# def delete_user(key):
#     db.delete(key)
#     return jsonify({"status": "ok"}, 200)


# @app.route("/produits", methods=["POST"])
# def create_products():
#     titre = request.json.get("titre")
#     description = request.json.get("description")
#     prix = request.json.get("prix")
#     disponibilite = request.json.get("disponibilite")

#     produit = db.put(
#         {
#             "titre": titre,
#             "description": description,
#             "prix": prix,
#             "disponibilite": disponibilite,
#         }
#     )
#     return jsonify(produit, 201)
