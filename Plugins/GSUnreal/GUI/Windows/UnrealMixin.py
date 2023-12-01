import unreal
import sys
from PySide6.QtWidgets import QApplication

# This function will be called when the application is closing.
def __QtAppQuit__():
	unreal.unregister_slate_post_tick_callback(tick_handle)

# This function is called by the windows when they are closing. (Only if the connection is properly made.)
def __QtWindowClosed__(window=None):
	if window in opened_windows:
		opened_windows.remove(window)

# This part is for the initial setup. Need to run once to spawn the application.
unreal_app = QApplication.instance()
if not unreal_app:
	unreal_app = QApplication(sys.argv)
	unreal_app.aboutToQuit.connect(__QtAppQuit__)
	existing_windows = {}
	opened_windows = []


# desired_window_class: class QtGui.QWidget : The window class you want to spawn
# return: The new or existing window
def spawnQtWindow(desired_window_class=None):
	window = existing_windows.get(desired_window_class, None)
	if not window:
		window = desired_window_class()
		existing_windows[desired_window_class] = window
		window.aboutToClose = __QtWindowClosed__
	if window not in opened_windows:
		opened_windows.append(window)
	window.show()
	window.activateWindow()
	return window


"""
import GSUnreal.GUI.Windows.MainUnrealWindow.MainUnrealWindow as MainWindow
from GSUnreal.GUI.Windows import UnrealMixin
UnrealMixin.spawnQtWindow(MainWindow.MainUnrealWindow)
"""