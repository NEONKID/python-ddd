from pydantic import errors


class CommandResult:
    def __init__(self, **kwargs) -> None:
        self.__errors = []
        self.__kwargs = kwargs

    def __getattr__(self, attr):
        assert (
            not self.has_errors()
        ), f"Cannot access '{attr}'. CommandResult has errors.\n  Errors: {self.__errors}"
        return self.__kwargs[attr]

    def has_errors(self):
        return len(self.__errors) > 0

    def add_error(self, error):
        self.__errors.append(error)

    @classmethod
    def ok(cls, **kwargs):
        return CommandResult(**kwargs)

    @classmethod
    def error(cls, errors):
        result = CommandResult()
        for error in errors:
            result.add_error(error)
        return result


class CommandHandler:
    pass