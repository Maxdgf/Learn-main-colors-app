from PyQt5.QtWidgets import *			
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap 
from PyQt5 import QtGui 
import sys
from PyQt5.QtGui import *

app = QApplication([])
win = QWidget()
win.resize(2000, 1000)
win.setStyleSheet("background-color : gray")
win.setWindowTitle("Learn main colors")

btn_color_one = QPushButton("color 1")
btn_color_one.setStyleSheet("background-color : green")
btn_color_two = QPushButton("color 2")
btn_color_two.setStyleSheet("background-color : red")
btn_color_three = QPushButton("color 3")
btn_color_three.setStyleSheet("background-color : blue")
btn_color_four = QPushButton("color 4")
btn_color_four.setStyleSheet("background-color : yellow")
btn_color_five = QPushButton("color 5")
btn_color_five.setStyleSheet("background-color : orange")
btn_color_six = QPushButton("color 6")
btn_color_six.setStyleSheet("background-color : brown")
btn_color_seven = QPushButton("color 7")
btn_color_seven.setStyleSheet("background-color : pink")
btn_color_eight = QPushButton("color 8")
btn_color_eight.setStyleSheet("background-color : violet")
btn_clear = QPushButton("Clear all")
btn_clear.setStyleSheet("background-color : tomato")
feel = QLabel("Learn main colors")
feel.setStyleSheet("background-color : white")
feel.setFixedSize(2000, 800)

row_tools = QVBoxLayout() 
row = QVBoxLayout() 


col1 = QHBoxLayout()
col2 = QHBoxLayout()
col3 = QHBoxLayout()
col4 = QVBoxLayout()
col5 = QHBoxLayout()

col1.addWidget(btn_color_one)
col1.addWidget(btn_color_five)
col2.addWidget(btn_color_two)
col2.addWidget(btn_color_four)
col3.addWidget(btn_color_three)
col3.addWidget(btn_color_six)
col4.addWidget(btn_color_seven)
col4.addWidget(btn_color_eight)
col4.addWidget(btn_clear)
col4.addWidget(feel)


row.addLayout(col3, 40)
row.addLayout(col2, 40)
row.addLayout(col1, 40)
row.addLayout(col4, 40)
win.setLayout(row)
win.show()


def one_action(self):
    feel.setText("                   Зелёный\n"
                 "                    (green)")
    feel.setStyleSheet("background-color : green")
    feel.setFont(QFont('Arial', 100))

def two_action(self):
    feel.setText("                   Красный\n"
                 "                    (red)")
    feel.setStyleSheet("background-color : red")
    feel.setFont(QFont('Italic', 100))

def three_action(self):
    feel.setText("                   Синий\n"
                 "                   (blue)")
    feel.setStyleSheet("background-color : blue")
    feel.setFont(QFont('Italic', 100))

def four_action(self):
    feel.setText("                    Жёлтый\n"
                 "                    (yellow)")
    feel.setStyleSheet("background-color : yellow")
    feel.setFont(QFont('Italic', 100))

def five_action(self):
    feel.setText("                   Оранжевый\n"
                 "                    (orange)")
    feel.setStyleSheet("background-color : orange")
    feel.setFont(QFont('Italic', 100))

def six_action(self):
    feel.setText("                   Коричневый\n"
                 "                    (brown)")
    feel.setStyleSheet("background-color : brown")
    feel.setFont(QFont('Italic', 100))

def seven_action(self):
    feel.setText("                   Розовый\n"
                 "                    (pink)")
    feel.setStyleSheet("background-color : pink")
    feel.setFont(QFont('Italic', 100))

def eight_action(self):
    feel.setText("                   Фиолетовый\n"
                 "                    (violet)")
    feel.setStyleSheet("background-color : violet")
    feel.setFont(QFont('Italic', 100))

def clear(self):
    feel.setText("Learn main colors")
    feel.setStyleSheet("background-color : white")
    feel.setFont(QFont('Normal', 8))

btn_color_one.clicked.connect(one_action)
btn_color_two.clicked.connect(two_action)
btn_color_three.clicked.connect(three_action)
btn_color_four.clicked.connect(four_action)
btn_color_five.clicked.connect(five_action)
btn_color_six.clicked.connect(six_action)
btn_color_seven.clicked.connect(seven_action)
btn_color_eight.clicked.connect(eight_action)
btn_clear.clicked.connect(clear)

app.exec()
