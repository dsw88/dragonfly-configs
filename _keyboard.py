from dragonfly import (
    Grammar,
    Key,
    IntegerRef,
    Text,
    Dictation,
)

from lib.series_mapping import SeriesMappingRule

alphabet = {
    "air": "a",
    "bat": "b",
    "cap": "c",
    "drum": "d",
    "each": "e",
    "fine": "f",
    "gust": "g",
    "harp": "h",
    "sit": "i",
    "jury": "j",
    "crunch": "k",
    "look": "l",
    "made": "m",
    "near": "n",
    "odd": "o",
    "pit": "p",
    "quench": "q",
    "red": "r",
    "sun": "s",
    "trap": "t",
    "urge": "u",
    "vest": "v",
    "whale": "w",
    "plex": "x",
    "yank": "y",
    "zip": "z",
}
alphabet_mapping = {word: Key(alphabet[word]) for word in alphabet}

other_keys = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
    "enter": "enter",
    "tab": "tab",
    "space": "space",
    "escape": "escape",
    "dash": "hyphen",
    "equals": "=",
    "back tick": "`",
    "slash": "slash",
    "back slash": "backslash",
    "semicolon": ";",
    "quote": "squote",
    "single quote": "squote",
    "left square": "[",
    "right square": "]",
    "comma": "comma",
    "period": "dot",
    "dot": "dot",
}
other_keys_mapping = {key: Key(other_keys[key]) for key in other_keys}

number_keys = {
    "left": "left",
    "right": "right",
    "up": "up",
    "down": "down",
}

shifted_keys_mapping = {
    "(wipe | back space | delete) [<n>]": Key("backspace:%(n)d"),
    "bang": Key("!"),
    "at sign": Key("@"),
    "hash | pound": Key("#"),
    "dollar": Key("$"),
    "percent | modulo": Key("percent"),
    "carrot": Key("^"),
    "ampersand": Key("&"),
    "star | asterisk": Key("*"),
    "left parentheses": Key("("),
    "right parentheses": Key(")"),
    "arguments": Key("(,),left"),  # TODO - Figure out how to make this shorter
    "minus": Key("hyphen"),
    "underscore": Key("_"),
    "plus": Key("+"),
    "tilde": Key("~"),
    "left bracket": Key("{"),
    "right bracket": Key("}"),
    "colon": Key("colon"),
    "double quote": Key("dquote"),
    "question mark": Key("question"),
    "bar": Key("|"),
    "left angle": Key("<"),
    "right angle": Key(">"),
}
keyboard_mapping = {**other_keys_mapping, **shifted_keys_mapping}

edit_mapping = {
    "slap": Key("w-right") + Key("enter"),
    "cut that": Key("w-x"),
    "copy that": Key("w-c"),
    "paste that": Key("w-v"),
    "undo that | nope": Key("w-z"),
    "redo that | yep": Key("ws-z"),
    "hunt": Key("w-f"),
    "save that": Key("w-s"),
    "select all": Key("w-a"),
    "select line": Key("w-right,ws-left"),
    "select up [<n>]": Key("s-up:%(n)d"),
    "select down [<n>]": Key("s-down:%(n)d"),
    "select right [<n>]": Key("s-right:%(n)d"),
    "select left [<n>]": Key("s-left:%(n)d"),
    "select word": Key("a-left,as-right"),
    "select word right [<n>]": Key("as-right:%(n)d"),
    "select word left [<n>]": Key("as-left:%(n)d"),
    "select way left": Key("ws-left"),
    "select way right": Key("ws-right"),
    "select way up": Key("ws-up"),
    "select way down": Key("ws-down"),
    "delete line": Key("w-right,ws-left,backspace"),
    "delete word left": Key("as-left,backspace"),
    "delete word right": Key("as-right,backspace"),
    "delete way right": Key("ws-right,backspace"),
    "delete way left": Key("ws-left,backspace"),
    "delete way up": Key("ws-up,backspace"),
    "delete way down": Key("ws-down,backspace"),
}

navigation_mapping = {
    "go up [<n>]": Key("up:%(n)d"),
    "go down [<n>]": Key("down:%(n)d"),
    "go left [<n>]": Key("left:%(n)d"),
    "go right [<n>]": Key("right:%(n)d"),
    "go word left [<n>]": Key("a-left:%(n)d"),
    "go word right [<n>]": Key("a-right:%(n)d"),
    "go way left": Key("w-left"),
    "go way right": Key("w-right"),
    "go way up": Key("w-up"),
    "go way down": Key("w-down"),
}

formatting_mapping = {
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
    IntegerRef("n", 1, 9999),
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


defaults = {"n": 1}

keyboard_rule = SeriesMappingRule(
    name="keyboard",
    mapping={
        **alphabet_mapping,
        **keyboard_mapping,
        **navigation_mapping,
        **edit_mapping,
        **formatting_mapping,
    },
    extras=extras,
    defaults=defaults,
)

# Modifier rules
modifiers = {
    "shift": "s",
    "command": "w",
    "alt": "a",
    "control": "c",
    "command shift": "ws",
    "control shift": "cs",
    "alt shift": "as",
    "command alt": "wa",
    "control command": "cw",
    "control alt": "ca",
}

grammar = Grammar("keyboard")
grammar.add_rule(keyboard_rule)

modifier_keys = {**alphabet, **other_keys, **number_keys}
for modifier_command, modifier_code in modifiers.items():
    mapping = {
        modifier_key: Key(f"{modifier_code}-{modifier_keys[modifier_key]}")
        for modifier_key in modifier_keys
    }
    rule = SeriesMappingRule(
        name=modifier_command, mapping=mapping, command_prefix=modifier_command
    )
    grammar.add_rule(rule)

grammar.load()
