import dash_bootstrap_components as dbc
import dash_html_components as html

import base64

# Couleurs utilisées dans le Dashboard
colors = {
    'background1': '#20B5C8',
    'background2': '#D4E6F1',
    'background3': '#717677',
    'text': 'white'
}

logo = "app/assets/img/logo_ESIEE_blanc.png"

encoded_image = base64.b64encode(open(logo, 'rb').read())


items=[
        dbc.DropdownMenuItem("Moritz Martin",href="https://www.linkedin.com/in/martin-moritz",external_link=True),
        dbc.DropdownMenuItem("Rogissart Vincent",href="https://www.linkedin.com/in/vincent-rogissart-20743a1aa/",external_link=True),
        ]

navbar = dbc.Navbar(
    [
        dbc.Col([
            html.A(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), height="50px"), href="https://www.esiee.fr/"),
        ], width=1),

        dbc.Col([
            dbc.Button("Accueil",id="go-home-button", color="primary", className="mr-1", href="http://127.0.0.1:5000/", style={'fontWeight': 'bold'}),
            dbc.Button("Mon Profil",id="go-profile-button", color="info", className="mr-1", href="http://127.0.0.1:5000/profile", style={'fontWeight': 'bold'}),
            dbc.Button("Connexion",id="go-log-button", color="success", className="mr-1", href="http://127.0.0.1:5000/login", style={'fontWeight': 'bold'}),
        ], width=3),
        dbc.Col([
            html.H1(
                children='Projet ESIEE Paris : Gestion de Tournois',
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontWeight': 'bold',
                    'fontSize':22
                }
            ),
        ], width=5),
        dbc.DropdownMenu(items,label="Auteurs",color="info",className="ml-auto p-2 bd-highlight",in_navbar=True, direction="left", toggle_style={'fontWeight': 'bold'}),
    ],
    color="dark",
    dark=True,
)
