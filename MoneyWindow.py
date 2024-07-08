from NewWindow import NewWindow


class MoneyWindow(NewWindow):
    def __init__(self):
        super().__init__()
        self.__multipliers = {
            'Доллар США': 'USD',
            'Российский рубль': 'RUB',
            'Евро': 'EUR',
        }

        self.setMoneyMode()
        self.setMultipliers(self.__multipliers)


