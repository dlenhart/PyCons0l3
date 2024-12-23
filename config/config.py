#!/usr/bin/python

from configparser import ConfigParser


class SectionNotFoundException(Exception):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)


class KeyNotFoundException(Exception):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)


class Config:
    _filename = None
    _section = None
    _config = {}

    def __init__(self, filename: str, section: str):
        self._filename = filename
        self._section = section
        self.load()

    def load(self) -> None:
        parser = ConfigParser()
        parser.read(self._filename)

        file_config = {}

        if parser.has_section(self._section):
            params = parser.items(self._section)
            for param in params:
                file_config[param[0]] = param[1]
        else:
            raise SectionNotFoundException('Section {0} not found in the {1} file'
                                           .format(self._section, self._filename))

        self._config = file_config

    def all(self) -> dict:
        return self._config

    def get(self, key) -> str:
        if key in self._config:
            return self._config[key]
        else:
            raise KeyNotFoundException(f'Key not found: {key}')

    def set(self, key, value) -> None:
        self._config[key] = value

    def update(self, key, new_value) -> None:
        if key in self._config:
            self._config[key] = new_value
        else:
            raise KeyNotFoundException(f'Key not found: {key}')

    def delete(self, key) -> None:
        if key in self._config:
            self._config.pop(key)
        else:
            raise KeyNotFoundException(f'Key not found: {key}')
