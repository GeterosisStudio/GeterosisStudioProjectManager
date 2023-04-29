class Project:
    def __init__(self):
        self.project_hash = None
        self.project_name = None
        self.project_path = None

    def set_project_hash(self, hash_str):
        self.project_hash = hash_str
        return True

    def get_project_hash(self):
        return self.project_hash

    def set_project_name(self, name):
        self.project_name = name
        return True

    def get_project_name(self):
        return self.project_name

    def set_project_path(self, path):
        self.project_path = path
        return True
