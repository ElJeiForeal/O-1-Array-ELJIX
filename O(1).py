# made by GPT ( i was too lazy )
class JICT:
    @staticmethod
    def Convert(obj):
        if isinstance(obj, (tuple, int, float, str, bool, type(None))):
            return obj
        elif isinstance(obj, list):
            return tuple(JICT.Convert(e) for e in obj)
        elif isinstance(obj, set):
            return tuple(sorted(JICT.Convert(e) for e in obj))
        elif isinstance(obj, dict):
            return tuple(sorted((JICT.Convert(k), JICT.Convert(v)) for k, v in obj.items()))
        else:
            return id(obj)

    def __new__(cls, obj):
        # When you call JICT(obj), it returns the converted tuple form directly
        return JICT.Convert(obj)
#

#Made by me
class ELJIX():
    def __init__(self):
        self.__key_to_value = {}
        self.__value_to_keys = {}
        self.__AllKeys = set()
    
    def __getitem__(self, key):
        if key not in self.__key_to_value:
            raise ValueError(f"Invalid key of {key}")

        return self.__key_to_value[key]

    def __setitem__(self, key, value):
        self.add(key, value)
    
    def __delitem__(self, key):
        self.remove(key)
    
    def __contains__(self, key):
        return key in self.__AllKeys

    def __iter__(self):
        return iter(self.__key_to_value)

    def add(self, key, value):
        if key in self.__key_to_value:
            self.remove(key)


        self.__key_to_value[key] = value

        if value not in self.__value_to_keys:
            self.__value_to_keys[value] = set()

        self.__value_to_keys[value].add(key)
        self.__AllKeys.add(key)

    def index(self, value):
        if value not in self.__value_to_keys: return None

        return self.__value_to_keys[value]

    def remove(self, key):
        if key not in self.__key_to_value: raise ValueError(f"Invalid key of {key}")

        char = self[key] 

        del self.__key_to_value[key]
        self.__value_to_keys[char].remove(key)
        self.__AllKeys.remove(key)

        if len(self.__value_to_keys[char]) == 0:
            del self.__value_to_keys[char]

    @property
    def Length(self):
        return len(self.__key_to_value)

    @property
    def Keys(self):
        return self.__AllKeys
    
    @property
    def items(self):
        return self.__key_to_value.items()

    def clear(self):
        self.__key_to_value = {}
        self.__value_to_keys = {}
        self.__AllKeys = set()
        self.__Length = 0

    def copy(self):
        new_obj = ELJIX()
        new_obj.__key_to_value = self.__key_to_value.copy()
        new_obj.__value_to_keys = {k: v.copy() for k, v in self.__value_to_keys.items()}
        new_obj.__AllKeys = self.__AllKeys.copy()
        return new_obj


    def get(self, key, default=None):
        if key in self.__key_to_value:
            return self.__key_to_value[key]
        return default

    def setdefault(self, key, default):
        if key in self.__key_to_value:
            return self.__key_to_value[key]
        self.add(key, default)
        return default
    
    @classmethod
    def fromkeys(cls, iterable, value=None):
        new_obj = cls()
        for key in iterable:
            new_obj.add(key, value)
        return new_obj


    def __repr__(self):
        return str(self.__key_to_value)   
#