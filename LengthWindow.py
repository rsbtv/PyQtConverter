from NewWindow import NewWindow


class LengthWindow(NewWindow):
    def __init__(self):
        super().__init__()

        self.__multipliers = {
            'Ангстрем': 10_000_000_000,
            'Нанометр': 1_000_000_000,
            'Микрометр': 1_000_000,
            'Миллиметр': 1_000,
            'Сантиметр': 100,
            'Дециметр': 10,
            'Дюйм': 39.37,
            'Фунт': 3.281,
            'Метр': 1,
            'Ярд': 1.094,
            'Миля': 0.0006214,
            'Километр': .001
        }

        self.setWindowTitle("Длина")
        self.setMultipliers(self.__multipliers)
