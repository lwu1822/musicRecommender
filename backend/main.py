import threading
from flask import render_template, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from __init__ import app, db
from model.jokes import initJokes
from model.users import initUsers
from model.players import initPlayers

# Import all your API blueprints
from api.covid import covid_api
from api.joke import joke_api
from api.user import user_api
from api.player import player_api
from api.song import song_api
from projects.projects import app_projects

# Initialize the SQLAlchemy object
db.init_app(app)

# --- ROBUST PREFLIGHT REQUEST HANDLER ---
# This function will run before every request.
@app.before_request
def before_request_handler():
    # Checks if the request method is OPTIONS (a preflight request)
    if request.method == 'OPTIONS':
        # Creates a response with the necessary CORS headers
        response = jsonify({})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

# --- CORS CONFIGURATION FOR ACTUAL REQUESTS ---
# This will handle CORS for all non-preflight requests.
CORS(app, origins=["http://127.0.0.1:4000", "http://localhost:4000", "https://lwu1822.github.io"], supports_credentials=True)

# Register all API blueprints
app.register_blueprint(joke_api)
app.register_blueprint(covid_api)
app.register_blueprint(user_api)
app.register_blueprint(player_api)
app.register_blueprint(app_projects)
app.register_blueprint(song_api)

# --- JWT AND OTHER APP CONFIGURATION ---
app.config['SECRET_KEY'] = 'secretkey'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False # Keep this disabled for now
jwt = JWTManager(app)

# --- Standard Flask Routes ---
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/table/')
def table():
    return render_template("table.html")

@app.before_first_request
def activate_job():
    initJokes()
    initUsers()
    initPlayers()

# --- Main execution point ---
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8086")