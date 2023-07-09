#1
demo_l = [5,4,4,6,8,12,12,1,5]
l = []
l2 = []
for i in demo_l:
    if i not in l:
        l.append(i)
        if demo_l.count(i) > 1:
            l2.append(i)
print(l)
print(l2)
#2
from collections import Counter
demo_l = [5,4,4,6,8,12,12,1,5]
c = Counter(demo_l)
print(c)
#3
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QTextEdit
)
from PyQt6.QtGui import QIcon, QAction

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        exitAction = QAction(QIcon('groggu.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300,300,350,250)
        self.setWindowTitle('Main window')
        self.show()
if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
#4
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QTextEdit, QWidget, QPushButton
)
from PyQt6.QtGui import QIcon, QAction

class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle('Window1')
        self.setMinimumWidth(200)
        self.setMinimumHeight(50)
        self.setGeometry(200,200,350,250)
        self.button = QPushButton(self)
        self.button.setText('Ok')
        self.button.show()

class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Window2')
        self.setMinimumWidth(200)
        self.setMinimumHeight(50)
        self.setGeometry(200,200,350,250)
        self.button = QPushButton(self)
        self.button.setText('KO')
        self.button.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Main Window')
        self.setGeometry(100,100,350,250)

    def show_window_1(self):
        self.w1 = Window1()
        self.w1.button.clicked.connect(self.show_window_2)
        self.w1.button.clicked.connect(self.w1.close)
        self.w1.show()

    def show_window_2(self):
        self.w2 = Window2()
        self.w2.button.clicked.connect(self.show_window_1)
        self.w2.button.clicked.connect(self.w2.close)
        self.w2.show()


if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    w.show_window_1()
    sys.exit(app.exec())
#5
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QTextEdit, QWidget, QPushButton, QMdiArea, QMdiSubWindow
)
from PyQt6.QtGui import QIcon, QAction

class MDIWindow(QMainWindow):
    count = 0
    def __init__(self):
        super().__init__()
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu('File')
        file.addAction('New')
        file.addAction('Cascade')
        file.addAction('Tiled')
        file.triggered[QAction].connect(self.WindowTrig)
        self.setWindowTitle('MDI Application')

    def WindowTrig(self, p):
        if p.text() == 'New':
            MDIWindow.count = MDIWindow.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle('Sub' + str(MDIWindow.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        if p.text() == 'Cascade':
            self.mdi.cascadeSubWindows()
        if p.text() == 'Tiled':
            self.mdi.tileSubWindows()

app = QApplication(sys.argv)
mdiwindow = MDIWindow()
mdiwindow.show()
app.exec()
#6
class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1
    def set_age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print('Недопустимый возраст')
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name
    def display_info(self):
        print(f'Имя: {self.__name}\tВозраст: {self.__age}')
tom = Person('Tom')
#tom.display_info()
tom.set_age(25)
tom.display_info()
#print(tom.__name)
print(tom._Person__name)
#7
