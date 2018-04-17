from parrot import ParrotEuropean, ParrotAfrican, ParrotNorwegianBlue


def test_speedOfEuropeanParrot():
    parrot = ParrotEuropean()
    assert parrot.speed() == 12.0


def test_speedOfAfricanParrot_With_One_Coconut():
    parrot = ParrotAfrican(1)
    assert parrot.speed() == 3.0


def test_speedOfAfricanParrot_With_Two_Coconuts():
    parrot = ParrotAfrican(2)
    assert parrot.speed() == 0.0


def test_speedOfAfricanParrot_With_No_Coconuts():
    parrot = ParrotAfrican(0)
    assert parrot.speed() == 12.0


def test_speedNorwegianBlueParrot_nailed():
    parrot = ParrotNorwegianBlue(0, nailed=True)
    assert parrot.speed() == 0.0


def test_speedNorwegianBlueParrot_not_nailed():
    parrot = ParrotNorwegianBlue(1.5, nailed=False)
    assert parrot.speed() == 18.0


def test_speedNorwegianBlueParrot_not_nailed_high_voltage():
    parrot = ParrotNorwegianBlue(4, nailed=False)
    assert parrot.speed() == 24.0