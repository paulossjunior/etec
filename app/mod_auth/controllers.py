# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.mod_auth.forms import LoginForm


# Import module models (i.e. User)
from app.mod_auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route('/', methods=['GET'])
def home():
	return render_template("auth/signin.html")

@mod_auth.route('/add/', methods=['POST'])
def add():

	nome = request.form['nome']
	senha = request.form['password']
	email = request.form['email']
	sexu = request.form['sexu']
	
	user = User(nome,email,senha,sexu)
	db.session.add(user)
	db.session.commit()
	
	usuarios = User.query.all()

	return render_template("auth/report.html", usuarios=usuarios)
