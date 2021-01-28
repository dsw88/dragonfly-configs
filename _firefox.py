from dragonfly import Grammar, AppContext, MappingRule, Key


class FirefoxRule(MappingRule):
    mapping = {
        "window new": Key("w-n"),
        "tab new": Key("w-t"),
        "tab reopen": Key("ws-t"),
        "tab close": Key("w-w"),
        "go url": Key("w-l"),
        "go back": Key("w-["),
        "go forward": Key("w-]"),
        "tab next": Key("c-tab"),
        "tab last": Key("cs-tab"),
        "refresh it": Key("w-r"),
    }


context = AppContext(executable="Firefox")
grammar = Grammar("firefox", context=context)
grammar.add_rule(FirefoxRule())
grammar.load()
