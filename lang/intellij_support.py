from dragonfly import Key, Pause, Text


def invoke_live_template(template_name):
    Key("w-j").execute()
    Pause("5").execute()
    Text(template_name).execute()
    Key("enter").execute()


def run_action(action_name):
    Key("ws-a").execute()
    Pause("20").execute()
    Text(action_name).execute()
    Pause("20").execute()
    Key("enter").execute()
