from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys
from random import choice
#app = QApplication([])
#window = QPushButton('PUSH ME')
window_titles = ['My App', 'Still My App', 'Still My App', 'What on Earth',
                 'What on Earth', 'This is surprising!', 'This is surprising!',
                 'Something went wrong']
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.n_times_clicked = 0
        self.setWindowTitle('My App')
        self.resize(400, 400)
        self.setWindowOpacity(0.9)
        self.button = QPushButton('Press me!')
        #print(button.text())
        #button.setCheckable(True)
        self.button.clicked.connect((self.the_button_was_clicked))
        self.windowTitleChanged.connect(self.the_window_title_changed)
        self.setCentralWidget(self.button)
    def the_button_was_clicked(self):
        print('Clicked!')
        new_win_title = choice(window_titles)
        print("Setting title: %s" % new_win_title)
        self.setWindowTitle(new_win_title)
    def the_window_title_changed(self, window_title):
        print('Window title changed: %s' % window_title)
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()