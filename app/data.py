import pandas as pd
import os

from data.redis import *

# Import des données de la BDD Redis dans des dataframes pandas

# Users
def get_users():
    users =[]

    keys = redis_client.keys()

    for key in keys:
        if 'user' in key:
            users.append(pd.DataFrame(redis_client.hgetall(key), index=[key]))

    df_users = pd.concat(users)

    return df_users

# Tournois
def get_tournois():
    tournois =[]

    keys = redis_client.keys()

    for key in keys:
        if 'tournoi' in key:
            tournois.append(pd.DataFrame(redis_client.hgetall(key), index=[key]))

    df_tournois= pd.concat(tournois)

    return df_tournois

# Participants
def get_participants():
    participants =[]

    keys = redis_client.keys()

    for key in keys:
        if 'participant' in key:
            participants.append(pd.DataFrame(redis_client.hgetall(key), index=[key]))

    df_participants= pd.concat(participants)

    return df_participants


# Users dictionnaire
def get_dict_users():
    dict_users =[]

    for key in keys:
        if 'user' in key:
            dict_users.append(redis_client.hgetall(key), index=[key])

    return dict_users

# Get Keys
def get_keys():
    keys = redis_client.keys()
    #for key in redis_client.scan_iter("user"):
        #keys.append(key)
    return keys

### DataFrame
df_users = get_users()
df_tournois = get_tournois()
df_participants = get_participants()

df_keys = get_keys()

print('DF_USERS : ',df_users)
print('\nDF_TOURNOIS : ',df_tournois)
print('\nDF_PARTICIPANTS : ',df_participants)

def get_liste_tournois():
    df_tournois = get_tournois()
    options_inscription = []
    for i in range(len(df_tournois)):
        option = {}
        option['label'] = df_tournois["nom"].iloc[i]
        option['value'] = df_tournois["nom"].iloc[i]
        options_inscription.append(option)
    return options_inscription

liste_tournois = get_liste_tournois()
print("\nListe_tournois :",liste_tournois)
