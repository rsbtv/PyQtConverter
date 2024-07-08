from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from LengthWindow import LengthWindow
from WeightWindow import WeightWindow
from MoneyWindow import MoneyWindow


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.lengthWindow = None
        self.weightWindow = None
        self.moneyWindow = None
        self.initUI()

    def initUI(self):
        btn_Length = QPushButton('Длина', self)
        btn_Weight = QPushButton('Масса', self)
        btn_Money = QPushButton('Валюта', self)

        # Подключаем слоты (обработчики событий) к кнопкам
        btn_Length.clicked.connect(self.btn_Length_clicked)
        btn_Weight.clicked.connect(self.btn_Weight_clicked)
        btn_Money.clicked.connect(self.btn_Money_clicked)

        # Создаем вертикальный контейнер и добавляем в него кнопки
        vbox = QVBoxLayout()
        vbox.addWidget(btn_Length)
        vbox.addWidget(btn_Weight)
        vbox.addWidget(btn_Money)
        # Устанавливаем макет нашему окну
        self.setLayout(vbox)
        self.setStyleSheet('''
        * {
            font-size: 25px;
        }
        
        QWidget {
            background-color: #f7f8f2;
        }
        
        QPushButton {
            background-color: #ecb78c;
            border-radius: 5px;
            padding-top: 10px;
            padding-bottom: 10px;
            color: black;
        }
        
        QPushButton::hover {
            background-color: #d4742e;
            color: #f7f8f2;
        }
        ''')

        self.setWindowTitle('Конвертер')

        self.show()

    def btn_Length_clicked(self):
        if not self.lengthWindow:
            self.lengthWindow = LengthWindow()
            self.lengthWindow.show()

    def btn_Weight_clicked(self):
        if not self.weightWindow:
            self.weightWindow = WeightWindow()
            self.weightWindow.show()

    def btn_Money_clicked(self):
        if not self.moneyWindow:
            self.moneyWindow = MoneyWindow()
            self.moneyWindow.show()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec()
