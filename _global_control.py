from dragonfly import (
    Key,
    Grammar,
    CompoundRule,
    Choice,
    MappingRule,
    IntegerRef,
)


# Requires the 'Magnet' tool in MacOS
class SnapWindowRule(CompoundRule):
    spec = "snap <region>"
    extras = [
        Choice(
            "region",
            {
                "left": Key("ca-left"),  # TODO -  Broken
                "right": Key("ca-right"),  # TODO - Broken
                "all": Key("ca-m"),
            },
        )
    ]

    def _process_recognition(self, node, extras):
        extras["region"].execute()


class WindowNavigationRule(MappingRule):
    mapping = {
        "window next [<n>]": Key("w-tab:%(n)d"),
        "window last [<n>]": Key("ws-tab:%(n)d"),
        "swap": Key("w-tab"),
    }
    extras = [IntegerRef("n", 1, 9999)]
    defaults = {"n": 1}


class GlobalControlRule(MappingRule):
    mapping = {"program close": Key("w-q"), "computer lock": Key("cw-q")}


grammar = Grammar(name="global_control")
grammar.add_rule(SnapWindowRule())
grammar.add_rule(WindowNavigationRule())
grammar.add_rule(GlobalControlRule())
grammar.load()
