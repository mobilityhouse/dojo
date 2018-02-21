from stringcalculator.stringcalculator import add, get_numbers
import pytest

@pytest.mark.parametrize('value, output', [
    ('', '0'),
    ('1', '1'),
    ('1,2', '3'),
    ('1,2,6', '9'),
    ('1\n3\n4', '8'),
    ('1\n,\n3', "Number expected but , found on position 3")
])
def test_add(value, output):
    assert add(value) == output


def test_get_numbers():
    assert get_numbers('1 ,2') == [1, 2]

