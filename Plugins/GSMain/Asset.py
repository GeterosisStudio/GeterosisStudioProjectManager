import os
import json


class Asset:
    def __init__(self, file_path=None):
        self.__file = ""
        self.__path = ""
        self.__data = {}
        self.__items = []

        if file_path and os.path.isfile(file_path):
            self.load_asset_file(file_path)



    def create(self):
        pass

    def load_asset_file(self, file_path):
        self.__file = ""
        self.__path = ""
        with open('strings.json') as f:
            self.set_data(json.load(f))
        self.__items = self.__data["items"]

    def set_file(self, file_path):
        pass

    def get_file(self):
        return self.__file

    def set_path(self, asset_path):
        pass

    def get_path(self):
        return self.__path

    def set_data(self, data):
        if isinstance(data, dict):
            self.__data = data
        else:
            raise ValueError

    def get_data(self):
        return self.__data

    def set_items(self, data):
        if isinstance(data, list):
            self.__items = data
        else:
            raise ValueError


if __name__ == "__main__":
    asset = Asset()
    asset.set_data({"asd": "aaa"})
    print(asset.get_data())
