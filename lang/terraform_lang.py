from dragonfly import Dictation, Text

from lib.series_mapping import SeriesMappingRule

formatting_mapping = {
    "hello earth": Text("Hello Terraform!"),
    "something else": Text("ANother piece of text"),
}

extras = []


terraform_rule = SeriesMappingRule(
    name="terraform",
    mapping={
        **formatting_mapping,
    },
    extras=extras,
)
