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

#20B5C8

# Disposition des figures et autres composants
layout = html.Div(style={'backgroundColor': colors['background1'], 'height':'100vh'}, children=[

    # navbar
    html.Div([navbar]),

    dbc.Row([

        dbc.Col([
            html.H2(
                id='text-before-button',
                children="Page de gestion des tournois",
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

    html.H5("S'inscrire à un tournoi", style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    dbc.Row([
        dbc.Alert(
                "Action réussie !",
                id="alert-register-tournament",
                dismissable=True,
                is_open=False,
                fade=False,
                color = "success",
            ),
    ], no_gutters=True, justify='around', align = 'center', style={'backgroundColor':colors['background1']}),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    dbc.Row([
        dbc.Col([
            html.Div(children=[
                # Menu déroulant pour le choix des tournois
                dcc.Dropdown(
                id='selection-inscription-tournoi',
                placeholder='Sélectionnez un tournoi',
                options=liste_tournois,
                multi=False,
                value=[{"label":"Smash Tournament", "value":"Smash Tournament"}],
                style={'display': 'inline-block','width':'100%', 'border':'solid', 'border-radius': '2px', 'padding': '4px'}
                ),
            ]),
        ], width=6, style={'margin-right':'40px'}),
        dbc.Col([
            dbc.Button("S'inscrire au tournoi",id="registertournament-button", color="primary", className="mr-1", style={'fontWeight': 'bold'}),
        ], width=2),
    ], no_gutters=True, justify='center'),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    html.H5("Se désinscrire d'un tournoi", style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    dbc.Row([
        dbc.Alert(
                "Action réussie !",
                id="alert-unsubscribe-tournament",
                dismissable=True,
                is_open=False,
                fade=False,
                color = "success",
            ),
    ], no_gutters=True, justify='around', align = 'center', style={'backgroundColor':colors['background1']}),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    dbc.Row([
        dbc.Col([
            html.Div(children=[
                # Menu déroulant pour le choix des tournois
                dcc.Dropdown(
                id='selection-desinscription-tournoi',
                placeholder='Sélectionnez un tournoi',
                options=liste_tournois,
                multi=False,
                value=[],
                style={'display': 'inline-block','width':'100%', 'border':'solid', 'border-radius': '2px', 'padding': '4px'}
                ),
            ]),
        ], width=6, style={'margin-right':'40px'}),
        dbc.Col([
            dbc.Button("Se désinscrire du tournoi",id="unsubscribetournament-button", color="warning", className="mr-1", style={'fontWeight': 'bold'}),
        ], width=2),
    ], no_gutters=True, justify='center'),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    html.H5("Ajouter un tournoi", style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    dbc.Row([
        dbc.Alert(
                "Action réussie !",
                id="alert-add-tournament",
                dismissable=True,
                is_open=False,
                fade=False,
                color = "success",
            ),
    ], no_gutters=True, justify='around', align = 'center', style={'backgroundColor':colors['background1']}),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    dbc.Row([
        dbc.Col([
            html.Div(children=[
                # Menu déroulant pour le choix des tournois
                dcc.Dropdown(
                id='selection-add-tournoi',
                placeholder='Sélectionnez un tournoi',
                options=liste_tournois,
                multi=False,
                value=[],
                style={'display': 'inline-block','width':'100%', 'border':'solid', 'border-radius': '2px', 'padding': '4px'}
                ),
            ]),
        ], width=6, style={'margin-right':'40px'}),
        dbc.Col([
            dbc.Button("Créer un tournoi",id="addtournament-button", color="success", className="mr-1", style={'fontWeight': 'bold'}),
        ], width=2),
    ], no_gutters=True, justify='center'),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    html.Hr(),

    html.Div(id="register-redirect"),

    # Données de la session
    log_button_msg,
    log_button_color,
    login_status,
    register_success,

])
