import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton, QDoubleSpinBox
from PyQt5.QtCore import Qt
import math

class FunctionCalculator(QWidget):
    def __init__(self):
        super(FunctionCalculator, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('lab1')

        self.function_label = QLabel('Choose a function:')
        self.function_radio1 = QRadioButton('y = 4^x - 10 * 2^(x-1) - 24')
        self.function_radio2 = QRadioButton('y = 1 - 1/(1 - arcsin(2x + 3π/2))')

        self.point_label = QLabel('Enter a point:')
        self.point_spinbox = QDoubleSpinBox()
        self.point_spinbox.setDecimals(2)

        self.calculate_button = QPushButton('Calculate')
        self.calculate_button.clicked.connect(self.calculate_function)

        self.result_label = QLabel('Result:')

        # Layout setup
        layout = QVBoxLayout()

        function_layout = QVBoxLayout()
        function_layout.addWidget(self.function_label)
        function_layout.addWidget(self.function_radio1)
        function_layout.addWidget(self.function_radio2)

        point_layout = QHBoxLayout()
        point_layout.addWidget(self.point_label)
        point_layout.addWidget(self.point_spinbox)

        layout.addLayout(function_layout)
        layout.addLayout(point_layout)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_function(self):
        point = self.point_spinbox.value()

        if self.function_radio1.isChecked():
            result = f'y = 4^{point} - 10 * 2^({point}-1) - 24 = {math.pow(4, point) - 10 * math.pow(2, point-1) - 24}'
        elif self.function_radio2.isChecked():
            result = f'y = 1 - 1/(1 - arcsin(2*{point} + 3π/2)) = {1 - 1/(1 - math.asin(2*point + 3*math.pi/2))}'
        else:
            result = 'Please select a function'

        self.result_label.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = FunctionCalculator()
    calculator.show()
    sys.exit(app.exec_())
