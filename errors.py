class UnicornError(Exception):
    def __init__(self, name: str):  # noqa
        self.name = name
