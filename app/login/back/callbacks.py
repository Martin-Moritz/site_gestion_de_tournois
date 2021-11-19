import dash
from dash.dependencies import *
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.figures import *
from app.login.front.forms import *
from app.data import *

from data.redis import *

from flask_login import login_user, logout_user, current_user
from app.models import User

# Callbacks pour rafraichir et mettre à jour les différentes figures et composants
def register_callbacks(dashapp):
    @dashapp.callback([Output('log-button-msg', 'data'), Output('log-button-color', 'data'), Output('login-status', 'data')],
    [Input('user-status-div', 'children')])
    def update_data_log_button(children):
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

    @dashapp.callback(
    [Output("alert-login", "children"), Output("alert-login", "color"), Output("alert-login", "is_open"), Output("register-success", "data")],
    [Input('login-button', 'n_clicks')],
    [State('login-name-input', 'value'), State('login-password-input', 'value'), State('alert-login', 'is_open'), State("register-success", "data")])
    def login(n_clicks, username, password, alert_is_open, data):

        alert_children = "Identifiant ou mot de passe incorrect"
        alert_color = "danger"

        if n_clicks==None:
            if data == 1:
                # dans le cas où viens de s'inscrire et d'être redirigé sur la page de connexion
                alert_children = "Inscription réussie !"
                alert_color = "success"
                alert_is_open = True

                data = 0
            else:
                alert_is_open = False

        else:
            df_users = get_users()

            is_username_valid = False
            is_password_valid = False

            #check username if is valid
            index=0
            while index<len(df_users) and is_username_valid==False:
                if df_users['nom'][index]==username:
                    is_username_valid = True
                else:
                    index=index+1

            if is_username_valid == True:
                #check password if username is valid
                if df_users['mdp'][index]==password:
                        is_password_valid = True

            if is_username_valid==True and is_password_valid == True:
                #if the username and the password are valids : log in the user
                user = User(username)
                login_user(user)

                alert_is_open = False

            else:
                if alert_is_open == False:
                    alert_is_open = True

        return [alert_children], alert_color, alert_is_open, data

    """
    @dashapp.callback([Output('logout-button', 'children')],
    [Input('logout-button', 'n_clicks')])
    def logout(n_clicks):
        if n_clicks==None:
            pass
        else:
            if current_user.is_authenticated:
                logout_user()

        if current_user.is_authenticated == True:
            msg = 'Se déco'
        else:
            msg = 'Déjà déco'

        return [msg]
    """

    @dashapp.callback(
    [Output('user-status-div', 'children')],
    [Input('login-button', 'n_clicks')])
    def login_status(n_clicks):
        ''' callback to display login/logout link in the header '''
        if current_user.is_authenticated:  # If the URL is /logout, then the user is about to be logged out anyways
            return [" "]
        else:
            return [""]


"""
    @dashapp.callback(Output('page-content', 'children'), Output('redirect', 'pathname'),
              [Input('url', 'pathname')])
    def display_page(pathname):
        ''' callback to determine layout to return '''
        # We need to determine two things for everytime the user navigates:
        # Can they access this page? If so, we just return the view
        # Otherwise, if they need to be authenticated first, we need to redirect them to the login page
        # So we have two outputs, the first is which view we'll return
        # The second one is a redirection to another page is needed
        # In most cases, we won't need to redirect. Instead of having to return two variables everytime in the if statement
        # We setup the defaults at the beginning, with redirect to dash.no_update; which simply means, just keep the requested url
        view = None
        url = dash.no_update
        if pathname == '/login':
            view = login
        elif pathname == '/success':
            if current_user.is_authenticated:
                view = success
            else:
                view = failed
        elif pathname == '/logout':
            if current_user.is_authenticated:
                logout_user()
                view = logout
            else:
                view = login
                url = '/login'

        elif pathname == '/page-1':
            view = page_1_layout
        elif pathname == '/page-2':
            if current_user.is_authenticated:
                view = page_2_layout
            else:
                view = 'Redirecting to login...'
                url = '/login'
        else:
            view = index_page
        # You could also return a 404 "URL not found" page here
        return view, url
"""
