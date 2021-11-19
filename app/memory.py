import dash
from dash.dependencies import *

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate


register_success = dcc.Store(id='register-success', storage_type='session', data=0)

login_status = dcc.Store(id='login-status', storage_type='session')

log_button_msg = dcc.Store(id='log-button-msg', storage_type='session', data="Connexion")

log_button_color = dcc.Store(id='log-button-color', storage_type='session', data="success")
