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
                children="Page d'accueil",
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
        dbc.Button("Aller à la page de gestion des tournois",id="go-registertournament-button", color="secondary", className="mr-1", href="http://127.0.0.1:5000/tournament", style={'fontWeight': 'bold'}),
    ], no_gutters=True, justify='around', align = 'center'),

    html.Hr(),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    dbc.Row(id='liste-tournois', children=[
    # Ici est affichée la liste des tournois disponibles
    ], no_gutters=True, justify='around', align = 'center', style={'backgroundColor':colors['background1']}),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    html.Hr(),

    # Données de la session
    log_button_msg,
    log_button_color,
    login_status,
    register_success,

])
