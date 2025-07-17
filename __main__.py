"""_summary_"""

from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QLineEdit,
    QSpinBox,
    QMainWindow,
)
from PyQt6.QtCore import Qt
from logging import getLogger, basicConfig, INFO, Logger
from sys import argv
from random import choice, randint
from string import digits, ascii_lowercase, ascii_uppercase, punctuation


class PasswordGenApp(QMainWindow):
    """_summary_

    Args:
        CoreMainWindow (_type_): _description_
    """

    def __init__(self, logger: Logger, title: str):
        """_summary_

        Args:
            logger (Logger): _description_
            title (str): _description_
        """
        super().__init__()
        self.logger = logger

        self.setWindowTitle(title)

        self.output = ""

        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 16)
        self.spin_box.setValue(12)

        self.numbers = QCheckBox("Add numbers (0-9)")
        self.numbers.setChecked(True)
        self.lowercase = QCheckBox("Add lowercase letters (a-z)")
        self.lowercase.setChecked(True)
        self.uppercase = QCheckBox("Add uppercase letters (A-Z)")
        self.uppercase.setChecked(True)
        self.specials = QCheckBox(
            "Add special characters (~ ! @ # $ % ^ & * ( ) - _ = + [ ] { } ; : , . < > / ? |)"
        )

        options_layout = QVBoxLayout()

        options_layout.addWidget(self.spin_box)
        options_layout.addWidget(self.numbers)
        options_layout.addWidget(self.lowercase)
        options_layout.addWidget(self.uppercase)
        options_layout.addWidget(self.specials)

        self.gen_button = QPushButton("Generate")
        self.gen_button.clicked.connect(self.generate)

        self.label = QLineEdit()
        self.label.setReadOnly(True)
        result_layout = QVBoxLayout()
        result_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        result_layout.addWidget(self.gen_button)
        result_layout.addWidget(self.label)

        layout = QVBoxLayout()
        layout.addLayout(options_layout)
        layout.addLayout(result_layout)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.show()

    def generate(self):
        """_summary_"""
        self.pool = []
        if self.numbers.isChecked():
            self.pool.append(digits)
        if self.lowercase.isChecked():
            self.pool.append(ascii_lowercase)
        if self.uppercase.isChecked():
            self.pool.append(ascii_uppercase)
        if self.specials.isChecked():
            self.pool.append(punctuation)

        if len(self.pool) != 0:
            for _ in range(0, self.spin_box.value()):
                self.output += str(choice(self.pool[randint(0, len(self.pool) - 1)]))

        self.label.setText(self.output)
        self.output = ""


app = QApplication(argv)

logger = getLogger(__name__)
basicConfig(filename="app.log", level=INFO)

window = PasswordGenApp(logger=logger, title="Password Generator")

app.exec()
