from dragonfly import Grammar, AppContext, MappingRule, Key, Text


class TerminalRule(MappingRule):
    mapping = {
        "tab next": Key("ws-]"),
        "tab previous": Key("ws-["),
        "tab new": Key("w-t"),
        "kill all": Key("c-c"),
        "split vertical": Key("w-d"),
        "split horizontal": Key("ws-d"),
        "split next": Key("w-]"),
        "split last": Key("w-["),
        "exit": Text("exit") + Key("enter"),
        "where am": Text("pwd") + Key("enter"),
        "list": Text("ls -lha") + Key("enter"),
        "go home": Text("cd ~") + Key("enter"),
        "parent": Text("cd ..") + Key("enter"),
        "change dir": Text("cd "),
        "navi": Key("c-g"),  # Requires navi
        "terraform plan": Text("terraform plan") + Key("enter"),
        "terraform apply": Text("terraform apply") + Key("enter"),
        "terraform init": Text("terraform init") + Key("enter"),
        "terraform destroy": Text("terraform destroy"),
        "cat": Text("cat "),
        "vim": Text("vim "),
        "make": Text("make") + Key("enter"),
        "history": Text("history") + Key("enter"),
        "find history": Text("fh") + Key("enter"),  # Requires fzf
        "find directory": Text("fd") + Key("enter"),  # Requires fzf
        "keep alive": Text("while true ; do date; sleep 15; done") + Key("enter"),
        "pie test": Text("pytest") + Key("enter"),
        "pip install": Text("pip install "),
        "pip install requirements": Text("pip install -r requirements.txt")
        + Key("enter"),
        "pip list": Text("pip list") + Key("enter"),
        "vim save": Text(":w") + Key("enter"),
        "vim quit": Text(":wq") + Key("enter"),
    }


iterm_context = AppContext(executable="iTerm2")
terminal_context = AppContext(executable="Terminal")
terminals_context = iterm_context | terminal_context
grammar = Grammar("terminal", context=terminals_context)
grammar.add_rule(TerminalRule())
grammar.load()
