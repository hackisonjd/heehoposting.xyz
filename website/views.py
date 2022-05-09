'''
Valid views (or webpages) for Flask website.
'''
import glob
import os.path
from flask import Blueprint, render_template
import markdown


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
    with open('website/static/index.txt', 'r') as f:
        text = f.read()
    text = markdown.markdown(text)
    return render_template('index.html', navbar=navbar, text=text)

@bp.route('/about')
def about():
    '''
    Information about me, this is the portfolio bit.
    '''

    with open('website/static/bio.txt', 'r') as f:
        bio = f.read()
    bio = markdown.markdown(bio)
    print(bio)

    return render_template('about.html', navbar=navbar, bio=bio)

@bp.route('/contact')
def contact():
    '''
    Displays contact information on how to reach me directly.
    '''
    with open('website/static/contact.txt', 'r') as f:
        contact = f.read()
    contact = markdown.markdown(contact)
    return render_template('contact.html', navbar=navbar, contact=contact)

@bp.route('/links')
def links():
    '''
    Displays useful links that helped me make this website in addition to other things.
    '''
    with open('website/static/links.txt', 'r') as f:
        links = f.read()
    links = markdown.markdown(links)
    return render_template('links.html', navbar=navbar, links=links)
