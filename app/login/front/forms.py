import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

login_name_input = dbc.Row(
    [
        dbc.Label("Pseudonyme", html_for="login-name-input", width=6),
        dbc.Col(children=[

            html.Div([
            dbc.Input(
                type="text", id="login-name-input"
            ),
            ]),
            ],
            width=12,
        ),
    ],
    className="mb-3", align = 'center',
)

login_password_input = dbc.Row(
    [
        dbc.Label("Mot de passe", html_for="login-password-input", width=6),
        dbc.Col(children=[

            html.Div([
            dbc.Input(
                type="password",
                id="login-password-input",
            ),
            ]),
            ],
            width=12,
        ),
    ],
    className="mb-3", align = 'center',
)

login_form = dbc.Form(
    [login_name_input,
    login_password_input,
    dbc.Row([
        dbc.Button("Connexion",id="login-button", color="success", className="mr-3", style={'fontWeight': 'bold'}),
    ], no_gutters=True, justify='around', align = 'center'),
    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),
    dbc.Row([
        dbc.Button("Créer un compte",id="go-register-button", href="http://127.0.0.1:5000/register", color="link", className="mr-3", style={'fontWeight': 'bold'}),
    ], no_gutters=True, justify='around', align = 'center'),
    ], style={'border':'solid', 'border-radius': '8px', 'padding': '5px'}
)
