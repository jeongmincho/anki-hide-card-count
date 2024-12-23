from aqt import gui_hooks
from aqt import mw
from anki.hooks import wrap
from aqt.reviewer import Reviewer

def hide_card_count(self, _old):
    return ""

def init():
    Reviewer._remaining = wrap(Reviewer._remaining, hide_card_count, 'around')

gui_hooks.profile_did_open.append(init)
