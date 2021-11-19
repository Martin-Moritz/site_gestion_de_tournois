import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

register_name_input = dbc.Row(
    [
        dbc.Label("Identifiant", html_for="register-name-input", width=6),
        dbc.Col(children=[

            html.Div([
            dbc.Input(
                type="text", id="register-name-input", placeholder="Entrez un pseudonyme"
            ),
            dbc.FormFeedback(id="register-name-valid", children="Ce pseudonyme est disponible", valid=True),
            dbc.FormFeedback(id="register-name-invalid", children="Ce pseudonyme n'est pas disponible", valid=False),

            ]),
            ],
            width=12,
        ),
    ],
    className="mb-3", align = 'center',
)

register_password_input = dbc.Row(
    [
        dbc.Label("Mot de passe", html_for="register-password-input", width=6),
        dbc.Col(children=[

            html.Div([
            dbc.Input(
                type="password",
                id="register-password-input",
                placeholder="Entrez un mot de passe",
            ),
            dbc.FormFeedback(id="register-password-valid", children="Le mot de passe est valide", valid=True),
            dbc.FormFeedback(id="register-password-invalid", children="Le mot de passe doit contenir au moins 6 caractères", valid=False),

            ]),
            ],
            width=12,
        ),
    ],
    className="mb-3", align = 'center',
)

register_confirm_password_input = dbc.Row(
    [
        dbc.Label("Confirmer le mot de passe", html_for="confirm-password-input", width=6),
        dbc.Col(children=[

            html.Div([
            dbc.Input(
                type="password",
                id="confirm-password-input",
                placeholder="Confirmer votre un mot de passe",
            ),
            dbc.FormFeedback(id="confirm-password-valid", children="Les mots de passe sont identiques", valid=True),
            dbc.FormFeedback(id="confirm-password-invalid", children="Les mots de passe ne sont pas identiques", valid=False),

            ]),
            ],
            width=12,
        ),
    ],
    className="mb-3", align = 'center',
)

register_form = dbc.Form(
    [register_name_input,
    register_password_input,
    register_confirm_password_input,
    dbc.Row([
        dbc.Button("S'inscrire",id="register-button", color="primary", className="mr-3", style={'fontWeight': 'bold'}),
    ], no_gutters=True, justify='around', align = 'center'),
    ], style={'border':'solid', 'border-radius': '8px', 'padding': '5px'}
)
