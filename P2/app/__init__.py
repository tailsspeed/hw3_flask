from flask import Flask

myobj = Flask(__name__)

#.from_mapping holds config settings--key to prevent cross-site attacks
myobj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess'
)

from app import routes
