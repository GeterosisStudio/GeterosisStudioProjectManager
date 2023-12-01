import copy
import random
import time

colors = {
    "PURPLE": '\033[95m',
    "INDIGO": '\033[94m',
    "BLUE": '\033[96m',
    "GREEN": '\033[92m',
    "YELLOW": '\033[93m',
    "RED": '\033[91m',
    "GREY": '\033[0m',
    "WHITE": '\033[1m'
}




scene_item = {
    "input": {
        "active": True,
        "color": "GREEN"
    },
    "output": {
        "active": True,
        "color": "GREEN"
    },
    "element": {
        "color": "PURPLE",
        "item_menu": "url to menu",
    }
}


def asset_vizualize(asset):
    printed = ""
    for elem in asset:
        if isinstance(elem, list):
            for el in elem:
                printed += item_setup(el) + "   "
        else:
            printed += item_setup(elem) + "   "
    return printed


def item_setup(item):
    returned = ""
    if item["input"]["active"] == True:
        elem = colors[item["input"]["color"]] + "●" + " "
        returned += elem

    elem = colors[item["element"]["color"]] + "████████"
    returned += elem

    if item["output"]["active"] == True:
        elem = " " + colors[item["output"]["color"]] + "●"
        returned += elem
    return returned


def generate_asset():
    asset = []

    asset_dafault_item = {
        "input": {
            "active": True,
            "color": "GREEN"
        },
        "output": {
            "active": True,
            "color": "GREEN"
        },
        "element": {
            "color": "PURPLE",
            "item_menu": "url to menu",
        }
    }

    input = copy.deepcopy(asset_dafault_item)
    input["input"]["active"] = False
    color = random.choice(list(colors.items()))[0]
    input["element"]["color"] = color
    color = random.choice(list(colors.items()))[0]
    input["output"]["color"] = color

    output = copy.deepcopy(asset_dafault_item)
    output["output"]["active"] = False
    color = random.choice(list(colors.items()))[0]
    output["element"]["color"] = color
    color = random.choice(list(colors.items()))[0]
    output["input"]["color"] = color



    asset.append(input)
    for i in range(18):
        asset_item = copy.deepcopy(asset_dafault_item)
        color = random.choice(list(colors.items()))[0]
        asset_item["element"]["color"] = color
        color = random.choice(list(colors.items()))[0]
        asset_item["input"]["color"] = color
        color = random.choice(list(colors.items()))[0]
        asset_item["output"]["color"] = color

        asset.append(asset_item)

    asset.append(output)

    return asset



for i in range(200):
    print( str(i) + "\t" + asset_vizualize(generate_asset()))
    time.sleep(random.uniform(0.2, 1.0))





