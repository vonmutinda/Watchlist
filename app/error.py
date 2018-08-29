from flask import render_template
from app import app

@app.errorhandler(404)
def foo_oo_foo(error):

    return render_template('fourOfour.html'),404