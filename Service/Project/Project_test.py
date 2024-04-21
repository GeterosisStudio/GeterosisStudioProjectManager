import unittest

from Project import Project

class ProjectTest(unittest.TestCase):
    def setUp(self) -> None:
        self.project = Project()

    def init_project(self):
        self.project.init_proj("D:/Projects/")
        self.project.get_project_struct()
        self.project.create_asset_object("animation/scenes/e0010/e0010s0000d0000v0000/")
        self.project.create_assets_in_folder("animation/scenes/e0010/")
        asset = self.project.get_asset_from_path("D:/Projects/animation/scenes/e0010/e0010s0000d0000v0000/")
        item = asset.get_asset_item(0, 0)

