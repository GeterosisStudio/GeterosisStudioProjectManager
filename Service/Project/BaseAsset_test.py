import os
import unittest

from BaseAsset import BaseAsset
from Settings import Settings


class BaseAssetTest(unittest.TestCase):
    def setUp(self) -> None:
        self.asset = BaseAsset()

    def test_load_tmplate_dict(self):
        tmplate = {
            "assettype": "TestAsset",
            "assetname": "Default Asset",
            "assetclass": "BaseAsset",
            "items": {
                "0": {
                    "0": {
                        "name": "GSMontage",
                        "itempath": "default"
                    }
                }
            }
        }
        self.assertEqual(self.asset.load_asset_tmplate(tmplate), True)

    def test_load_tmplate_file(self):
        default_asset_path = Settings.get_default_assets_path()
        default_assets = [i for i in os.listdir(default_asset_path) if '.json' in i]
        for i in default_assets:
            self.assertEqual(self.asset.load_asset_tmplate(default_asset_path + i), True)

if __name__ == '__main__':
    unittest.main()