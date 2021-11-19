
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
