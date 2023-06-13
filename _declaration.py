# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import string

data = {}


def declarations():
    for i in range(1, 15):
        numero = f"Article-{i}"
        auteur = "".join(
            random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10)
        )
        date = f"{random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(2010, 2023)}"
        types = ["poulet", "mouton", "tomate","lait"]
        lieu = "".join(
            random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10)
        )
        description = "".join(
            random.choices(
                string.ascii_uppercase
                + string.ascii_lowercase
                + string.digits
                + string.punctuation,
                k=30,
            )
        )

        type=random.choice(types)
        photo = f'img/{type}.jpg'
        data[numero] = {
            "auteur": auteur,
            "date": date,
            "type": type,
            "lieu": lieu,
            "description": description,
            "photo": photo,
            "quantite":random.randint(0,50)
        }

    return data
