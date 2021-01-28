from dragonfly import Grammar, AppContext, MappingRule, Key, Text


class OutlookRule(MappingRule):
    mapping = {
        "flag": Key("c-1"),
        "clear flag": Key("c-0"),
        "mark viewed": Key("w-t"),
    }


context = AppContext(executable="Outlook")
grammar = Grammar("outlook", context=context)
grammar.add_rule(OutlookRule())
grammar.load()
