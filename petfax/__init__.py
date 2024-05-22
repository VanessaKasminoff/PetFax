from flask import (Flask, render_template) 
import json

pets = json.load(open('pets.json'))

def create_app(): 
    app = Flask(__name__)

    @app.route('/')
    def hello(): 
        return render_template('home.html', pets=pets)

    from . import pet
    app.register_blueprint(pet.bp)

    return app
