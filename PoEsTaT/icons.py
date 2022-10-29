from . import DATADIR as _DATADIR
from .standardtypes import Singleton as _Singleton

class IconLib(_Singleton):
    def __init__(self):
        pass

class Icon(object):
    def __init__(self, name, filename):
        self.name = name
        self.file = filename
        self.dat = self.loadKnown(filename)

    def loadKnown(self, filename):
        """
        load a filename, return opened data
        :return: image object
        """
        pass