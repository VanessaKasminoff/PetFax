from flask import (Flask, render_template) 
import json

pets = json.load(open('pets.json'))

def create_app(): 
    app = Flask(__name__)

    @app.route('/')
    def hello(): 
        return render_template('home.html', pets=pets)

    from . import (pet, fact)
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)

    return app
