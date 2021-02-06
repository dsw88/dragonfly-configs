from dragonfly import Grammar, Key

from _keyboard import alphabet
from lib.series_mapping import SeriesMappingRule

caps_mapping = {word: Key(alphabet[word].upper()) for word in alphabet}
caps_rule = SeriesMappingRule(name="caps", mapping=caps_mapping, command_prefix="ship")

caps_mapping = {word: Key(alphabet[word].upper()) for word in alphabet}
grammar = Grammar("keyboard")
grammar.add_rule(caps_rule)
grammar.load()
