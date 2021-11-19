from data.redis import *
from app import app
#from app.data import *
import os

# Pour lancer l'app avec Python directement
if __name__ == '__main__':

    # Stockage des données dans une base de données redis
    #redis_init()

    # lancement de l'application flask
    app.run(host='0.0.0.0',debug=True)
