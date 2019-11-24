import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Calculator")
        self.resize(300, 300)
        self.move(300, 300)
        self.label = QLabel("0")
        self.edit = QLineEdit("0")
        self.edit2 = QLineEdit("0")
        self.button = QPushButton("+")
        self.button2 = QPushButton("-")
        self.button3 = QPushButton("*")
        self.button4 = QPushButton("/")
        self.button5 = QPushButton("Clear")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.edit)
        layout.addWidget(self.edit2)
        layout.addWidget(self.button)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        self.setLayout(layout)
        self.button.clicked.connect(self.plus)
        self.button2.clicked.connect(self.minus)
        self.button3.clicked.connect(self.multiplication)
        self.button4.clicked.connect(self.division)
        self.button5.clicked.connect(self.clear)
    def clear(self):
        self.label.setText("{}".format(0))
    def plus(self):
        n1=int(self.edit.text())
        n2=int(self.edit2.text())
        n3=int(self.label.text())
        if n3==0:
            self.label.setText("{}".format(n1 + n2))
        else:
            self.label.setText("{}".format(n1 + n2 + n3))
    def minus(self):
        n1=int(self.edit.text())
        n2=int(self.edit2.text())
        n3 = int(self.label.text())
        if n3==0:
            self.label.setText("{}".format(n1 - n2))
        else:
            self.label.setText("{}".format(n3-n1-n2))
    def multiplication(self):
        n1=int(self.edit.text())
        n2=int(self.edit2.text())
        n3 = int(self.label.text())
        if n3==0:
            self.label.setText("{}".format(n1 * n2))
        else:
            self.label.setText("{}".format(n3*n1*n2))
    def division(self):
        n1=int(self.edit.text())
        n2=int(self.edit2.text())
        n3 = int(self.label.text())
        if n3==0:
            self.label.setText("{}".format(n1 / n2))
        else:
            self.label.setText("{}".format(n3/n1/n2))


if __name__ == '__main__':
    app = QApplication()
    form = Form()
    form.show()
    sys.exit(app.exec_())




