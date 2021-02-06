# ---------------------------------------------------------------------------
# Create a compound rule which demonstrates CompoundRule and Choice types.
from dragonfly import Grammar, MappingRule, Function, Choice
from lang.python_lang import python_rule
from lang.terraform_lang import terraform_rule


langs = {
    "python": python_rule,
    "terraform": terraform_rule,
}


def enable_lang(lang):
    print(f"Enable {lang}")
    for current in langs:
        if lang == current:
            langs[current].enable()
        else:
            langs[current].disable()


grammar = Grammar("programming")
for lang in langs:
    rule = langs[lang]
    grammar.add_rule(rule)
    rule.disable()


class EnableLangRule(MappingRule):
    mapping = {
        "enable <lang>": Function(enable_lang),
    }
    extras = [
        Choice(
            "lang",
            {
                "terraform": "terraform",
                "python": "python",
            },
        )
    ]
    defaults = {"lang": ""}


grammar.add_rule(EnableLangRule())
grammar.load()
