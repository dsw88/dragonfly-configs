from dragonfly import (
    Key,
    Grammar,
    CompoundRule,
    Choice,
    MappingRule,
    IntegerRef,
    Dictation,
    Function,
)
from dragonfly.windows import Window
import applescript


def focus_app(app_name):
    if app_name == "":
        return
    script = f'tell application "{app_name}" to activate'
    applescript.AppleScript(script).run()


# Requires the 'Magnet' tool in MacOS
class MagnetRule(CompoundRule):
    spec = "snap <region>"
    extras = [
        Choice(
            "region",
            {
                "left": Key("ca-l"),
                "right": Key("ca-r"),
                "all": Key("ca-m"),
                "full screen": Key("wc-f"),
            },
        )
    ]

    def _process_recognition(self, node, extras):
        extras["region"].execute()


# Requires Vimac
class VimacRule(MappingRule):
    mapping = {"good": Key("a-space"), "slide": Key("c-;")}


class AppFocusRule(MappingRule):
    mapping = {"focus <app_name>": Function(focus_app)}
    extras = [
        Choice(
            "app_name",
            {
                "intellij [idea]": "IntelliJ IDEA",
                "teams": "Microsoft Teams",
                "eye term": "iTerm2",
                "terminal": "Terminal",
                "edge": "Microsoft Edge",
                "chrome": "Google Chrome",
                "amazon music": "Amazon Music",
                "music": "Music",
                "outlook": "Microsoft Outlook",
                "zoom": "zoom.us",
                "code": "Visual Studio Code",
                "slack": "Slack",
                "obsidian": "Obsidian",
                "excel": "Microsoft Excel",
                "power point": "Microsoft PowerPoint",
                "word": "Microsoft Word",
                "firefox": "Firefox",
            },
        )
    ]
    defaults = {"lang": ""}


class WindowNavigationRule(MappingRule):
    mapping = {
        "program next [<n>]": Key("w-tab:%(n)d"),
        "program last [<n>]": Key("ws-tab:%(n)d"),
        "window next [<n>]": Key("w-backtick:%(n)d"),
        "window last [<n>]": Key("ws-backtick:%(n)d"),
        "window close": Key("w-w"),
        "swap": Key("w-tab"),
        "desktop next": Key("ctrl:down/50")
        + Key("right/50")
        + Key("ctrl:up"),  # TODO - Broken
        "desktop last": Key("c-left"),  # TODO - Broken
        "mission control": Key("ctrl:down/50")
        + Key("up/50")
        + Key("ctrl:up"),  # TODO - Broken
    }
    extras = [IntegerRef("n", 1, 9999)]
    defaults = {"n": 1}


class GlobalControlRule(MappingRule):
    mapping = {
        "program close": Key("w-q"),
        "computer lock": Key("cw-q"),
        "spotlight": Key("w-space"),
    }


grammar = Grammar(name="global_control")
grammar.add_rule(MagnetRule())
grammar.add_rule(VimacRule())
grammar.add_rule(AppFocusRule())
grammar.add_rule(WindowNavigationRule())
grammar.add_rule(GlobalControlRule())
grammar.load()
