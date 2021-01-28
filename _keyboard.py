from dragonfly import (
    Grammar,
    Key,
    IntegerRef,
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

keyboard_mapping = {
    "one": Key("1"),
    "two": Key("2"),
    "three": Key("3"),
    "four": Key("4"),
    "five": Key("5"),
    "six": Key("6"),
    "seven": Key("7"),
    "eight": Key("8"),
    "nine": Key("9"),
    "zero": Key("0"),
    "enter": Key("enter"),
    "tab": Key("tab"),
    "space": Key("space"),
    "(wipe | back space | delete) [<n>]": Key("backspace:%(n)d"),
    "escape": Key("escape"),
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
    "hyphen | minus | dash": Key("hyphen"),
    "underscore": Key("_"),
    "plus": Key("+"),
    "equals": Key("="),
    "tilde": Key("~"),
    "back tick": Key("`"),
    "left bracket": Key("{"),
    "right bracket": Key("}"),
    "left square": Key("["),
    "right square": Key("]"),
    "colon": Key("colon"),
    "semicolon": Key(";"),
    "single quote": Key("squote"),
    "double quote": Key("dquote"),
    "question mark": Key("question"),
    "forward slash": Key("slash"),
    "back slash": Key("backslash"),
    "bar": Key("|"),
    "comma": Key("comma"),
    "period": Key("dot"),
    "left angle": Key("<"),
    "right angle": Key(">"),
}

edit_mapping = {
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

extras = [IntegerRef("n", 1, 9999)]
defaults = {"n": 1}

keyboard_rule = SeriesMappingRule(
    mapping={
        **alphabet_mapping,
        **keyboard_mapping,
        **navigation_mapping,
        **edit_mapping,
    },
    extras=extras,
    defaults=defaults,
)


grammar = Grammar("keyboard")
grammar.add_rule(keyboard_rule)
grammar.load()
