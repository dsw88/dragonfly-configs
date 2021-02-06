from dragonfly import Dictation, Text

from lib.series_mapping import SeriesMappingRule

formatting_mapping = {
    "hello typescript <text>": Text("Hello Typescript! %(text)s"),
}

extras = [
    Dictation("text"),
]


typescript_rule = SeriesMappingRule(
    name="typescript",
    mapping={
        **formatting_mapping,
    },
    extras=extras,
)
