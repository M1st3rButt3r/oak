class Error:
    def __init__(self, name, details, position):
        self.name = name
        self.details = details
        self.pos = position

    def __repr__(self):
        return f"[{self.name}]: {self.details} in '{self.pos.fn}' line {self.pos.ln} column {self.pos.col}"


class IllegalCharError(Error):
    def __init__(self, details, position):
        super().__init__("IllegalCharError", f"Forbidden char '{details}'", position)