
from PyQt5.QtWidgets import*

app = QApplication([])

window = QWidget()
window.resize(215,300)

question = QLabel("Коли був створений minecraft?")
ans1 = QRadioButton("2005")
ans2 = QRadioButton("2009")
ans3 = QRadioButton("2015")
ans4 = QRadioButton("2020")

line1 = QVBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()


line1.addWidget(question)
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

question1 = QLabel("Коли була створена CS:GO?")
ans5 = QRadioButton("2012")
ans6 = QRadioButton("2015")
ans7 = QRadioButton("2020")
ans8 = QRadioButton("2023")

line4 = QHBoxLayout()
line5 = QHBoxLayout()

line1.addWidget(question1)
line1.addLayout(line4)
line1.addLayout(line5)

line4.addWidget(ans5)
line4.addWidget(ans6)

line5.addWidget(ans7)
line5.addWidget(ans8)

ans5.clicked.connect(show_win)
ans6.clicked.connect(show_lose)
ans7.clicked.connect(show_lose)
ans8.clicked.connect(show_lose)

question2 = QLabel("Коли був створений Fortnite?")
ans9 = QRadioButton("2010")
ans10 = QRadioButton("2013")
ans11 = QRadioButton("2017")
ans12 = QRadioButton("2019")

line6 = QHBoxLayout()
line7 = QHBoxLayout()

line1.addWidget(question2)
line1.addLayout(line6)
line1.addLayout(line7)

line6.addWidget(ans9)
line6.addWidget(ans10)

line7.addWidget(ans11)
line7.addWidget(ans12)


ans9.clicked.connect(show_lose)
ans10.clicked.connect(show_win)
ans11.clicked.connect(show_lose)
ans12.clicked.connect(show_lose)

window.setWindowTitle("Питання")
window.setLayout(line1)
window.show()
app.exec()


