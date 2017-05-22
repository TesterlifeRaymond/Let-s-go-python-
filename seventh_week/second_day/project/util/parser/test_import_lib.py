"""
@ Version : ??
@ Author  : liujinjia
@ File    : test_import_lib.py
@ Project : Let-s-go-python-
@ Create Time: 2017-05-23 06:20
"""


class ObjectDict(dict):
    """object view of dict, you can
    >>> a = ObjectDict()
    >>> a.fish = 'fish'
    >>> a['fish']
    'fish'
    >>> a['water'] = 'water'
    >>> a.water
    'water'
    >>> a.test = {'value': 1}
    >>> a.test2 = ObjectDict({'name': 'test2', 'value': 2})
    >>> a.test, a.test2.name, a.test2.value
    (1, 'test2', 2)
    """
    def __init__(self, initd=None):
        """ ObjectDict init function """
        if initd is None:
            initd = {}
        dict.__init__(self, initd)

    def __getattr__(self, item):
        """ObjectDict getattr function """
        _dict = self.__getitem__(item)
        # if value is the only key in object, you can omit it
        if isinstance(_dict, dict) and 'value' in _dict and len(_dict) == 1:
            return _dict['value']
        return _dict

    def __setattr__(self, item, value):
        """ObjectDict setattr function """
        self.__setitem__(item, value)
