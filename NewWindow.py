from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QLineEdit
from forex_python import converter
from forex_python.converter import CurrencyRates


class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.line_secondOperand = None
        self.cmb_secondOperand = None
        self.line_firstOperand = None
        self.cmb_firstOperand = None
        self.__multipliers = None
        self.__isMoneyMode = False
        self.currencyRate = None

        self.initUI()

    def setMoneyMode(self):
        self.__isMoneyMode = True

    def setMultipliers(self, newMultipliers):
        self.__multipliers = newMultipliers

        self.cmb_firstOperand.addItems(self.__multipliers.keys())
        self.cmb_secondOperand.addItems(self.__multipliers.keys())

        if self.__isMoneyMode:
            self.line_firstOperand.textChanged.connect(self.moneyConverting)
            self.cmb_firstOperand.currentTextChanged.connect(self.moneyConverting)
            self.cmb_secondOperand.currentTextChanged.connect(self.moneyConverting)
            self.currencyRate = CurrencyRates()
        else:
            self.line_firstOperand.textChanged.connect(self.converting)
            self.cmb_firstOperand.currentTextChanged.connect(self.converting)
            self.cmb_secondOperand.currentTextChanged.connect(self.converting)

    def initUI(self):
        self.cmb_firstOperand = QComboBox(self)
        self.line_firstOperand = QLineEdit(self)
        self.cmb_secondOperand = QComboBox(self)
        self.line_secondOperand = QLineEdit(self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.cmb_firstOperand)
        vbox.addWidget(self.line_firstOperand)
        vbox.addWidget(self.cmb_secondOperand)
        vbox.addWidget(self.line_secondOperand)

        self.setStyleSheet('''
        * {
            font-size: 25px;
        }

        QLineEdit {
        border: 2px solid #6da681;
        border-radius: 5px;
        }

        QMainWindow {
            background-color: #f7f8f2;  
        }
        ''')
        # Устанавливаем макет нашему окну
        self.setLayout(vbox)

        self.line_secondOperand.setEnabled(False)

    def converting(self):
        if not (self.line_firstOperand.text() == ''):
            try:
                result = (float(self.line_firstOperand.text())
                              / self.__multipliers[self.cmb_firstOperand.currentText()]
                              * self.__multipliers[self.cmb_secondOperand.currentText()])
                self.line_secondOperand.setText(str(result))
            except ValueError:
                pass

    def moneyConverting(self):
        if not (self.line_firstOperand.text() == ''):
            try:
                result = self.currencyRate.convert(self.__multipliers[self.cmb_firstOperand.currentText()],
                                                   self.__multipliers[self.cmb_secondOperand.currentText()],
                                                   float(self.line_firstOperand.text()))
                self.line_secondOperand.setText(str(result))
            except ValueError:
                pass

            except Exception as e:
                # self.line_secondOperand.setText(e)
                print(e)
