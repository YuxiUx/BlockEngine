import readline
class DirectDebugConsole:
    """
      Direct debug console provide reltime access to application variables and code
      Only for development! 
      This file is part of blockengine
      Code by YuxiUx
    """
    def __init__(self, key=False, local={}, glob={}, default="L"):
        print("Using direct console. Don't do this on production")
        print(" ")
        self.key = key
        self.default = default
        self.local = local
        self.glob = glob
    def Input(self, arg=False):
        inp = ""
        try:
            print("Enter a command or \m for multiline input")
            inp = input('$: ')
            if inp.strip() == "\m":
                self.MultiInput()
            else:
                self.Exec(inp)
        except Exception as e:
            print(e)
            
    def MultiInput(self, arg=False):
        print("Multilne input. When are you done enter blank line")
        inp = ""
        c = " "
        try:
            while c != "":
                c = input('$$: ')
                inp += c + "\n"
            self.Exec(inp)
        except Exception as e:
            print(e)
    def Listener(self, event):
        if event.key == self.key:
            if self.default == "L":
                self.Input()
            else:
                self.MultiInput()
    def Exec(self, cmd):
        try:
            exec (cmd, self.local, self.glob)
            print("OK")
        except Exception as e:
            #print("Failed to run your command")
            print(e)
        print(" ")
    