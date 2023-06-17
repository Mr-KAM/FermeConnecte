from deta import *  # pip install deta
from dotenv import load_dotenv
from _database import *
from glob import *
import pathlib
load_dotenv()

cle_ferme_connecte = os.environ["cle_ferme_connecte"]
deta = Deta(cle_ferme_connecte)

prod_img=deta.Drive("produit")

local_image="static\img\img_produit\*"
images=glob(local_image)
# print(images)

def add_images(deta_drive,images_path):
    for img_path in images_path:
        # name=img_path.split("\\")[-1]
        name=pathlib.PurePath(img_path).name
        add_file(deta_drive,name,img_path)
        print(f"{name} succesfully added")
        # print("with pathlib:",pathlib.PurePath(img_path).name)
        # print(pathlib.PurePath(img_path).name)

if __name__ == "__main__":
    add_images(prod_img,images)