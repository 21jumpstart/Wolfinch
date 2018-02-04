'''
 OldMonk Auto trading Bot
 Desc: Market Strategy Abstract Class Implementation
 (c) Joshith Rayaroth Koderi
'''
from abc import ABCMeta, abstractmethod

class Strategy:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__ (self):
        ''' 
        Init for the strategy class
        '''
        pass
    
    def __str__ (self):
        return "{Message: TODO: FIXME: jork: implement}"

    def configure (self):
        pass
    
    @abstractmethod
    def generate_signal (self):
        '''
        Trade Signale in range(-5..0..5), ==> (strong sell .. 0 .. strong buy) 0 is neutral (hold) signal 
        '''
        return 0
        
    