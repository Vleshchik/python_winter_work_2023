xyz = 1_000_000
print(xyz)
#x y z = 1000 2000 3000
#print(x y z)
x,y,z = 1000, 2000, 3000
print(x,y,z)
x_y_z = 1_000_000
print(x_y_z)
#2
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys
#app = QApplication([])
#window = QPushButton('PUSH ME')

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('My App')
        self.resize(400, 400)
        self.setWindowOpacity(0.9)
        self.button = QPushButton('Press me!')
        #print(button.text())
        #button.setCheckable(True)
        self.button.clicked.connect((self.the_button_was_clicked))
        self.setCentralWidget(self.button)
    def the_button_was_clicked(self):
        print('Clicked!')
        self.button.setText("Y have already clicked me.")
        self.button.setEnabled(False)
        self.setWindowTitle('My One shoot app')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()