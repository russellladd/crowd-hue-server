from flask import *

main = Blueprint('main', __name__)
api = Blueprint('api', __name__)

@main.route('/')
def main_route():

	return 'Hello World!'
	# return render_template("index.html", **options)

@api.route('/api', methods=['GET'])
def api_route():

	return ('Welcome to the API Index')


@api.route('/api/color', methods=['GET', 'POST'])
def api_color_route():
	return ('Welcome to the API Color')

# @main.app_errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404
