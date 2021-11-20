
import dash
from dash.dependencies import *
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.figures import *
from app.data import *

from werkzeug.security import generate_password_hash

from data.redis import *

from flask_login import login_user, logout_user, current_user

# Callbacks pour rafraichir et mettre à jour les différentes figures et composants
def register_callbacks(dashapp):
    @dashapp.callback([Output('log-button-msg', 'data'), Output('log-button-color', 'data'), Output('login-status', 'data')],
    [Input('go-log-button', 'n_clicks')])
    def update_data_log_button(n_clicks):
        if current_user.is_authenticated == True:
            log_button_msg = 'Déconnexion'
            log_button_color = 'warning'
            login_status = 'connected'
        else:
            log_button_msg = 'Connexion'
            log_button_color = 'success'
            login_status = 'loggedout'
        return log_button_msg, log_button_color, login_status

    @dashapp.callback([Output('go-log-button', 'children'), Output('go-log-button', 'color')],
    [Input('login-status', 'data')],
    [State('log-button-msg', 'data'), State('log-button-color', 'data')])
    def update_log_button(n_clicks, log_button_msg, log_button_color):
        return log_button_msg, log_button_color

    @dashapp.callback([Output('go-log-button', 'href')],
    [Input('go-log-button', 'n_clicks')],
    [State('go-log-button', 'href')])
    def logout(n_clicks, href):
        if n_clicks==None:
            pass
        else:
            if current_user.is_authenticated:
                href = None
                logout_user()
            else:
                href = "http://127.0.0.1:5000/login"

        return [href]


    @dashapp.callback([],
    [Input('registertournament-button', 'n_clicks')],
    [State('selection-inscription-tournoi', 'value')])
    def inscription_tournoi(n_clicks, nom_tournoi):

        username = str(current_user.get_id())

        df_tournois = get_tournois()
        df_participants = get_participants()

        new_participant = {"tournoi":str(nom_tournoi), "participant":str(username)}
        # Ajout des données dans la bdd redis
        redis_client.hmset('participant ' + str(len(df_participants)+1), new_participant)

        redis_client.save()

        df_participants = get_participants()
"""
    @dashapp.callback([],
    [Input('registertournament-button', 'n_clicks')],
    [State('selection-inscription-tournoi', 'value')])
    def inscription_tournoi(n_clicks, nom_tournoi):

        if n_clicks == None:
            pass

        else:
            if current_user.is_authenticated == False:
                pass
            else:
                username = str(current_user.get_id())

            df_tournois = get_tournois()
            df_participants = get_participants()

            df_participation = df_participants[df_participants.participant==username]

            for participation in df_participation.tournoi:
                already_registered = False
                if participation == nom_tournoi:
                    already_registered = True

            if already_registered == False:

                new_participant = {"tournoi":str(nom_tournoi), "participant":str(username)}
                # Ajout des données dans la bdd redis
                redis_client.hmset('participant ' + str(len(df_participants)+1), new_participant)

                redis_client.save()

                df_participants = get_participants()
"""
