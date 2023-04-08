import os
import json
from flask import Flask, jsonify, render_template, request, g
from flask_cors import CORS


""" initialzie objects """


def create_app(config_class):

    """ initialize flask app """
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)
    
    
    """ health check route """
    @app.route("/")
    def home():
        return jsonify({"message": f'Hello from "{app.config["APP_ENV"]}"'})


    """ register routes """
    from app.utilities.errors import errors
    from app.routes.home import home_bp
    from app.routes.auth import auth_bp 

    app.register_blueprint(errors)
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)


    """ context method: before_request"""
    @app.before_request
    def before_request():
        ### load databae
        if os.path.exists(app.config["MYDB"]):
            try:
                with open(app.config["MYDB"], "r") as f:
                    g.mydb = json.load(f)
            except Exception as e:
                print(e)
                g.mydb = {"users": []}
        else:
            g.mydb = {"users": []}


    """ context method: after_request"""
    @app.after_request
    def after_request(response):
        ### save database
        with open(app.config["MYDB"], "w") as f:
            f.write(json.dumps(g.mydb, indent=4)) 
        
        ### return response
        return response
    
    
    """ context method:  after app context is teardown"""
    @app.teardown_appcontext
    def teardown_app_context(exception):
        pass


    """ return app """
    return app