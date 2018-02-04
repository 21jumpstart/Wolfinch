'''
 OldMonk Auto trading Bot
 Desc: Market Indicator Abstract Class Implementation
 (c) Joshith Rayaroth Koderi
'''
from abc import ABCMeta, abstractmethod

class Indicator:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__ (self):
        ''' 
        Init for the strategy class
        '''
        pass
    
    def __str__ (self):
        return "{Message: Indicator Abstract Class}"

    def configure (self):
        pass
    
    @abstractmethod
    def calculate (self):
        pass
    