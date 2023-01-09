import sys
from PyQt5.QtWidgets import QApplication
import presenter
import Model

class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = presenter.Presenter()
        return cls.instance 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    presenter = Singleton()
    app.exec_()
    