"""Singleton pattern"""

import threading

class SingletonMeta(type):
  """Custom metaclass"""

  def __init__(self, *args, **kwargs):
    self.__instance = None
    self.__lock = threading.RLock()
    super().__init__(*args, **kwargs)

  def __call__(self, *args, **kwargs):
    if self.__instance is None:
      with self.__lock:
        if self.__instance is None:
          self.__instance = super().__call__(*args, **kwargs)
    return self.__instance

class President(metaclass=SingletonMeta):
  """President (singleton class)"""
  pass
