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

contents = dict_files()

@bp.route('/')
def index():
    '''
    Homepage for the website.
    '''
    return render_template('index.html', contents=contents)

@bp.route('/about')
def about():
    '''
    Information about me, this is the portfolio bit.
    '''
    filename = os.path.join
    with open('website/static/bio.txt', 'r') as f:
        bio = f.read()
    bio = markdown.markdown(bio)
    print(bio)

    return render_template('about.html', contents=contents, bio=bio)

@bp.route('/contact')
def contact():
    '''
    Displays contact information on how to reach me directly.
    '''
    return render_template('contact.html', contents=contents)
