# Singleton pattern implementation in Python
# Goal: create no more than one instance of a class and provide a global point of access to it.

class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance
    
    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception('This class is a singleton!')
        else:
            Singleton.__instance = self
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance