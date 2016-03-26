import json


class BaseResponse:
    def __init__(self, json_str):
        self._json = json.loads(json_str, encoding='utf-8')
        pass

    def decode(self):
        self.__dict__.update(self._json)

    def pop(self, key, default=None):
        """

        Parameters
        ----------
        key : str
        default : object
        """
        return self._json.pop(key, default)
