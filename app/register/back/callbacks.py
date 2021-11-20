import dash
from dash.dependencies import *
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.figures import *
from app.register.front.forms import *
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

    @dashapp.callback(
    [Output("register-name-input", "valid"), Output("register-name-input", "invalid")],
    [Input("register-name-input", "value")])
    def check_name_validity(name):

        df_users = get_users()

        if name == None or name == '':
            return False, False
        else:
            is_name_valid = True
            i=0
            name_already_exists = False
            while i<len(df_users) and name_already_exists==False:
                if df_users['nom'][i]==name:
                    name_already_exists = True
                    is_name_valid = False
                else:
                    i=i+1
            return is_name_valid, not is_name_valid

    @dashapp.callback(
    [Output("register-password-input", "valid"), Output("register-password-input", "invalid")],
    [Input("register-password-input", "value")])
    def check_password_validity(password):
        if password == None or password == '':
            return False, False
        else:
            is_password_valid = False
            if len(password)>=6:
                is_password_valid = True
            return is_password_valid, not is_password_valid

    @dashapp.callback(
    [Output("confirm-password-input", "valid"), Output("confirm-password-input", "invalid")],
    [Input("confirm-password-input", "value"), Input("register-password-input", "value")])
    def check_confirm_password_validity(password, confirm_password):
        if confirm_password == None or confirm_password == '':
            return False, False
        else:
            is_confirm_password_valid = False
            if password == confirm_password:
                is_confirm_password_valid = True
            return is_confirm_password_valid, not is_confirm_password_valid

    @dashapp.callback([Output("alert-register", "children"), Output("alert-register", "color"), Output("alert-register", "is_open"), Output("register-redirect", "children"), Output("register-success", "data")],
    [Input("register-button", "n_clicks")],
    [State("register-name-input", "value"), State("register-password-input", "value"), State("confirm-password-input", "value"), State("register-name-input", "valid"), State("register-password-input", "valid"), State("confirm-password-input", "valid"), State("alert-register", "is_open"), State("register-success", "data")])
    def submit(n_clicks, name, password, confirm_password, name_valid, password_valid, confirm_password_valid, alert_is_open, data):

        alert_children = "Formulaire incomplet"
        alert_color = "warning"

        redirect = []

        data = 0

        if n_clicks == None:
            alert_is_open = False

        else:

            if alert_is_open == False:
                alert_is_open = True

            if name == None or name=='':
                alert_children = "Formulaire incomplet"
                alert_color = "warning"
            elif password == None or password=='':
                alert_children = "Formulaire incomplet"
                alert_color = "warning"
            elif confirm_password == None or confirm_password=='':
                alert_children = "Formulaire incomplet"
                alert_color = "warning"
            elif name_valid==False:
                alert_children = "Formulaire invalide"
                alert_color = "danger"
            elif password_valid==False:
                alert_children = "Formulaire invalide"
                alert_color = "danger"
            elif confirm_password_valid==False:
                alert_children = "Formulaire invalide"
                alert_color = "danger"

            else:
                # Création du compte
                df_users = get_users()
                new_user = {"nom":str(name), "mdp":str(password)}

                # Ajout des données dans la bdd redis
                redis_client.hmset('user ' + str(len(df_users)+1), new_user)

                redis_client.save()

                """
                existing_user = User.query.filter_by(name=name).first()
                if existing_user is None:
                    user = User(name=name, password=generate_password_hash(password, method='sha256'))
                    db.session.add(user)
                    db.session.commit()
                """
                # actualisation de df_users
                df_users = get_users()

                alert_children = "Inscription réussie !"
                alert_color = "success"

                redirect = dcc.Location(pathname="/login", id="redirecttologinpage")

                data = 1

        return [alert_children], alert_color, alert_is_open, redirect, data
