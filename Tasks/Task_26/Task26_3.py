from PyQt6.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit
from PyQt6.QtGui import QAction
import sys

class MDIWindow(QMainWindow):
    count = 0
    def __init__(self):
        super().__init__()
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu("Меню")
        file.addAction("Описание")
        file.addAction("Инструкция")
        file.addAction("Помощь")
        self.setWindowTitle("Task 26.3")


app = QApplication(sys.argv)
mdiwindow = MDIWindow()
mdiwindow.show()
app.exec()
