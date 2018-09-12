import logging.config
import gevent.wsgi
import werkzeug.serving
import config
import os
import datetime

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security
from flask_socketio import SocketIO

from api.users.users import ns as users_namespace
from api.evaluators.evaluator import nse as evaluator_namespace
from api.courses.courses import ns as courses_namespace
from api.groups.groups import ns as groups_namespace
from api.topics.topics import ns as topics_namespace
from api.languages.languages import ns as languages_namespace
from api.submissions.submissions import ns as submissions_namespace
from api.problems.problems import ns as problems_namespace
from api.assignments.assignments import ns as assignments_namespace
from api.teams.teams import ns as team_namespace
from api.statistic.statistic import ns as statistics_namespace
from api.forums.forum import ns as forum_namespace
from api.comments.comment import ns as comment_namespace
from api.contests.contests import ns as contests_namespace
from api.messages.message import ns as messages_namespace
from api.recommendation.recommendation import ns as recomendation_namespace

from api.restplus import api
from models import db, User

from sockets import ChatNamespace as chat
from sockets import ContestNamespace as contest

from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object(config.ProductionConfig)
# app.config.from_object(os.environ['APP_SETTINGS'])

security = Security(app)
socketio = SocketIO(app)

CORS(app)

@app.route('/')
def hello():
    return "Hello World!"

def create_db(db_instancep):
    db_instance.init_app(app)
    db_instance.create_all()


def initialize_app(flask_app):
    # configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(users_namespace)
    api.add_namespace(evaluator_namespace)
    api.add_namespace(courses_namespace)
    api.add_namespace(groups_namespace)
    api.add_namespace(topics_namespace)
    api.add_namespace(languages_namespace)
    api.add_namespace(submissions_namespace)
    api.add_namespace(problems_namespace)
    api.add_namespace(assignments_namespace)
    api.add_namespace(team_namespace)
    api.add_namespace(statistics_namespace)
    api.add_namespace(forum_namespace)
    api.add_namespace(comment_namespace)
    api.add_namespace(messages_namespace)
    api.add_namespace(recomendation_namespace)
    flask_app.register_blueprint(blueprint)

    socketio.on_namespace(chat.ChatNamespace('/chat'))
    socketio.on_namespace(contest.ContestNamespace('/contest'))
    

def main():
    initialize_app(app)
    logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logging.info("New session ––– " + str(datetime.datetime.now()) + " ––– New session")
    # gevent_server = gevent.wsgi.WSGIServer(('', 5000), app)
    # gevent_server.serve_forever()
    socketio.run(app, port=5000, debug=True)

if __name__ == '__main__':
    main()
