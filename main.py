import sys


import numpy as np

from sympy import symbols, Eq, solve
import vlc
from PyQt5.QtGui import QMovie



from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QComboBox, QLabel, QPushButton, QMessageBox, QInputDialog
from PyQt5.uic import loadUi

from decimal import Decimal, getcontext, InvalidOperation

import math



from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi



class FirstPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("page1.ui", self)

        self.pushButton.clicked.connect(self.next_page)


    def next_page(self):
        self.call_window = SecondPage()
        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)





class SecondPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("page2.ui", self)


        self.pushButton.clicked.connect(self.third_page_call_button)

        self.pushButton_2.clicked.connect(self.forth_page_call_button)



    def third_page_call_button(self):
        self.call_window = ThirdPage()
        widget.addWidget(self.call_window)

        widget.setCurrentIndex(widget.currentIndex() + 1)



    def forth_page_call_button(self):
        self.call_window = ForthPage()

        widget.addWidget(self.call_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)



from PyQt5.QtWidgets import QMainWindow, QMessageBox
import numpy as np
from PyQt5.uic import loadUi


class ThirdPage(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            loadUi("page3_i.ui", self)

            self.pushButton_2.clicked.connect(self.add_element)
            self.pushButton.clicked.connect(self.solve_button)
            self.label_4.setMouseTracking(True)
            self.label_4.enterEvent = self.mouseEntered
            self.label_4.leaveEvent = self.mouseLeft

            self.label_5.setVisible(False)
        except Exception as e:
            QMessageBox.critical(None, "Initialization Error", f"An error occurred during initialization.\n\nDetails: {e}")

    def give_proper_matrix(self, a):
        try:
            b = []
            for i in a:
                c = []
                d = i.split(',')
                for j in d:
                    c.append(float(j))
                b.append(c)
            return b
        except Exception as e:
            QMessageBox.critical(None, "Matrix Conversion Error", f"Invalid matrix format.\n\nDetails: {e}")
            return []

    def mouseEntered(self, event):
        try:
            self.label_5.setVisible(True)
            event.accept()
        except Exception as e:
            QMessageBox.critical(None, "Mouse Event Error", f"Error on mouse enter.\n\nDetails: {e}")

    def mouseLeft(self, event):
        try:
            self.label_5.setVisible(False)
            event.accept()
        except Exception as e:
            QMessageBox.critical(None, "Mouse Event Error", f"Error on mouse leave.\n\nDetails: {e}")

    def calulation(self, mat):
        try:
            value, vector = np.linalg.eig(mat)
            return value, vector
        except Exception as e:
            QMessageBox.critical(None, "Calculation Error", f"Failed to calculate eigenvalues and eigenvectors.\n\nDetails: {e}")
            return None, None

    def add_element(self):
        try:
            new_text = ', '.join(self.lineEdit.text().split())
            current_text = self.label_6.text()
            if current_text:
                updated_text = current_text + "\n" + new_text
            else:
                updated_text = new_text
            self.label_6.setText(updated_text)
            print(
                type(self.label_6.text().split("\n")),
                self.label_6.text().split("\n"),
                self.give_proper_matrix(self.label_6.text().split("\n"))
            )
        except Exception as e:
            QMessageBox.critical(None, "Add Element Error", f"Failed to add the element.\n\nDetails: {e}")

    def solve_button(self):
        try:
            matrix = self.give_proper_matrix(self.label_6.text().split("\n"))
            if not matrix:
                return

            mat = np.array(matrix)
            x, y = self.calulation(mat)
            if x is None or y is None:
                return

            print(f"{x[0]}\n{y[0]}")
            self.call_window = ThirdPageTwo(x, y)
            widget.addWidget(self.call_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        except Exception as e:
            QMessageBox.critical(None, "Solve Button Error", f"Error occurred while solving.\n\nDetails: {e}")


class ThirdPageTwo(QMainWindow):
    def __init__(self, eigen_value, eigen_vector):
        super().__init__()
        try:
            loadUi("page3_ii.ui", self)

            eigen_value_str = self.format_eigenvalues(eigen_value)
            eigen_vector_str = self.format_eigenvectors(eigen_vector)

            self.label_6.setText(eigen_value_str)
            self.label_7.setText(eigen_vector_str)
        except Exception as e:
            QMessageBox.critical(None, "Initialization Error", f"Error occurred during initialization.\n\nDetails: {e}")

    def format_eigenvalues(self, eigenvalues):
        try:
            def to_scientific(x):
                base, exp = f"{x:.3e}".split('e')
                return f"{float(base):.3f} × 10<sup>{int(exp)}</sup>"

            return ", ".join(to_scientific(val) for val in eigenvalues)
        except Exception as e:
            QMessageBox.critical(None, "Formatting Error", f"Error formatting eigenvalues.\n\nDetails: {e}")
            return "Error"

    def format_eigenvectors(self, eigenvectors):
        try:
            formatted_vectors = []

            for i, vec in enumerate(eigenvectors.T):
                formatted_vec = "(" + ", ".join(self.to_scientific(v) for v in vec) + ")"
                formatted_vectors.append(f"Vector {i + 1}: {formatted_vec}")
            return "<br>".join(formatted_vectors)

        except Exception as e:
            QMessageBox.critical(None, "Formatting Error", f"Error formatting eigenvectors.\n\nDetails: {e}")
            return "Error"

    def to_scientific(self, value):

        try:

            base, exp = f"{value:.3e}".split('e')
            return f"{float(base):.3f} × 10<sup>{int(exp)}</sup>"

        except Exception as e:
            QMessageBox.critical(None, "Scientific Notation Error", f"Error converting to scientific notation.\n\nDetails: {e}")
            return "Error"

import numpy as np
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class ForthPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("page4_i.ui", self)

        self.pushButton_2.clicked.connect(self.add_element)
        self.pushButton.clicked.connect(self.solve_button)

    def add_element(self):
        new_text = ', '.join(self.lineEdit.text().split())
        current_text = self.label_6.text()

        updated_text = f"{current_text}\n{new_text}" if current_text else new_text
        self.label_6.setText(updated_text)

    def solve_button(self):
        mat = np.array(self.give_proper_matrix(self.label_6.text().split("\n")))

        try:
            inverse = np.linalg.inv(mat)
            self.call_window = ForthPageTwo(inverse)
            widget.addWidget(self.call_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        except np.linalg.LinAlgError:
            print("Matrix is not invertible.")
            QMessageBox.critical(self, "Error", "The matrix is not invertible.")

    def give_proper_matrix(self, matrix_text):
        matrix = []
        for row in matrix_text:
            try:
                matrix.append([float(num) for num in row.split(',')])
            except ValueError:
                QMessageBox.critical(self, "Error", "Invalid input. Please enter numeric values.")
                return []
        return matrix


class ForthPageTwo(QMainWindow):
    def __init__(self, inverse_matrix):
        super().__init__()
        loadUi("page4_ii.ui", self)

        formatted_rows = []
        for row in inverse_matrix:
            formatted_row = ", ".join(f"{num:.2f}" for num in row)
            formatted_rows.append(f"[ {formatted_row} ]")

        inverse_text = "\n".join(formatted_rows)
        self.label_4.setText(inverse_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    main_wind = FirstPage()
    widget.addWidget(main_wind)
    widget.setFixedSize(main_wind.size())
    widget.show()
    sys.exit(app.exec())
