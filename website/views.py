'''
Valid views (or webpages) for Flask website.
'''
import glob
import os.path
from flask import Blueprint, render_template, request, redirect, url_for
import markdown
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
from .models import User


bp = Blueprint('views', __name__)

def dict_files():
    '''
    Reads through all files in the templates directory and stores them in a dictionary.
    '''
    files = {'Home': 'views.index'}
    for file in glob.glob('website/templates/*.html'):
        if 'website/templates/index.html' not in file and 'website/templates/base.html' not in file:
            # return only the capitalized version of the basename of the path (w/o extension)
            file_key = (os.path.splitext(os.path.basename(file))[0]).capitalize()
            files[file_key] = ('views.' + file_key.lower())
    return files

navbar = dict_files()

@bp.route('/')
def index():
    '''
    Homepage for the website.
    '''
    with open('website/static/index.txt', 'r', encoding="utf-8") as file:
        text = file.read()
    text = markdown.markdown(text)
    return render_template('index.html', navbar=navbar, user=current_user,  text=text)

@bp.route('/about')
def about():
    '''
    Information about me, this is the portfolio bit.
    '''

    with open('website/static/bio.txt', 'r', encoding="utf-8") as file:
        bio = file.read()
    bio = markdown.markdown(bio)
    print(bio)

    return render_template('about.html', navbar=navbar, bio=bio, user=current_user)

@bp.route('/contact')
def contact():
    '''
    Displays contact information on how to reach me directly.
    '''
    with open('website/static/contact.txt', 'r', encoding="utf-8") as file:
        con = file.read()
    con = markdown.markdown(contact)
    return render_template('contact.html', navbar=navbar, contact=con, user=current_user)

@bp.route('/links')
def links():
    '''
    Displays useful links that helped me make this website in addition to other things.
    '''
    with open('website/static/links.txt', 'r', encoding="utf-8") as file:
        link = file.read()
    link = markdown.markdown(link)
    return render_template('links.html', navbar=navbar, links=link, user=current_user)

@bp.route('/login', methods=['POST', 'GET'])
def login():
    '''
    This method handles the login page for accounts, which is just my personal account for now.
    '''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.mastermind'))

    return render_template('/admin/login.html', user=current_user)

@bp.route('/mastermind', methods=['POST', 'GET'])
@login_required
def mastermind():
    '''
    Information for my login page that definitely isn't going to get broken into nosiree.
    '''
    return render_template('/admin/mastermind.html', user=current_user, navbar=navbar)

@bp.route('/logout')
@login_required
def logout():
    '''
    Logout protocol, is only used if the mastermind is logged in.
    '''
    logout_user()
    return redirect(url_for('views.index'))