# -*- coding: utf-8 -*-
import json
from anki import Collection
from anki.exporting import Exporter
from anki_tool.rest import *

col = None
PATH = "/home/social/Anki/luxerypro/collection.anki2"


def get_collection():
    global col, PATH
    if not col:
        col = Collection(PATH)
    return col


@app.route('/v1/card', methods=['GET'])
def get_card():
    args = flask.request.args
    deck_name = args['deck'] if 'deck' in args else 'value_war'
    col = get_collection()
    deck = col.decks.byName(deck_name)
    col.decks.select(deck['id'])
    card = col.sched.getCard()
    card_id = card.id

    # {'data': u'', 'did': 1384394478449, 'due': 1432055076, 'factor': 0,
    # 'flags': 0, 'id': 1414420814332, 'ivl': 0, 'lapses': 0, 'left': 2002,
    # 'mod': 1432055016, 'nid': 1414420814300, 'odid': 0, 'odue': 0, 'ord': 0,
    # 'queue': 1, 'reps': 37, 'type': 1, 'usn': 327}

    if not card:
        # current deck is finished
        print "finisehd"
    card_dict = {
        'question': card.q(),
        'answer': card.a(),
        'id': card_id
    }
    return flask.jsonify(card_dict)


@app.route('/v1/card', methods=['PUT'])
def answer_card():
    request = json.loads(flask.request.data)
    card_id = request['id']
    ease = request['ease']
    card = col.getCard(card_id)
    col.sched.answerCard(card, ease)
    return flask.Response(status=200)
