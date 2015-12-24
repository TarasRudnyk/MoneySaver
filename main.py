import sys
from PyQt5.QtWidgets import QApplication
import authorization_form


class Window(authorization_form.Authorization):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.validate_auth_data)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
