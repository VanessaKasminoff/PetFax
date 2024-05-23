from flask import (Blueprint, render_template, request, redirect)

bp = Blueprint('fact', __name__, url_prefix='/facts')

@bp.get('/')
def index():
    return render_template('fact.html')


@bp.get('/new')
def new():
    return render_template('fact_new.html')


@bp.post('/')
def create():
    print(request.form)
    return redirect('/facts')