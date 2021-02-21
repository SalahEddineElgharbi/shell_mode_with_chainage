from expert_system.config.Cmd import Cmd



class Logger:
    def __init__(self, type):
        self.type = type

    def info(self, message, type=None):
        if Cmd.args.verbose:
            type = type or self.type
            print(f"<{type}>  -- {message}")
