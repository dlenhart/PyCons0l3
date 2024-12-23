#!/usr/bin/env python3

import re
import textwrap
import sys
import time
from enum import Enum

"""
Name:           PyCons0l3
Description:    Make things pretty in the console. Bars, boxes, colored text, backgrounds, simple spinners etc..
Author:         Drew D. Lenhart
Repository:     https://github.com/dlenhart/pycons0l3
"""


class Constants(Enum):
    MAX_WIDTH = 70
    LEFT_PADDING_2 = 2
    LEFT_PADDING_4 = 4
    RIGHT_PADDING_2 = 2
    RIGHT_PADDING_4 = 4
    TOP_BOX_PADDING = 1
    BOTTOM_BOX_PADDING = 1


class Colors(Enum):
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


class Spinner(Enum):
    CLEAR_LINE = '\033[K'
    DOTS = {
        "interval": 80,
        "frames": [
            "⠋",
            "⠙",
            "⠹",
            "⠸",
            "⠼",
            "⠴",
            "⠦",
            "⠧",
            "⠇",
            "⠏"
        ]
    }
    LINES = {
        "interval": 100,
        "frames": [
            "-",
            "\\",
            "|",
            "/"
        ]
    }
    PIPE = {
        "interval": 130,
        "frames": [
            "┤",
            "┘",
            "┴",
            "└",
            "├",
            "┌",
            "┬",
            "┐"
        ]
    }
    STAR = {
        "interval": 100,
        "frames": [
            "+",
            "x",
            "*"
        ]
    }


class Console:

    @staticmethod
    def write(message: str = '') -> None:
        """Print to the console"""
        print(f'{message}')

    @staticmethod
    def bar(
            message: str = '',
            color: str = None,
            line_type: str = '-',
            width: int = Constants.MAX_WIDTH.value
    ) -> None:
        """Generate a bar for the console with styling options"""
        padding = Console._build_bar_characters(
            Console._max_bar_width(width, Constants.LEFT_PADDING_2.value + len(message)),
            line_type
        )

        Console._print_line(color, '+' + Console._build_bar_characters(
            Constants.LEFT_PADDING_2.value, line_type
        ) + message + padding + '+')

    @staticmethod
    def box(
            text: str = '',
            center: bool = True,
            color: str = None,
            width: int = Constants.MAX_WIDTH.value
    ) -> None:
        """Generate a box for the console with styling options"""
        wrapped_text = Console._wrap_text(text, width)
        max_line_length = Console._max_length(wrapped_text)
        Console._print_line(color, Console._top_box_bar(max_line_length, width))

        for line in wrapped_text:
            operation = line.center(max_line_length) if center else Console._pad_non_centered_line(line, width)
            formatted_line = f"| {operation} |"
            Console._print_line(color, formatted_line)

        Console._print_line(color, Console._top_box_bar(max_line_length, width))

    @staticmethod
    def spinner(text: str = 'Some message here...', spinner_type: str = 'DOTS', iterations: int = 2):
        """Wrapper to animate a spinner"""
        spinner = Console._select_spinner(spinner_type)
        while True:
            Console._animate_spinner(list(spinner['frames']), spinner['interval'], text, iterations)
            break

        Console.write(Colors.RESET.value)

    @staticmethod
    def new_line() -> None:
        """New console line"""
        Console.write('\n')

    @staticmethod
    def bold(text: str = 'empty') -> str:
        """Style text as bold"""
        return '\033[1m' + text + '\033[0m'

    @staticmethod
    def italic(text: str = 'empty') -> str:
        """Style text as itallic"""
        return '\033[3m' + text + '\033[0m'

    @staticmethod
    def underline(text: str = 'empty') -> str:
        """Style text as underline"""
        return '\033[4m' + text + '\033[0m'

    @staticmethod
    def color(message: str, color: str = 'WHITE') -> None:
        """Write text to the console with color"""
        Console.write(Console._select_color(color) + message + Colors.RESET.value)

    @staticmethod
    def background(
            color: str,
            message: str = "",
            text_color: str = 'white',
            fill_width: bool = False,
            width: int = Constants.MAX_WIDTH.value
    ) -> None:
        """Write text to the console with background color"""
        message = Console._pad_line_with_spaces(fill_width, message, width)
        Console.write(
            Console._select_color(text_color) +
            Console._select_color('BACKGROUND_' + color) +
            message +
            Colors.RESET.value
        )

    @staticmethod
    def _select_color(color) -> str:
        """Dynamically select the color"""
        if color:
            func = getattr(Colors, color.upper())
            return func.value

        return Colors.WHITE.value

    @staticmethod
    def _select_spinner(spinner_type) -> str:
        """Dynamically select the spinner by type"""
        if type:
            func = getattr(Spinner, spinner_type.upper())
            return func.value

        return Spinner.DOTS.value

    @staticmethod
    def _max_bar_width(longest: int, smallest: int) -> int:
        """Get the maximum bar width"""
        return longest - smallest - 3

    @staticmethod
    def _build_bar_characters(count: int, char: str = '-') -> str:
        """Generate characters for bar"""
        return char * count

    @staticmethod
    def _max_length(wrapped_text) -> int:
        """Determine the max length of a text line"""
        max_line_length = max(len(line) for line in wrapped_text)
        return max_line_length

    @staticmethod
    def _wrap_text(text, width):
        """Wrap text"""
        wrapped_text = textwrap.wrap(text, width - 4)
        return wrapped_text

    @staticmethod
    def _pad_non_centered_line(line, width) -> str:
        """Generate line padding with spaces"""
        spaces = Console._build_bar_characters(width - len(line) - 4, ' ')
        return line + spaces

    @staticmethod
    def _pad_line_with_spaces(fill_width, message, width) -> str:
        """Generate line padding with spaces"""
        if fill_width:
            message = Console._pad_non_centered_line(message, width)
            padding = Constants.RIGHT_PADDING_4.value * " "
            message = f"{message}{padding}"
        return message

    @staticmethod
    def _print_line(color, line):
        """Dynamically call a class method by color or default"""
        if color:
            func = getattr(Console, 'color')
            func(line, color)
        else:
            Console.write(line)

    @staticmethod
    def _top_box_bar(max_line_length, total_width) -> str:
        """Generate the top of a box"""
        adjustments = ""
        if max_line_length < total_width:
            count = total_width - max_line_length
            adjustments = "-" * count

        return "+" + "-" * (max_line_length - 2) + adjustments + "+"

    @staticmethod
    def _longest_line_count(wrapped_text):
        """Return the length of the longest line in a block of wrapped text"""
        longest_line = 0
        for line in wrapped_text:
            if len(line) > longest_line:
                longest_line = len(line)
        return longest_line

    @staticmethod
    def _animate_spinner(frames, interval: str, label: str, iterations: int = 2):
        """Animate given frame for set number of iterations."""
        for i in range(iterations):
            for frame in frames:
                sys.stdout.write("\r{0} {1}".format(frame, label))
                sys.stdout.write(Spinner.CLEAR_LINE.value)
                sys.stdout.flush()
                time.sleep(0.001 * interval)

    @staticmethod
    def _parse_tags(message) -> str:
        """Parse tags in a given text & replace with appropriate style"""
        bold_tags = re.findall(r"<b>(.*?)</b>", message)
        underlined_tags = re.findall(r"<ul>(.*?)</ul>", message)
        itallic_tags = re.findall(r"<i>(.*?)</i>", message)

        for txt in bold_tags:
            message = message.replace('<b>' + txt + '</b>', Console.bold(txt)) if txt else None

        for txt in underlined_tags:
            message = message.replace('<ul>' + txt + '</ul>', Console.underline(txt)) if txt else None

        for txt in itallic_tags:
            message = message.replace('<i>' + txt + '</i>', Console.italic(txt)) if txt else None

        return message
