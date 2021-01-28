from dragonfly import MappingRule, Function, Dictation, Text, Grammar


class TextFormattingRule(MappingRule):
    mapping = {
        "say <text>": Text("%(text)s"),
        "snake <snaketext>": Text("%(snaketext)s"),
        "kebab <kebabtext>": Text("%(kebabtext)s"),
        "hammer <hammertext>": Text("%(hammertext)s"),
        "title <titletext>": Text("%(titletext)s"),
        "sentence <sentencetext>": Text("%(sentencetext)s"),
        "all caps <allcapstext>": Text("%(allcapstext)s"),
        "camel <cameltext>": Text("%(cameltext)s"),
        "constant <constanttext>": Text("%(constanttext)s"),
        "dotted <dottedtext>": Text("%(dottedtext)s"),
        "dunder <snaketext>": Text("__%(snaketext)s"),
        "slasher <slashtext>": Text("%(slashtext)s"),
        "smash <smashtext>": Text("%(smashtext)s"),
    }
    extras = [
        Dictation("text"),
        Dictation("snaketext").lower().replace(" ", "_"),
        Dictation("kebabtext").lower().replace(" ", "-"),
        Dictation("hammertext").title().replace(" ", ""),
        Dictation("titletext").title(),
        Dictation("sentencetext").capitalize(),
        Dictation("allcapstext").upper(),
        Dictation("cameltext").camel(),
        Dictation("constanttext").upper().replace(" ", "_"),
        Dictation("dottedtext").replace(" ", "."),
        Dictation("slashtext").replace(" ", "/"),
        Dictation("smashtext").replace(" ", ""),
    ]


grammar = Grammar(name="text_formatting")
grammar.add_rule(TextFormattingRule())
grammar.load()
