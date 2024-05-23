#  DEPENDENCIES
from flask import (Flask, render_template)
from flask_migrate import Migrate
from dotenv import (load_dotenv, dotenv_values)
import os
import json

load_dotenv()

pets = json.load(open('pets.json', 'r', encoding='utf-8'))

def create_app(): 
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('PG_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    from .models import model
    model.db.init_app(app)
    migrate = Migrate(app, model.db)

    @app.route('/')
    def hello(): 
        return render_template('home.html', pets=pets)

    from . import (pet, fact)
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)

    return app