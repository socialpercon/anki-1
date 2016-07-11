# coding: utf-8
import flask
from flask.ext.cors import CORS
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

__VIEWS__ = ['card']

app = flask.Flask('anki')

CORS(app)
