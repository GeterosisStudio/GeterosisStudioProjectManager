import sys
import os
import json
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QWidget, QMenu
from PySide6 import QtUiTools, QtCore, QtGui
from PySide6.QtGui import QIcon
from Core import Icons
from Service.Network import Client

class ProjectWindow(QMainWindow):
    def __init__(self, project_path=None):
        super(ProjectWindow, self).__init__()
        self.project_info = ""
        if project_path:
            self.load_project_info(project_path)
            self.setWindowTitle('GSPM Editor: ' + self.project_info["name"])
        self.ui = QtUiTools.QUiLoader().load(__file__.replace('.py', '.ui'))
        self.setCentralWidget(self.ui)
        self.project_root = self.get_project_root()
        self.project_struct = self.get_project_struct()
        self.project_config = self.get_config()

        self.setWindowIcon(QIcon(self.get_project_icon()))

        self.ui.project_tree_widget.itemDoubleClicked.connect\
            (lambda:self.load_asset_tab_widget(self.ui.project_tree_widget.currentItem()))
        self.tree_widget_context_menu = QMenu()
        self.tree_widget_context_menu.addAction("Open location.", self.tree_widget_item_open_loaction)

        self.ui.project_tree_widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.project_tree_widget.customContextMenuRequested.connect(self.show_tree_widget_context_menu)

        self.node_icon = QtGui.QIcon(Icons.get_icon_path_from_name("node.png"))


        self.ui.splitter.setSizes([2, 5, 2])

        self.ui.asset_tab_widget.tabCloseRequested.connect(lambda index: self.close_asset_tab_widget_item(index))
        self.ui.asset_tab_widget.currentChanged.connect(self.current_tab_changed)

        #ui setup
        self.load_data()
        self.load_window_config()


    def load_window_config(self):
        self.resize(self.project_config["Project browser"]["weight"], self.project_config["Project browser"]["height"])
        self.move(self.project_config["Project browser"]["horizontal"],
                  self.project_config["Project browser"]["vertical"])

    def get_project_icon(self):
        if self.project_info["image"]:
            return self.project_root + self.project_info["image"]


    def get_config(self):
        with open(self.project_root + "settings/EditorConfigs.json") as config:
            return json.load(config)

    def save_config(self, data):
        with open(self.project_root + "settings/Configs.json", "w") as config:
            json.dump(data, config, indent=4)

    def closeEvent(self, event):
        self.project_config["Project browser"]["weight"] = self.size().width()
        self.project_config["Project browser"]["height"] = self.size().height()
        self.project_config["Project browser"]["horizontal"] = self.pos().x()
        self.project_config["Project browser"]["vertical"] = self.pos().y()
        self.save_config(self.project_config)

        event.accept()



    def load_project_info(self, projrct_file):
        print(projrct_file)
        with open(projrct_file) as f:
            self.project_info = json.load(f)


    def get_project_root(self):
        return self.project_info["prod_path"]

    def get_project_struct(self):
        with open(self.project_root + "settings/FileSystem.json") as f:
            return json.load(f)

    def load_data(self):
        self.load_project_tree_widget()
        #self.load_asset_tab_widget()

    def load_project_tree_widget(self):
        for i in self.project_struct:
            self.create_project_tree_widget_item(self.project_struct[i])

    def load_asset_tab_widget(self, item):
        if not self.get_tree_widget_item_data(item, 1):
            return False
        print(self.get_tree_widget_item_data(item, 0))
        for tab in range(self.ui.asset_tab_widget.count()):
            if self.ui.asset_tab_widget.widget(tab).property("item") == item:
                self.ui.asset_tab_widget.setCurrentIndex(tab)
                return True

        tab_widget = self.ui.asset_tab_widget.addTab(QWidget(), item.text(0))
        self.ui.asset_tab_widget.widget(tab_widget).setProperty("item", item)
        self.ui.asset_tab_widget.setCurrentIndex(tab_widget)


    def current_tab_changed(self, index):
        item = self.ui.asset_tab_widget.widget(index).property("item")
        self.ui.project_tree_widget.setCurrentItem(item)

    def update_project_tree_widget(self):
        pass


    def update_asset_tab_widget(self, tab_widget):
        tab_widget = None

    def create_project_tree_widget_item(self, item_dict, parent_item = None):
        item = QTreeWidgetItem()
        item.setText(0, item_dict['name'])
        if not parent_item:
            self.ui.project_tree_widget.addTopLevelItem(item)
        else:
            parent_item.addChild(item)

        if item_dict['folders']:
            for i in item_dict['folders']:
                self.create_project_tree_widget_item(item_dict['folders'][i], item)

        if item_dict['asset'] and item_dict['asset']['foldercount'] > 0:
            self.add_asset_subfolder_items(item, self.project_root + item_dict['localpath'],
                                           item_dict['asset']['foldercount'], item_dict['asset'])

        elif item_dict['asset']:
            item_path = self.project_root + item_dict['localpath'] + "/"
            item.setData(0, QtCore.Qt.UserRole, item_path)
            item.setData(1, QtCore.Qt.UserRole, item_dict['asset'])
            item.setIcon(0, self.node_icon)
            return True

        item_path = self.project_root + item_dict['localpath'] + "/"
        item.setData(0, QtCore.Qt.UserRole, item_path)




    def add_asset_subfolder_items(self, parent_item, path, depth, asset):
        count = depth - 1
        listdir = [fname for fname in os.listdir(path) if os.path.isdir("/".join([path, fname]))]
        if count <= 0:
            for i in listdir:
                item = QTreeWidgetItem()
                item.setText(0, i)
                item_path = path + i + "/"
                item.setData(0, QtCore.Qt.UserRole, item_path)
                item.setData(1, QtCore.Qt.UserRole, asset)
                item.setIcon(0, self.node_icon)
                parent_item.addChild(item)
        else:
            for i in listdir:
                item = QTreeWidgetItem()
                item.setText(0, i)
                parent_item.addChild(item)
                self.add_asset_subfolder_items(item, "/".join([path, i]), count)

    def close_asset_tab_widget_item(self, index):
        self.ui.asset_tab_widget.removeTab(index)

    def get_tree_widget_item_data(self, item, data_index=0):
        if item.data(data_index, QtCore.Qt.UserRole):
            return item.data(data_index, QtCore.Qt.UserRole)
        else:
            return False

    def tree_widget_item_open_loaction(self):
        item = self.ui.project_tree_widget.currentItem()
        self.open_location(self.get_tree_widget_item_data(item))

    def open_location(self, path):
        path = path
        path = os.path.realpath(path)
        os.startfile(path)

    def show_tree_widget_context_menu(self, event):
        self.tree_widget_context_menu.exec(self.ui.project_tree_widget.mapToGlobal(event))

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication()
    window = ProjectWindow("default_project/default.gsproj")
    window.show()
    sys.exit(app.exec())
