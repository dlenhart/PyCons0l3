#!/usr/bin/env python3

"""
Colors - Color text and colored background for the console using method chaining

e.g.

console = Color()

console.text("Hi there, this is some text").color('red').background('white').print()
console.text("Hi there, this is some text").color('white').print()
console.text("Hi there, this is some text").color('magenta').print()
console.text("Hi there, this is some text").print()
"""


class Color:
    MAX_WIDTH = 70
    LEFT_PADDING = 2
    TOP_BOX_PADDING = 1
    BOTTOM_BOX_PADDING = 1
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GRAY = '\033[37m'
    DARK_GRAY = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    WHITE = '\033[97m'
    BACKGROUND_BLACK = '\033[40m'
    BACKGROUND_RED = '\033[41m'
    BACKGROUND_GREEN = '\033[42m'
    BACKGROUND_YELLOW = '\033[43m'
    BACKGROUND_BLUE = '\033[44m'
    BACKGROUND_MAGENTA = '\033[45m'
    BACKGROUND_CYAN = '\033[46m'
    BACKGROUND_LIGHT_GRAY = '\033[47m'
    BACKGROUND_DARK_GRAY = '\033[100m'
    BACKGROUND_BRIGHT_RED = '\033[101m'
    BACKGROUND_BRIGHT_GREEN = '\033[102m'
    BACKGROUND_BRIGHT_YELLOW = '\033[103m'
    BACKGROUND_BRIGHT_BLUE = '\033[104m'
    BACKGROUND_BRIGHT_MAGENTA = '\033[105m'
    BACKGROUND_BRIGHT_CYAN = '\033[106m'
    BACKGROUND_WHITE = '\033[107m'

    def __init__(self):
        self._text = None
        self._color = None
        self._background = None

    def print(self) -> None:
        print(f'{self._color}{self._background}{self._text}{Color.RESET}')

    def text(self, message=''):
        self._text = message
        return self

    def color(self, color: str = 'WHITE'):
        self._color = Color._select_color(color)
        return self

    def background(self, color: str = 'WHITE'):
        self._background = Color._select_color(color) + Color._select_color('BACKGROUND_' + color)
        return self

    @staticmethod
    def _select_color(color: str) -> str:
        func = getattr(Color, color.upper()) if color else Color.WHITE
        return func

