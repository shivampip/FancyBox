name= 'FancyBox'

from .box import Box 
from .message import *


import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

#import codecs
#codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)