import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QLineEdit, QPushButton,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QHBoxLayout, QVBoxLayout, QWidget,
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.tf = True
        self.text = 'Нажмите Enter!'
        self.setWindowTitle("My App")
        self.resize(300, 300)

        layout = QHBoxLayout()

        widget0 = QLabel("Введите число, ")
        font = widget0.font()
        font.setPointSize(20)
        widget0.setFont(font)
        widget0.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        widget1 = QLabel("нажмите Enter")
        font = widget1.font()
        font.setPointSize(20)
        widget1.setFont(font)
        widget1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.widget2 = QLineEdit()
        self.widget2.setMaxLength(10)

        # widget.setReadOnly(True)

        self.widget2.returnPressed.connect(self.return_pressed)
        self.widget2.selectionChanged.connect(self.selection_changed)
        self.widget2.textChanged.connect(self.text_changed)
        self.widget2.textEdited.connect(self.text_edited)
        self.widget2.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        button = QPushButton("Результат!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        self.label_result = QLabel()

        widgets = [widget0, widget1, self.widget2, button, self.label_result]
        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed!")
        self.text = self.widget2.text()

    def selection_changed(self):
        print("Selection changed")

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)

    def the_button_was_clicked(self):
        print("Clicked!")
        self.label_result.setText(self.text)
        if self.tf:
            self.setWindowTitle('Result')
            self.tf = False
        else:
            self.tf = True
            self.setWindowTitle('MyApp')


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()