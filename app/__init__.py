from flask import Flask,render_template
from flask_login import LoginManager, login_user, logout_user, current_user

# application flask
#app = Flask(__name__) # name est une variable prédéfinie transmise à Flask

from . import dash
from .dash import create_app

from .models import User

login_manager = LoginManager()

app = create_app()

# Application Configuration
app.config.from_object('config.Config')

login_manager.init_app(app)

#login_manager.login_view = '/login'

@login_manager.user_loader
def load_user(username):
    """Check if user is logged-in on every page load."""
    if username is not None:
        return User(username)
    return None
