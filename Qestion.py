from PyQt5.QtWidgets import*

app = QApplication([])

window = QWidget()
window.resize(215,100)

ans = QLabel("Коли був створений minecraft?")
ans1 = QRadioButton("2005")
ans2 = QRadioButton("2009")
ans3 = QRadioButton("2015")
ans4 = QRadioButton("2020")

line1 = QVBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()


line1.addWidget(ans)
line1.addLayout(line2)
line1.addLayout(line3)

line2.addWidget(ans1)
line2.addWidget(ans2)

line3.addWidget(ans3)
line3.addWidget(ans4)

def show_win():
    victory_win = QMessageBox()
    victory_win.setText("Ця відповідь правильна")
    victory_win.exec_()

def show_lose():
    lose = QMessageBox()
    lose.setText("Це відповідь неправильна ")
    lose.exec_()

ans1.clicked.connect(show_lose)
ans2.clicked.connect(show_win)
ans3.clicked.connect(show_lose)
ans4.clicked.connect(show_lose)

window.setWindowTitle("Питання")
window.setLayout(line1)
window.show()
app.exec()
