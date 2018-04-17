class Parrot:
    def __init__(self, base_speed=12.0):
        self._base_speed = base_speed

    def speed(self):
        pass


class ParrotEuropean(Parrot):
    def __init__(self):
        super().__init__()

    def speed(self):
        return self._base_speed


class ParrotAfrican(Parrot):
    def __init__(self, number_of_coconuts, load_factor=9.0):
        super().__init__()
        self.coconuts_weight = number_of_coconuts * load_factor

    def speed(self):
        return max(0.0, self._base_speed - self.coconuts_weight)


class ParrotNorwegianBlue(Parrot):
    def __init__(self, voltage, nailed):
        super().__init__()
        self.nailed = nailed
        self.voltage = voltage

    def speed(self):
        if self.nailed:
            return 0
        else:
            return min(24.0, self.voltage * self._base_speed)
