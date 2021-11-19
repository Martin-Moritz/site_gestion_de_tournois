import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.figures import *
from app.navbar import *

from app.data import *

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
                children="Page de profil",
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

    html.H2(
        id='titre-page-profil',
        children='Mes tournois',
        style={
            'textAlign': 'center',
            'fontWeight': 'bold',
            'fontSize':20
        }
    ),

    html.Hr(),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    dbc.Row([
        dbc.Col([], width=2, align='center'),
        dbc.Col([
            html.H3(
                children="Les tournois que j'ai créés :",
                style={
                    'textAlign': 'left',
                    'fontWeight': 'bold',
                    'fontSize':18,
                    'margin-left':'20px'
                }
            ),
        ], width=5),
        dbc.Col([
            html.H3(
                children="Les tournois auxquels je participe :",
                style={
                    'textAlign': 'left',
                    'fontWeight': 'bold',
                    'fontSize':18,
                    'margin-left':'20px'
                }
            ),
        ], width=5),
        dbc.Col([], width=2, align='center'),
    ], no_gutters=True, justify='around'),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    dbc.Row([
        dbc.Col([], width=2, align='center'),
        dbc.Col([
            html.Div(id='liste-tournois-hosted', children=[
            # Ici s'affichera la liste des tournois créés par l'utilisateur
            ]),
            ], width=5),

        dbc.Col([
            html.Div(id='liste-tournois-participated', children=[
            # Ici s'affichera la liste des tournois auxquels l'utilisateur participe
            ]),
            ], width=5),
        dbc.Col([], width=2, align='center'),

    ], no_gutters=True, justify='around', style={'backgroundColor':colors['background1']}),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    html.Hr(),

    html.Div(id="profile-redirect"),

    # Données de la session
    log_button_msg,
    log_button_color,
    login_status,
    register_success,

])
