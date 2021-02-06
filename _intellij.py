from dragonfly import Grammar, AppContext, MappingRule, Key, Text, Dictation, Function
from lang.intellij_support import run_action


class IntellijRule(MappingRule):
    mapping = {
        "palette": Key("ws-a"),
        "please <paletteaction>": Key("ws-a") + Text("%(paletteaction)s"),
        "files": Key("ws-o"),
        "last": Key("c-tab"),
        "go there": Key("w-b"),
        "go back": Key("w-["),
        "go forward": Key("w-]"),
        "recent": Key("w-e"),
        "go next method": Key("cs-down"),
        "go last method": Key("cs-up"),
        "go next error": Key("f2"),
        "go last error": Key("s-f2"),
        "hunt replace": Key("w-r"),
        "hunt project": Key("ws-f"),
        "snippets": Key("w-j"),
        "show error": Key("w-f1"),
        "fix that": Key("a-enter"),
        "show type": Key("cs-p"),
        "show parameters": Key("w-p"),
        "tab next": Key("ws-]"),
        "tab last": Key("ws-["),
        "tab close": Key("w-w"),
        "tab reopen": Function(run_action, action_name="reopen tab"),
        "toggle comment": Key("w-slash"),
        "wide": Key("a-up"),
        "skinny": Key("a-down"),
        "line down": Key("as-down"),
        "line up": Key("as-up"),
        "split next": Key("a-tab"),
        "split last": Key("as-tab"),
        "split vertical": Function(run_action, action_name="Split Right"),
        "split horizontal": Function(run_action, action_name="Split Down"),
        # TODO - Multi cursor down
        # TODO - Multi cursor up
        "refactor that": Key("c-t"),
        "toggle project": Key("w-1"),
        "go way up": Key("w-home"),
        "go way down": Key("w-end"),
        "vim save": Text(":w") + Key("enter"),
        "vim quit": Text(":wq") + Key("enter"),
        "punch": Key("w-right,comma,enter"),
    }
    extras = [Dictation("paletteaction")]


context = AppContext(executable="idea")
grammar = Grammar("intellij", context=context)
grammar.add_rule(IntellijRule())
grammar.load()
