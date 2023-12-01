import json


def load_projects():
    with open(__file__.replace("Settings.py", "Configs/Projects.json")) as projects:
        return json.load(projects)


def save_projects(data):
    path = __file__.replace("Settings.py", "Configs/Projects.json")
    with open(path, "w") as config:
        json.dump(data, config, indent=4)


def get_config():
    with open(__file__.replace("Settings.py", "Configs/Configs.json")) as config:
        return json.load(config)


def save_config(data):
    path = __file__.replace("Settings.py", "Configs/Configs.json")
    with open(path, "w") as config:
        json.dump(data, config, indent=4)
