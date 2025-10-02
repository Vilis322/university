class MyDict:
    def __init__(self):
        self._my_dict = []

    def __getitem__(self, key):
        for k, v in self._my_dict:
            if k == key:
                return v
        return None

    def __setitem__(self, key, value):
        for i, (k, v) in enumerate(self._my_dict):
            if k == key:
                self._my_dict[i] = (k, value)
                return
        self._my_dict.append((key, value))

    def __delitem__(self, key):
        for i, (k, v) in enumerate(self._my_dict):
            if k == key:
                del self._my_dict[i]
                return

    def __contains__(self, key):
        for k, v in self._my_dict:
            if k == key:
                return True
        return False

    def keys(self):
        return [k for k, v in self._my_dict]

    def values(self):
        return [v for k, v in self._my_dict]

    def items(self):
        return [(k, v) for k, v in self._my_dict]

    def __str__(self):
        return "{" + ", ".join(f"{k}: {v}" for k, v in self._my_dict) + "}"


if __name__ == "__main__":
    my_dict = MyDict()
    my_dict['name'] = 'Alice'
    my_dict['age'] = 30
    print(my_dict['name'])
    print('city' in my_dict)
    del my_dict['age']
    print(my_dict.keys())
    print(my_dict.values())
