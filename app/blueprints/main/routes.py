from flask import render_template
from .import bp as main

@main.route('/', methods=['GET'])
def index():
    context = {}
    return render_template('main/index.html', **context)

@main.route('/about', methods=['GET'])
def about():
    context = {}
    return render_template('main/about.html', **context)

@main.route('/contact', methods=['GET'])
def contact():
    context = {}
    return render_template('main/contact.html', **context)

@main.route('/portfolio', methods=['GET'])
def portfolio():
    context = {}
    return render_template('main/portfolio.html', **context)

@main.route('/other', methods=['GET'])
def other():
    context = {}
    return render_template('main/other.html', **context)

