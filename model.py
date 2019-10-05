import json
import os

from abc import ABC
from abc import abstractmethod
from os.path import join, dirname, isdir


class AbstractPlant(ABC):
    def __init__(self, data_home):
        self.version = type(self).__name__.lower()
        self.data_home = data_home
        self.data_file = join(
                data_home,
                self.version + '.pot'
                )
        self.data = {
                'version': self.version,
                'food': 0,
                'data': []
                }

        if not isdir(self.data_home):
            os.makedirs(self.data_home, mode=0o700)

        try:
            with open(self.data_file, 'rb') as f:
                try:
                    self.data = json.loads(f.read())
                    reset_content = False
                except json.decoder.JSONDecodeError:
                    reset_content = True

        except FileNotFoundError:
            reset_content = True

        if reset_content:
            self.save()

    def save(self):
        with open(self.data_file, 'wb') as f:
            f.write(json.dumps(self.data).encode('utf8'))

    def feed(self):
        if 'food' not in self.data:
            self.data['food'] = 0

        self.data['food'] += 1
        self.tick()

    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def render(self):
        pass
