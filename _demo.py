import dragonfly


class ExampleCustomRule(dragonfly.CompoundRule):
    spec = "I want to eat <food>"
    extras = [
        dragonfly.Choice(
            "food", {"(an | a juicy) apple": "good", "a [greasy] hamburger": "bad"}
        )
    ]

    def _process_recognition(self, node, extras):
        good_or_bad = extras["food"]
        print("That is a %s idea!" % good_or_bad)


class ExampleDictationRule(dragonfly.MappingRule):
    mapping = {
        "dictate <text>": dragonfly.Function(
            lambda text: print("I heard %r!" % str(text))
        ),
    }
    extras = [dragonfly.Dictation("text")]


grammar = dragonfly.Grammar(name="demo")
grammar.add_rule(ExampleCustomRule())
grammar.add_rule(ExampleDictationRule())
grammar.load()
