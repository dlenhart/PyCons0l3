#!/usr/bin/env python3

"""
Example usage of the Console library - Drew D. Lenhart
"""

import time
import datetime

from console.console import Console
from config.config import Config


def print_fancy_colors():
    Console.color('Woah, some red text!', 'red')
    Console.color('Woah, some black text!', 'black')
    Console.color('Woah, some green text!', 'green')
    Console.color('Woah, some yellow text!', 'yellow')
    Console.color('Woah, some blue text!', 'blue')
    Console.color('Woah, some magenta text!', 'magenta')
    Console.color('Woah, some cyan text!', 'cyan')
    Console.color('Woah, some light gray text!', 'light_gray')
    Console.color('Woah, some dark grey text!', 'dark_gray')
    Console.color('Woah, some bright red text!', 'bright_red')
    Console.color('Woah, some bright green text!', 'bright_green')
    Console.color('Woah, some bright yellow text!', 'bright_yellow')
    Console.color('Woah, some bright blue text!', 'bright_blue')
    Console.color('Woah, some bright magenta text!', 'bright_magenta')
    Console.color('Woah, some bright cyan text!', 'bright_cyan')
    Console.color('Woah, some white text!', 'white')


def print_fancy_background_colors():
    Console.background('red', 'Woah, some red background!', 'white')
    Console.background('white', 'Woah, some white background!', 'black')
    Console.background('black', 'Woah, some black background!', 'white')
    Console.background('green', 'Woah, some green background!', 'white', True)
    Console.background('magenta', 'Woah, some magenta background!', 'white')
    Console.background('cyan', 'Woah, some cyan background!', 'white')
    Console.background('light_gray', 'Woah, some light gray background!', 'black')
    Console.background('dark_gray', 'Woah, some dark gray background!', 'white')
    Console.background('bright_red', 'Woah, some bright red background!', 'white')
    Console.background('bright_green', 'Woah, some bright green background!', 'white')
    Console.background('bright_yellow', 'Woah, some bright yellow background!', 'black')
    Console.background('bright_blue', 'Woah, some bright blue background!', 'black')
    Console.background('bright_magenta', 'Woah, some bright magenta background!', 'white')
    Console.background('bright_cyan', 'Woah, some bright cyan background!', 'black')


def main():
    start = time.perf_counter()

    '''Print bar with optional text, width is optional'''
    Console.bar()
    Console.bar("START TIME", "blue")
    Console.write(f'{datetime.datetime.now()}')
    Console.bar("BEGIN PROCESS")

    '''Print text with color, or text with background and optional text color'''
    print_fancy_colors()
    print_fancy_background_colors()

    lorem = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt '
             'ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip '
             'ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla '
             'pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
             )

    '''Set optional width'''
    width = 86
    Console.box(lorem, True, 'bright_red', width)
    Console.background('green', 'Woah, some green background!', 'white', True, width)
    Console.bar("WOW A BAR", "green", width=width)
    Console.box(lorem, False, 'light_gray', width)

    time.sleep(2)

    '''Load some configurations'''
    config = Config(filename='example.ini', section="configurations")

    Console.color('Loading configurations....', 'green')

    '''Get a value'''
    Console.write(config.get('host'))

    '''Set a new key/value'''
    config.set("new", "key")
    Console.write(str(config.all()))

    '''Delete a key/value'''
    config.delete('host')
    Console.write(str(config.all()))

    '''Update key/value'''
    config.update('database', 'TEST2')
    Console.write(str(config.all()))

    Console.bar("Time Elapsed")
    elapsed = time.perf_counter() - start
    Console.write(f'Time {elapsed:0.4}')
    Console.background('green', 'Success!', 'white', False)

    '''Print special text options'''
    Console.write(Console.italic('Process is completed'))
    Console.write(Console.underline('Process is fully completed'))
    Console.write(Console.italic(Console.bold('I promise the process is fully completed')))

    '''Print a spinner'''
    Console.spinner('Waiting to complete.....', spinner_type="DOTS", iterations=4)
    Console.spinner('Waiting to complete.....', spinner_type="LINES", iterations=6)
    Console.spinner('Waiting to complete.....', spinner_type="PIPE", iterations=6)
    Console.spinner('Waiting to complete.....', spinner_type="STAR", iterations=6)

    Console.bar()


if __name__ == "__main__":
    main()
