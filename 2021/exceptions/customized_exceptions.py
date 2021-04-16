# coding=utf-8


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not allowed.

    Attributes:
        prev_stat -- state at beginning of transition
        next_stat -- attempted new state
        message   -- explanation of why the specific transition is not allowed
    """

    def __init__(self, prev_stat, next_stat, message):
        self.prev_stat = prev_stat
        self.next_stat = next_stat
        self.message = message


if __name__ == "__main__":
    try:
        raise InputError("int('xyz')", "Convertion Failure")
    except InputError as e:
        print(e.expression)
        print(e.message)
    finally:
        print("End")
