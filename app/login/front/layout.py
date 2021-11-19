import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.figures import *
from app.navbar import *

from app.data import *

from .forms import *

from app.memory import *

# Couleurs utilisées dans le Dashboard
colors = {
    'background1': 'white',
    'background2': '#D4E6F1',
    'background3': '#91675E',
    'text': 'white'
}

# Disposition des figures et autres composants
layout = html.Div(style={'backgroundColor': colors['background1']}, children=[

    # navbar
    html.Div([navbar]),

    dbc.Row([

        dbc.Col([
            html.H2(
                id='text-before-button',
                children='Page de connexion',
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontWeight': 'bold',
                    'fontSize':20
                }
            ),
        ], width=3),

    ], no_gutters=True, justify='around', align = 'center', style={'height':'70px', 'backgroundColor':colors['background3']}),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    dbc.Row([
        dbc.Alert(
                "Identifiant ou mot de passe incorrect",
                id="alert-login",
                dismissable=True,
                is_open=False,
                fade=False,
                color = "danger",
            ),
    ], no_gutters=True, justify='around', align = 'center', style={'backgroundColor':colors['background1']}),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    dbc.Row([
        login_form
    ], no_gutters=True, justify='around', align = 'center', style={'backgroundColor':colors['background1']}),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    html.Hr(),

    dbc.Button("Déjà Déco",id="logout-button", color="warning", className="mr-3", style={'fontWeight': 'bold'}),

    dcc.Location(id='url-login', refresh=False),
    dcc.Location(id='redirect-login', refresh=True),
    html.Div(id='user-status-div'),
    html.Br(),
    html.Br(),
    html.Div(id='page-content'),

    # Données de la session
    log_button_msg,
    log_button_color,
    login_status,
    register_success,

])
