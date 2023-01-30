from flask import Blueprint, render_template, redirect, url_for

route = Blueprint('route', __name__, url_prefix='/')

@route.route('/')
def index():
    return redirect(url_for('route.osg_ge'))

@route.route('/osg_ge', methods=['GET'])
def osg_ge():
    return render_template('pages/osg_ge.html')