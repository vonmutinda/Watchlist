from flask import render_template
from . import main

@main.errorhandler(404)
def foo_oo_foo(error):

    return render_template('fourOfour.html'),404