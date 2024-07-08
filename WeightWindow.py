from NewWindow import NewWindow


class WeightWindow(NewWindow):
    def __init__(self):
        super().__init__()

        self.__multipliers = {
            'Миллиграмм': 1000000,
            'Грамм': 1000,
            'Килограмм': 1,
            'Унция': 35.27,
            'Фунт': 2.205,
            'Центнер': 0.01,
            'Тонна': 0.001
        }

        self.setMultipliers(self.__multipliers)
