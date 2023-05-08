class Asset(object):
    def __init__(self, project_path, asset_type, asset_name):
        self.project_path = project_path
        self.asset_type = asset_type
        self.asset_name = asset_name

    def print_info(self):
        print (self.project_path, self.asset_name, self.asset_type)

class Ass(Asset):
    def sas(self):
        print("qwe")


asset = Ass("E:/path", "AnimScene", "e0010s1101d0100v0010")

asset.sas()
