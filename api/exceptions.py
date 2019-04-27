class InvalidInput(Exception):
    def __init__(self, errors: dict):
        super().__init__(str(errors))
        self.errors = errors


class BadRequest(Exception):
    pass
