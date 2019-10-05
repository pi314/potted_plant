from .model import AbstractPlant
from os.path import join, exists, isfile


'''
Data format:
{
    'version': 'plant1',
    'food': 0,
    'data': [
        {'color': 2},  // 2, 12, 3, 13
        [
            {'size': 18, 'color': 12},
            ...
        ],
        {'size': 18, 'color': 12},
        {'size': 18, 'color': 12},
        {'size': 18, 'color': 12},
    ],
}
'''


class Plant1(AbstractPlant):
    def __init__(self, data_home):
        super().__init__(data_home)

    def tick(self):
        pass

    def render(self):
        pass
