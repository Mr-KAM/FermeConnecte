import os
import random

class Config:
<<<<<<< HEAD
=======
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or "sqlite:///db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
>>>>>>> 34c6ea91287c606392330f1a79bd8bde05d08852
    SECRET_KEY = os.getenv("SECRET_KEY") or "".join(
        [chr(random.randint(65, 92)) for _ in range(50)]
    )