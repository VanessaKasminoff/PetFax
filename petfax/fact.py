from flask import (Blueprint, render_template, request, redirect)
from .models import model

bp = Blueprint('fact', __name__, url_prefix='/facts')

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            submitter = request.form['submitter']
            fact = request.form['fact']
            new_fact = model.Fact(submitter=submitter, fact=fact)
            model.db.session.add(new_fact)
            model.db.session.commit()

            return redirect('/facts')
        except Exception as error:
            print(error)

    results = model.Fact.query.all()
    return render_template('fact.html', facts=results)


@bp.get('/new')
def new():
    return render_template('fact_new.html')