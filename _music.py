from dragonfly import Grammar, AppContext, MappingRule, Key, Text


class MusicRule(MappingRule):
    mapping = {
        "play | pause": Key("space"),
        "hunt": Key("w-f"),
        "next song": Key("w-right"),
        "last song": Key("w-left"),
        "louder": Key("w-up"),
        "softer": Key("w-down"),
    }


context = AppContext(executable="Music")
grammar = Grammar("music", context=context)
grammar.add_rule(MusicRule())
grammar.load()
