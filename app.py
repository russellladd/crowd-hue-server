import os

from flask import Flask, render_template

import controllers

# Initialize Flask app with the template folder address
app = Flask(__name__)

app.config['DEBUG'] = True
# Register the controllers
PREFIX = ''

app.register_blueprint(controllers.main, url_prefix=PREFIX)
app.register_blueprint(controllers.api, url_prefix=PREFIX)

# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port, debug=True)
