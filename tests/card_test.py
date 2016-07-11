# -*- coding: utf-8 -*-
from anki import Collection

col = None
PATH = "/home/social/Anki/luxerypro/collection.anki2"

def collection_test():
    col = Collection("/home/social/Anki/luxerypro/collection.anki2")
    card = col.sched.getCard()
    if not card:
        # current deck is finished
        print "finisehd"
    print card.q()
    print card.a()
    col.sched.answerCard(card, 1)

def get_collection():
    global col, PATH
    if not col:
        col = Collection(PATH)
    return col


def get_card(deck_name):
    col = get_collection()
    deck = col.decks.byName(deck_name)
    col.decks.select(deck['id'])
    card = col.sched.getCard()
    card_id = card.id

    #{'data': u'', 'did': 1384394478449, 'due': 1432055076, 'factor': 0,
    # 'flags': 0, 'id': 1414420814332, 'ivl': 0, 'lapses': 0, 'left': 2002,
    # 'mod': 1432055016, 'nid': 1414420814300, 'odid': 0, 'odue': 0, 'ord': 0,
    # 'queue': 1, 'reps': 37, 'type': 1, 'usn': 327}

    if not card:
        # current deck is finished
        print "finisehd"
    card_dict = {
        'question': card.q(),
        'answer': card.a(),
        'id': card.id
    }
    print card_dict

def answer_card(card_id, ease):
    card = col.getCard(card_id)
    col.sched.answerCard(card, ease)

if __name__ == "__main__":
    #collection_test()
    get_card("arrow_english")
