import os

from flask import Flask

def create_app(test_config=None):
    # creates the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path, 'heehoposting.sqlite'),       
    )

    if test_config is None:
        # load instance config when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load test config when passed in
        app.config.from_mapping(test_config)

    # ensure that the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, world'

    return app