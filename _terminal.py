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
        "git status": Text("git status") + Key("enter"),
        "git show branches": Text("git branch") + Key("enter"),
        "git commit": Text("git commit") + Key("enter"),
        "git pull": Text("git pull") + Key("enter"),
        "git push": Text("git push") + Key("enter"),
        "git add all": Text("git add -A") + Key("enter"),
        "git add": Text("git add "),
        "git branch": Text("git branch "),
        "git checkout": Text("git checkout "),
        "git clone": Text("git clone "),
        "git diff": Text("git diff") + Key("enter"),
        "git diff cached": Text("git diff --cached") + Key("enter"),
        "git in it": Text("git init") + Key("enter"),
        "git new branch": Text("git checkout -b "),
        "git push head": Text("git push origin HEAD") + Key("enter"),
        "git push tags": Text("git push --tags") + Key("enter"),
        "git (remove|delete) branch": Text("git branch -d ") + Key("enter"),
        "git reset": Text("git reset "),
        "git reset hard": Text("git reset --hard "),
        "git stash pop": Text("git stash pop") + Key("enter"),
        "git stash": Text("git stash") + Key("enter"),
        "git stash list": Text("git stash list") + Key("enter"),
        "git tag": Text("git tag "),
    }


iterm_context = AppContext(executable="iTerm2")
terminal_context = AppContext(executable="Terminal")
terminals_context = iterm_context | terminal_context
grammar = Grammar("terminal", context=terminals_context)
grammar.add_rule(TerminalRule())
grammar.load()
