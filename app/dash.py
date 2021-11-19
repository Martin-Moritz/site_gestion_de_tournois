import flask
from flask import Flask,render_template
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from flask import Blueprint

# Style de page utilisé pour le dashboard -> 'dbc.themes.BOOTSTRAP' permet d'utiliser les dash_bootstrap_components
external_stylesheets = [dbc.themes.BOOTSTRAP]

server_bp = Blueprint('main',__name__)

def create_app():
    server = Flask(__name__)

    from app.home.front.layout import layout as layout1
    from app.home.back.callbacks import register_callbacks as register_callbacks1
    register_dashapp(server, 'Home','',layout1, register_callbacks1)

    from app.login.front.layout import layout as layout2
    from app.login.back.callbacks import register_callbacks as register_callbacks2
    register_dashapp(server, 'Login', '/login', layout2, register_callbacks2)

    from app.register.front.layout import layout as layout3
    from app.register.back.callbacks import register_callbacks as register_callbacks3
    register_dashapp(server, 'Register', '/register', layout3, register_callbacks3)

    from app.profile.front.layout import layout as layout4
    from app.profile.back.callbacks import register_callbacks as register_callbacks4
    register_dashapp(server, 'Profile', '/profile', layout4, register_callbacks4)

    from app.tournament.front.layout import layout as layout5
    from app.tournament.back.callbacks import register_callbacks as register_callbacks5
    register_dashapp(server, 'Register Tournament', '/tournament', layout5, register_callbacks5)

    register_blueprints(server)

    return server

def register_dashapp(app, title, base_pathname, layout, register_callbacks_fun):
    # meta pour la réactivité de la page
    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    my_dashapp = dash.Dash(__name__,
                           server=app,
                           url_base_pathname=f'{base_pathname}/',
                           meta_tags=[meta_viewport],
                           external_stylesheets=external_stylesheets
                           )

    with app.app_context():
        my_dashapp.title = title
        my_dashapp.layout = layout
        register_callbacks_fun(my_dashapp)

def register_blueprints(server):
    server.register_blueprint(server_bp)
