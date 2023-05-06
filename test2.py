from PyQt5.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem
import os


def create_tree_widget(parent, dir_data):
    for key, value in dir_data.items():
        item = QTreeWidgetItem(parent, [key])
        if isinstance(value, dict):
            create_tree_widget(item, value)
        elif isinstance(value, list):
            for item_value in value:
                QTreeWidgetItem(item, [str(item_value)])
        else:
            QTreeWidgetItem(item, [str(value)])


def create_dir_data(dir_path):
    data = {
        'assets': [i for i in os.listdir(os.path.join(dir_path, 'assets')) if os.path.isdir(os.path.join(dir_path, 'assets', i))],
        'animation': {

            'scenes': [i for i in os.listdir(os.path.join(dir_path, 'animation', 'scenes')) if os.path.isdir(os.path.join(dir_path, 'animation', 'scenes', i))],
            'movement': [i for i in os.listdir(os.path.join(dir_path, 'animation', 'movement')) if os.path.isdir(os.path.join(dir_path, 'animation', 'movement', i))],
        },
        'logicmaps': {

            'scenes': list(os.listdir(os.path.join(dir_path, 'logicmaps', 'scenes'))),
            'gameplay': list(os.listdir(os.path.join(dir_path, 'logicmaps', 'gameplay')))
        }
    }
    return data


data = create_dir_data("E:/Projects/ILLUSION_1")
app = QApplication([])
tree = QTreeWidget()
create_tree_widget(tree, create_dir_data("E:/Projects/ILLUSION_1"))
tree.show()
app.exec_()
