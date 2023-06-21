#Creation des objets

#User
class User:
    def __init__(self):
        self.key = ""
        self.nom_prenoms = ""
        self.telephone = ""
        self.email = ""
        self.status = ""
        self.mot_de_passe = ""
        self.Adresse = ""
        self.pp = ""
        self.Authen = ""
        self.theme = ""
    
    def data(self):
        data_user={
            "key": self.key,
            "nom_prenoms": self.nom_prenoms,
            "telephone": self.telephone,
            "email": self.email,
            "status": self.status,
            "mot_de_passe": self.mot_de_passe,
            "Adresse": self.Adresse,
            "pp": self.pp,
            "Authen": self.Authen,
            "theme": self.theme,

        }
        return data_user


#Produit
class Produit:
    def __init__(self,titre):
        self.key = ""
        self.unite = ""
        self.titre = titre
        self.categorie = ""
        self.description = ""
        self.quantite = ""
        self.prix = ""
    
    def data(self):
        data_produit={
            "key": self.key,
            "titre": self.titre,
            "categorie": self.categorie,
            "description": self.description,
            "quantite": self.quantite,
            "unite": self.unite,
            "prix": self.prix,

        }
        return data_produit

# tomate=produit("Tomate de bonois")


#Panier
class Panier:
    def __init__(self):
        self.key = ""
        self.status = ""
        self.produit = []
        self.Cout_total = ""
        self.cle_user = ""

    def add_to_basket(self, produit):
        self.produit.append(produit)
    
    def data(self):
        data_panier={
            "key": self.key,
            "status": self.status,
            "produit": self.produit,
            "Cout_total": self.Cout_total, 
            "cle_user": self.cle_user,

        }
        return data_panier


#Commande
class Commande:
    def __init__(self):
        self.key = ""
        self.Mode_payement = ""
        self.Date_livraison = ""
        self.cle_panier = ""

    def data(self):
        data_Commande={
            "key": self.key,
            "Mode_payement": self.Mode_payement,
            "Date_livraison": self.Date_livraison,
            "cle_panier": self.cle_panier, 

        }
        return data_Commande


#Notification
class Notification:
    def __init__(self):
        self.key = ""
        self.titre = ""
        self.detail = ""
        self.date = ""
        self.cle_user = ""

    def data(self):
        data_Notification={
            "key": self.key,
            "titre": self.titre,
            "detail": self.detail,
            "date": self.date, 
            "cle_user": self.cle_user,

        }
        return data_Notification

