from dragonfly import Grammar, MappingRule, IntegerRef, Key


class KeyboardRule(MappingRule):
    mapping = {
        "air": Key("a"),
        "bat": Key("b"),
        "cap": Key("c"),
        "drum": Key("d"),
        "each": Key("e"),
        "fine": Key("f"),
        "gust": Key("g"),
        "harp": Key("h"),
        "sit": Key("i"),
        "jury": Key("j"),
        "crunch": Key("k"),
        "look": Key("l"),
        "made": Key("m"),
        "near": Key("n"),
        "odd": Key("o"),
        "pit": Key("p"),
        "quench": Key("q"),
        "red": Key("r"),
        "sun": Key("s"),
        "trap": Key("t"),
        "urge": Key("u"),
        "vest": Key("v"),
        "whale": Key("w"),
        "plex": Key("x"),
        "yank": Key("y"),
        "zip": Key("z"),
        "enter": Key("enter"),
        "tab": Key("tab"),
        "space": Key("space"),
        "wipe | back space | delete": Key("backspace"),
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


class GlobalMovementRule(MappingRule):
    mapping = {
        "go up [<n>]": Key("up:%(n)d"),
        "go down [<n>]": Key("down:%(n)d"),
        "go left [<n>]": Key("left:%(n)d"),
        "go right [<n>]": Key("right:%(n)d"),
        "go home": Key("home"),
        "go end": Key("end"),
    }
    extras = [IntegerRef("n", 1, 9999)]
    defaults = {"n": 1}


grammar = Grammar("keyboard")
grammar.add_rule(KeyboardRule())
grammar.add_rule(GlobalMovementRule())
grammar.load()
