from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem

from views import user_info_ui


class User(QtWidgets.QWidget, user_info_ui.Ui_UserInfo):
    pass
