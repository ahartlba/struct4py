class Struct:
    def __init__(self, allow_override: bool = True):
        self.__dict__["_storage"] = {}
        self.__dict__["_ao"] = allow_override

    def __getattr__(self, name):
        if name not in self._storage or not isinstance(self._storage[name], Struct):
            if self.__dict__["_ao"]:
                self._storage[name] = Struct(self.__dict__["_ao"])
        return self._storage[name]

    def __setattr__(self, name, value):
        self._storage[name] = value

    def __repr__(self):
        return repr(self._storage)

    def to_dict(self):
        """convert structure to a dictionary"""

        def convert(obj):
            if isinstance(obj, Struct):
                return {key: convert(value) for key, value in obj._storage.items()}
            return obj

        return convert(self)
