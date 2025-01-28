from flask import Blueprint, render_template, request, redirect, url_for

my = Blueprint('main', __name__)


@my.route('/')
def index():
    return render_template('index.html')


@my.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')
