import plotly.express as px
import plotly.graph_objects as go
import dash
from dash.dependencies import *
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.data import *

import base64

# Couleurs utilisées dans le Dashboard
colors = {
    'background1': '#20B5C8',
    'background2': '#D4E6F1',
    'background3': '#717677',
    'text': 'white'
}

def create_tournament_card(nom_tournoi):

    df_tournois = get_tournois()

    type = df_tournois.type[df_tournois.nom==nom_tournoi]
    host = df_tournois.host[df_tournois.nom==nom_tournoi]
    jeu = df_tournois.jeu[df_tournois.nom==nom_tournoi]
    date = df_tournois.date[df_tournois.nom==nom_tournoi]
    nb_participants = str(len(df_participants[df_participants.tournoi==nom_tournoi]))
    max_participants = df_tournois.max_participants[df_tournois.nom==nom_tournoi]

    places_disponibles = nb_participants + '/' + max_participants

    #type pour l'image et la couleur de la card
    if any(type == "video"):
        img = "app/assets/img/video game.jpg"
        encoded_img = base64.b64encode(open(img, 'rb').read())
        color = "primary"
    elif any(type == "board"):
        img = "app/assets/img/board game.jpg"
        encoded_img = base64.b64encode(open(img, 'rb').read())
        color = "success"
    else:
        img = "app/assets/img/other game.jpg"
        encoded_img = base64.b64encode(open(img, 'rb').read())
        color = "warning"

    card_content = [
        dbc.CardImg(src='data:image/png;base64,{}'.format(encoded_img.decode()), top=True, alt=type, style={'align':'center','width':'300px','height':'200px'}),
        dbc.CardBody(
            [
                dbc.Row([
                    html.H3(nom_tournoi, className="card-title"),
                ], no_gutters=True, justify='around', align = 'center'),
                html.Br(),
                dbc.Row([
                    html.H5("Jeu : " + jeu, className="card-title"),
                ], no_gutters=True, justify='around', align = 'center'),
                html.Br(),
                dbc.Row([
                html.P("Organisateur du tournoi : " + host, className="card-text"),
                ], no_gutters=True, justify='around', align = 'center'),
                html.Br(),
            ], style={'width':'300px'}
        ),
        dbc.CardFooter(dbc.Row([
            html.P("Nombre d'inscrits au tournoi : " + places_disponibles, className="card-text"),
        ], no_gutters=True, justify='around', align = 'center')),
    ]

    card = dbc.Card(card_content, color=color, outline=True, style={'width':'300px', 'height':'450px', "margin-bottom": "50px", "margin-left": "20px", "margin-right": "20px"})

    return card
