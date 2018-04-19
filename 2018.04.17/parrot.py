BASE_SPEED = 12.0
NORWEGIAN_MAX_SPEED = 24.0


class BaseParrot:
    _load_factor = 9.0

    def __init__(self, number_of_coconuts, voltage, nailed):
        self.number_of_coconuts = number_of_coconuts
        self.voltage = voltage
        self.nailed = nailed

    def speed(self):
        raise NotImplementedError


class EuropeanParrot(BaseParrot):
    def speed(self):
        return BASE_SPEED


class AfricanParrot(BaseParrot):
    def speed(self):
        coconut_weight = self._load_factor * self.number_of_coconuts
        return max(0, BASE_SPEED - coconut_weight)


class NorwegianParrot(BaseParrot):
    def speed(self):
        if self.nailed:
            return 0
        return min(NORWEGIAN_MAX_SPEED, self.voltage * BASE_SPEED)


def Parrot(class_, *args):
    return class_(*args)


class ParrotType:
    EUROPEAN = EuropeanParrot
    AFRICAN = AfricanParrot
    NORWEGIAN_BLUE = NorwegianParrot
