import dash
from dash.dependencies import *
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.figures import *
from app.data import *

from data.redis import *

from flask_login import login_user, logout_user, current_user

# Callbacks pour rafraichir et mettre à jour les différentes figures et composants
def register_callbacks(dashapp):
    @dashapp.callback([Output('log-button-msg', 'data'), Output('log-button-color', 'data'), Output('login-status', 'data')],
    [Input('go-home-button', 'n_clicks')])
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

    @dashapp.callback([Output('titre-page-profil', 'children'), Output("profile-redirect", "children")],
    [Input('go-log-button', 'n_clicks')])
    def update_profile_title(n_clicks):

        redirect = []

        if current_user.is_authenticated == False:
            redirect = dcc.Location(pathname="/login", id="redirecttologinpage")
            name = ""
        else:
            name = str(current_user.get_id()) + " - "
        return [name + "Mes tournois"], redirect

    @dashapp.callback(Output('liste-tournois-hosted', 'children'),
        [Input('go-profile-button', 'n_clicks')])
    def update_tournois_hosted(n_clicks):

        if current_user.is_authenticated == True:
            host = str(current_user.get_id())
        else:
            host = ""

        df_tournois = get_tournois()

        tournois_hosted = df_tournois[df_tournois.host==host]

        # La liste à afficher
        children = [
        ]

        for i in range(len(tournois_hosted)):
            card = create_tournament_card(tournois_hosted.nom[i])
            children.append(card)

        return children

    @dashapp.callback(Output('liste-tournois-participated', 'children'),
        [Input('go-profile-button', 'n_clicks')])
    def update_tournois_participated(n_clicks):

        if current_user.is_authenticated == True:
            participant = str(current_user.get_id())
        else:
            participant = ""

        df_tournois = get_tournois()
        df_participants = get_participants()

        df_participation = df_participants[df_participants.participant==participant]

        frames = []
        for nom_tournoi in df_participation.tournoi:
            frames.append(df_tournois[df_tournois.nom==nom_tournoi])

        if frames==[]:
            tournois_participated = []
        else:
            tournois_participated = pd.concat(frames)

        # La liste à afficher
        children = [
        ]

        for i in range(len(tournois_participated)):
            card = create_tournament_card(tournois_participated.nom[i])
            children.append(card)

        return children
