import json


def load_projects():
    with open(__file__.replace("Settings.py", "Configs/Projects.json")) as projects:
        return json.load(projects)
