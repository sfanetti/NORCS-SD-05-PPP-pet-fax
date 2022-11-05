from flask import ( Blueprint, render_template, request ) 

bp = Blueprint('fact', __name__, url_prefix="/facts")


@bp.route('/new', methods=('GET', 'POST'))
def new():
    if request.method == "GET":
        return render_template('facts/new.html')
    if request.method == "POST":
        for key, value in request.form.items():
            print(f"Setting value of '{key}' to '{value}'")
        return render_template('facts/new.html')