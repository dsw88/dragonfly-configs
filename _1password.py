from dragonfly import (
    Key,
    Grammar,
    MappingRule,
)


# Requires the 'Magnet' tool in MacOS
class OnePasswordRule(MappingRule):
    mapping = {
        "password show": Key("w-backslash"),
        "password copy": Key("ws-c"),
    }


grammar = Grammar(name="1password")
grammar.add_rule(OnePasswordRule())
grammar.load()
