import redis
import json

# local ?
LOCAL = False

# Connection de la base redis
redis_client = redis.StrictRedis(host='localhost' if LOCAL else 'redis', charset='utf-8', decode_responses=True)

def redis_init():
    """
    Permet de stocker les données scrapées dans une base de données redis.
    Les données dans la base sont sous la forme clés/valeurs, où les valeurs sont
    ici des dictionnaires tirés de fichiers json.
    """

    # Redis est bien connecté ?
    redis_connected = redis_client.ping()
    print("redis is connected : ", redis_connected)

    # Lecture des données présentes dans les fichiers json
    with open('data/users.json') as users_data :
        users_dict_list = json.load(users_data)

    with open('data/tournois.json') as tournois_data :
        tournois_dict_list = json.load(tournois_data)

    with open('data/participants.json') as participants_data :
        participants_dict_list = json.load(participants_data)

        #print("TOURNOIS_DICT_LIST : ",tournois_dict_list)

    # Stockage des données dans la base de données Redis
    for i in range(len(users_dict_list)):
        redis_client.hmset('user ' + str(i+1), users_dict_list[i])

    for j in range(len(tournois_dict_list)):
        redis_client.hmset('tournoi ' + str(j+1), tournois_dict_list[j])

    for k in range(len(participants_dict_list)):
        redis_client.hmset('participant ' + str(k+1), participants_dict_list[k])

redis_init()
