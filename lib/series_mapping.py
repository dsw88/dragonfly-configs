from dragonfly import CompoundRule, MappingRule, RuleRef, Repetition


class SeriesMappingRule(CompoundRule):
    def __init__(self, name, mapping, extras=None, defaults=None, command_prefix=""):
        mapping_rule = MappingRule(
            name=f"{name}-mapping",
            mapping=mapping,
            extras=extras,
            defaults=defaults,
            exported=False,
        )
        single = RuleRef(rule=mapping_rule)
        series = Repetition(single, min=1, max=16, name="series")

        compound_spec = f"{command_prefix} <series>"
        compound_extras = [series]
        CompoundRule.__init__(
            self, name=name, spec=compound_spec, extras=compound_extras, exported=True
        )

    def _process_recognition(self, node, extras):  # @UnusedVariable
        series = extras["series"]
        for action in series:
            action.execute()
