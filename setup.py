import io

from setuptools import find_packages, setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
<<<<<<< HEAD
    name="ferme connecte",
=======
    name="fermeconnecte",
>>>>>>> 34c6ea91287c606392330f1a79bd8bde05d08852
    version="1.0.0",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
)