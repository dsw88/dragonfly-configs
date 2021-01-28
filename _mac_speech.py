from dragonfly import Grammar, MappingRule, Function, Key
from dragonfly import get_engine

grammar = Grammar("macspeech")
sleeping = False


def speech_on():
    global sleeping
    if not sleeping:
        sleeping = True
        grammar.set_exclusiveness(True)
    Key("win,win").execute()
    print("Mac Speech On")


def speech_off():
    global sleeping
    if sleeping:
        Key("escape").execute()
        sleeping = False
        grammar.set_exclusiveness(False)
    print("Mac Speech Off")


class MacSpeechRule(MappingRule):
    mapping = {
        "crazy idea": Key("a"),
        "speech on": Function(lambda: get_engine().stop_saving_adaptation_state())
        + Function(speech_on),
        "speech off": Function(speech_off)
        + Function(lambda: get_engine().start_saving_adaptation_state()),
    }


grammar.add_rule(MacSpeechRule())
grammar.load()
