class GreetingCard:
    def __init__(self, recipient = "Dana Ev", sender = "Eyal Ch"):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        print(f"Dear {self._recipient},\n"
              f"Hello from,{self._sender}")