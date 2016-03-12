from flask import *
from requests import *

main = Blueprint('main', __name__)
api = Blueprint('api', __name__)

@main.route('/')
def main_route():

	return 'Hello World!'
	# return render_template("index.html", **options)

@api.route('/api', methods=['GET'])
def api_route():

	return ('Welcome to the API Index')


@api.route('/api/color', methods=['POST'])
def api_color_route():

	body = request.get_json()

	if not 'hue' in body or not 'deviceID' in body:
		return 'You are missing "hue" or "deviceID" fields', 422

	hue = body['hue']
	deviceID = body['deviceID']

	if 'room' in body:
		room = body['room']
	else:
		room = 0

	hue = int(hue * 65535)
	room = room + 1

	requests.put('192.168.86.123/api/169b766c36914e2f2dd44e443bcbf1c7/lights/' + room + '/state', data={"bri": 254, "hue": hue, "sat": 254})

	return 'Success!'

# @main.app_errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404
