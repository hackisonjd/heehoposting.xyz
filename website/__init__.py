from flask import Flask

def create_app():

    from website.views import bp
    app = Flask(__name__)

    app.register_blueprint(bp, url_prefix="/")
    return app